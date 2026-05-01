// Render each Exhibit HTML to a 2x-DPR PNG matching the existing convention
// (1200 logical px × natural height, captured at deviceScaleFactor 2 → 2400px wide).
// Run with: node render_pngs.js   (puppeteer auto-downloads chromium on first run)

const puppeteer = require('puppeteer');
const path = require('path');

const exhibits = [
  'Regime_Change_Infographic.html',
  'Winter_Baseline_Infographic.html',
  'Exhibit_C_Storage_Capacity.html',
  'Exhibit_D_Bryson_Timeline.html',
  'Exhibit_E_Climate_Tested.html',
];

(async () => {
  const browser = await puppeteer.launch({
    headless: 'new',
    args: ['--no-sandbox', '--disable-setuid-sandbox'],
  });
  const page = await browser.newPage();
  await page.setViewport({ width: 1200, height: 1500, deviceScaleFactor: 2 });

  for (const file of exhibits) {
    const htmlPath = path.resolve(__dirname, file);
    const url = 'file://' + htmlPath;
    const pngPath = htmlPath.replace(/\.html$/, '.png');
    console.log(`rendering ${file} ...`);
    await page.goto(url, { waitUntil: 'networkidle0' });
    // Allow webfont + script-driven SVG to settle
    await new Promise(r => setTimeout(r, 800));
    // Get the page's natural height
    const bodyHeight = await page.evaluate(() => {
      const page = document.querySelector('.page');
      return page ? Math.ceil(page.getBoundingClientRect().bottom + 40) : document.body.scrollHeight;
    });
    await page.setViewport({ width: 1200, height: bodyHeight, deviceScaleFactor: 2 });
    await new Promise(r => setTimeout(r, 200));
    await page.screenshot({ path: pngPath, type: 'png', fullPage: false, omitBackground: false });
    console.log(`  → ${path.basename(pngPath)}`);
  }

  await browser.close();
  console.log('done.');
})();
