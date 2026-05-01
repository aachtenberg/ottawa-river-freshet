"""Scrape ORRPB historical summary pages into per-station CSV files.

Discovers station pages from the ORRPB historical-summary hub, parses each
station table, and writes one archival CSV per station plus a manifest CSV.

Stdlib-only, matching the repo's existing ingestion scripts.
"""

import csv
import os
import re
import sys
import urllib.parse
import urllib.request
from html.parser import HTMLParser

HUB_URL = 'https://www.ottawariver.ca/information/historical-data-summaries-water-levels-and-flows/'
PAGE_PREFIX = HUB_URL
USER_AGENT = os.environ.get(
    'SCRAPE_USER_AGENT',
    'freshet/1.0 (+https://github.com/aachtenberg/ottawa-river-freshet; community flood monitoring)',
)
DEFAULT_OUTPUT_DIR = os.path.abspath(
    os.path.join(os.path.dirname(__file__), '..', '..', 'data', 'orrpb-historical-summaries')
)
MONTH_COLUMNS = ['jan', 'feb', 'mar', 'apr', 'may', 'jun', 'jul', 'aug', 'sep', 'oct', 'nov', 'dec']
CSV_COLUMNS = ['year', *MONTH_COLUMNS, 'annual_mean', 'daily_max', 'daily_min']


def fetch_html(url):
    req = urllib.request.Request(url, headers={
        'User-Agent': USER_AGENT,
        'Accept': 'text/html,application/xhtml+xml',
    })
    with urllib.request.urlopen(req, timeout=30) as response:
        return response.read().decode('utf-8', errors='replace')


def clean_text(text):
    return re.sub(r'\s+', ' ', text or '').strip()


def slug_from_url(url):
    parsed = urllib.parse.urlparse(url)
    return parsed.path.rstrip('/').split('/')[-1]


def detect_measure(meta_text):
    lowered = meta_text.lower()
    if 'discharge' in lowered:
        return 'discharge', 'cubic_metres_per_second'
    if 'water level' in lowered:
        return 'water_level', 'metres'
    return 'unknown', ''


class HubParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.links = []
        self._current_href = None
        self._current_text = []

    def handle_starttag(self, tag, attrs):
        if tag != 'a':
            return
        attrs_dict = dict(attrs)
        self._current_href = attrs_dict.get('href')
        self._current_text = []

    def handle_data(self, data):
        if self._current_href is not None:
            self._current_text.append(data)

    def handle_endtag(self, tag):
        if tag != 'a' or self._current_href is None:
            return
        href = urllib.parse.urljoin(HUB_URL, self._current_href)
        text = clean_text(''.join(self._current_text))
        if href.startswith(PAGE_PREFIX) and href.rstrip('/') != HUB_URL.rstrip('/') and text:
            self.links.append((href, text))
        self._current_href = None
        self._current_text = []


class DetailPageParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.title = ''
        self.tables = []
        self._in_h1 = False
        self._h1_text = []
        self._current_table = None
        self._current_row = None
        self._current_cell = None

    def handle_starttag(self, tag, attrs):
        if tag == 'h1' and not self.title:
            self._in_h1 = True
            self._h1_text = []
            return
        if tag == 'table':
            self._current_table = []
            self.tables.append(self._current_table)
            return
        if tag == 'tr' and self._current_table is not None:
            self._current_row = []
            self._current_table.append(self._current_row)
            return
        if tag in ('td', 'th') and self._current_row is not None:
            self._current_cell = []
            self._current_row.append(self._current_cell)

    def handle_data(self, data):
        if self._in_h1:
            self._h1_text.append(data)
        if self._current_cell is not None:
            self._current_cell.append(data)

    def handle_endtag(self, tag):
        if tag == 'h1' and self._in_h1:
            title = clean_text(''.join(self._h1_text))
            if title:
                self.title = title
            self._in_h1 = False
            self._h1_text = []
            return
        if tag == 'table':
            self._current_table = None
            return
        if tag == 'tr':
            self._current_row = None
            return
        if tag in ('td', 'th'):
            self._current_cell = None


def cell_text(cell):
    return clean_text(''.join(cell))


def discover_station_pages():
    parser = HubParser()
    parser.feed(fetch_html(HUB_URL))
    seen = set()
    pages = []
    for href, text in parser.links:
        key = href.rstrip('/')
        if key in seen:
            continue
        seen.add(key)
        pages.append({'url': href, 'title': text, 'slug': slug_from_url(href)})
    return pages


