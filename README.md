# DrillRoom — MCAT Practice & Adaptive Question Bank

Authentic AAMC-format MCAT Practice Exam and Adaptive Passage Bank engine with real-time test telemetry, distractor autopsies, 5-Gate Review Protocol standards, and multi-device cloud synchronization.

🌐 **Live Web Application:** [https://orbgamestudios.github.io/Drillroom/](https://orbgamestudios.github.io/Drillroom/)

---

## Features

- **160 Complete Practice Sections**:
  - Full 90-minute timed exams (exact MCAT timing and section lengths).
  - 60-minute quick sections and half-sections across CARS, C/P, B/B, and P/S.
- **5-Gate Crucible Standard**:
  - 3-step cognitive derivations on every question.
  - Active distractor trap autopsies (`Gate 5`).
  - Strict choice length parity (ratio $\le 1.080\times$, correct answer never the longest choice giveaway).
  - Balanced 25% answer distribution.
- **Global Cross-Exam Deduplication**:
  - 324 unique passage fingerprints.
  - Zero duplicate passages across 60m and 90m sections during adaptive study.
  - Auto-skips previously completed passages with full score isolation.
- **Authentic MCAT Interface**:
  - Real-feel AAMC navigation bar and colors.
  - Periodic table, highlight, strikethrough, and pause.
  - Hidden analytical passage reading telemetry (calculates passage reading speed without artificial timers).
- **Multi-Device Cloud Synchronization**:
  - Create an account with a **Username** and **4-Digit PIN**.
  - Log in from any computer or mobile browser to sync completed passages, scores, and exam history.
  - Smart 3-way union merge ensures zero progress is lost across devices.
  - Powered by Cloudflare Workers and Cloudflare KV.

---

## Multi-Device Cloud Sync

1. Click **☁️ Cloud Sync** in the top navigation bar or on the home screen.
2. Enter your **Username** (e.g., `orbgames`) and **4-Digit PIN** (e.g., `1234`).
3. Click **Create Account** on your first device.
4. On any other computer or mobile device, open the site, click **☁️ Cloud Sync**, enter your username and PIN, and click **Log In & Sync**. All your progress will instantly appear.

### Cloudflare Worker Backend

The sync service is powered by the included Cloudflare Worker in `worker/index.js`.

To deploy your own worker:
```bash
npm install
npm run deploy:worker
```

---

## Running Tests

Verify all 138 test cases across deduplication, authentic MCAT UI controls, and multi-device cloud sync:

```bash
npm test
```
