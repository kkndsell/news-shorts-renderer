// Deterministic frame capture: time is driven by window.__step, CSS transitions are paused and advanced frame by frame.
// usage: node rec.js <page.html> <seconds> <outDir>
const { chromium } = require('playwright');
const fs = require('fs');
const path = require('path');
(async () => {
  const [page_, seconds, outDir] = [process.argv[2], Number(process.argv[3]), process.argv[4]];
  fs.rmSync(outDir, { recursive: true, force: true }); fs.mkdirSync(outDir, { recursive: true });
  const browser = await chromium.launch();
  const page = await browser.newPage({ viewport: { width: 1080, height: 1920 }, deviceScaleFactor: 1 });
  await page.goto('file://' + path.resolve(page_));
  await page.evaluate(() => document.fonts.ready);
  await page.evaluate(() => {
    window.__T = 0;
    window.__step = (dt) => {
      document.getAnimations().forEach((a) => { if (!a.__init) { a.__init = 1; a.pause(); a.currentTime = 0; } });
      window.__T += dt; window.renderAt(window.__T);
      document.getAnimations().forEach((a) => {
        if (!a.__init) { a.__init = 1; a.pause(); a.currentTime = 0; return; }
        const d = a.effect.getComputedTiming().endTime; a.currentTime = Math.min((a.currentTime || 0) + dt * 1000, d);
      });
    };
  });
  const fps = 30, N = Math.round(seconds * fps);
  for (let i = 0; i < N; i++) {
    await page.evaluate((dt) => window.__step(dt), 1 / fps);
    await page.screenshot({ path: `${outDir}/${String(i).padStart(5, '0')}.png` });
  }
  await browser.close();
  console.log('frames', N);
})();