def find_summary_table(tables):
    for table in tables:
        for row in table:
            cells = [cell_text(cell) for cell in row]
            if cells[:4] == ['Year', 'Jan', 'Feb', 'Mar']:
                return table
    return None


def extract_table_metadata(table):
    for row in table[:3]:
        cells = [cell_text(cell) for cell in row]
        text = ' | '.join(cell for cell in cells if cell)
        if 'Monthly and Annual' in text:
            return text
    return ''


def normalize_value(text):
    value = clean_text(text)
    if not value:
        return ''
    if value.upper() == 'NA':
        return 'NA'
    match = re.match(r'^(-?\d+(?:\.\d+)?)', value)
    if match:
        return match.group(1)
    return value


def extract_year_rows(table):
    rows = []
    header_seen = False
    for raw_row in table:
        cells = [cell_text(cell) for cell in raw_row]
        if not cells:
            continue
        if cells[:4] == ['Year', 'Jan', 'Feb', 'Mar']:
            header_seen = True
            continue
        if not header_seen:
            continue
        first = cells[0]
        if first.startswith('Mean - '):
            break
        if not re.fullmatch(r'\d{4}', first):
            continue
        values = [normalize_value(value) for value in cells[1:16]]
        if len(values) != 15:
            raise ValueError(f'Unexpected row width for year {first}: {cells!r}')
        row = {'year': first}
        for key, value in zip(CSV_COLUMNS[1:], values):
            row[key] = value
        rows.append(row)
    if not rows:
        raise ValueError('No yearly data rows found in summary table')
    return rows


def parse_station_page(page):
    html = fetch_html(page['url'])
    parser = DetailPageParser()
    parser.feed(html)
    table = find_summary_table(parser.tables)
    if table is None:
        raise ValueError('Could not find summary table on page')
    metadata_text = extract_table_metadata(table)
    measure_type, unit = detect_measure(metadata_text)
    if measure_type == 'unknown':
        measure_type, unit = detect_measure(html)
    rows = extract_year_rows(table)
    return {
        'slug': page['slug'],
        'title': parser.title or page['title'],
        'source_url': page['url'],
        'measure_type': measure_type,
        'unit': unit,
        'rows': rows,
    }


def write_station_csv(output_dir, station):
    path = os.path.join(output_dir, f"{station['slug']}.csv")
    with open(path, 'w', newline='', encoding='utf-8') as handle:
        writer = csv.DictWriter(handle, fieldnames=CSV_COLUMNS)
        writer.writeheader()
        writer.writerows(station['rows'])
    return path


def write_manifest(output_dir, manifest_rows):
    path = os.path.join(output_dir, 'manifest.csv')
    columns = ['slug', 'title', 'measure_type', 'unit', 'source_url', 'row_count', 'first_year', 'last_year', 'output_csv']
    with open(path, 'w', newline='', encoding='utf-8') as handle:
        writer = csv.DictWriter(handle, fieldnames=columns)
        writer.writeheader()
        writer.writerows(manifest_rows)
    return path


def main(argv):
    output_dir = argv[1] if len(argv) > 1 else os.environ.get('OUTPUT_DIR', DEFAULT_OUTPUT_DIR)
    os.makedirs(output_dir, exist_ok=True)

    print(f'Fetching hub page: {HUB_URL}')
    pages = discover_station_pages()
    print(f'Discovered {len(pages)} station pages')

    manifest_rows = []
    failures = []
    for page in pages:
        try:
            station = parse_station_page(page)
            output_path = write_station_csv(output_dir, station)
            years = [int(row['year']) for row in station['rows']]
            manifest_rows.append({
                'slug': station['slug'],
                'title': station['title'],
                'measure_type': station['measure_type'],
                'unit': station['unit'],
                'source_url': station['source_url'],
                'row_count': len(station['rows']),
                'first_year': min(years),
                'last_year': max(years),
                'output_csv': os.path.basename(output_path),
            })
            print(f"  wrote {station['slug']}.csv ({len(station['rows'])} rows)")
        except Exception as exc:
            failures.append((page['url'], str(exc)))
            print(f"  failed {page['url']}: {exc}", file=sys.stderr)

    manifest_path = write_manifest(output_dir, manifest_rows)
    print(f'Wrote manifest: {manifest_path}')

    if failures:
        print(f'{len(failures)} pages failed', file=sys.stderr)
        return 1
    return 0


if __name__ == '__main__':
    raise SystemExit(main(sys.argv))