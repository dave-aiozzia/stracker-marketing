# Stracker Intro — Sales Video

**75-second animated teaser** introducing Stracker to prospective B2B clients.

## Watch
- **Final cut:** `output/stracker-intro-1080p.mp4` (1920×1080, 60fps, ~3MB)
- **Draft:** `output/stracker-intro-480p.mp4` (854×480, 15fps, ~1MB)

## What it shows
1. **Hook** — sales chaos (spreadsheets, sticky notes, chat)
2. **Logo reveal** — Stracker crosshairs + tagline
3. **Dashboard** — KPIs, revenue chart, recent leads
4. **Pipeline** — lead card animates through 5 stages to "WON"
5. **Billing portal** — customer's substracker.io view with invoices
6. **CTA** — strackerapp.com

## How to rebuild

### Prereqs
- Python 3.10+
- Manim CE (`pip install manim`)
- ffmpeg
- LaTeX (optional, for `MathTex`)

### Render a single scene
```bash
manim -ql script.py Scene1_Hook      # 480p draft
manim -qm script.py Scene1_Hook      # 720p
manim -qh script.py Scene1_Hook      # 1080p (slow, best quality)
```

### Render all 6
```bash
for scene in Scene1_Hook Scene2_Logo Scene3_Dashboard Scene4_Pipeline Scene5_Portal Scene6_CTA; do
  manim -qh script.py $scene
done
```

### Stitch into one MP4
```bash
ffmpeg -y -f concat -safe 0 -i concat-1080.txt -c copy output/stracker-intro-1080p.mp4
```

## Add background music
Drop a track into `audio/` (e.g. `audio/track.mp3`), then:
```bash
ffmpeg -i output/stracker-intro-1080p.mp4 -i audio/track.mp3 \
  -c:v copy -c:a aac -shortest output/stracker-intro-with-music.mp4
```

## Customize
- **Copy/captions** — search `add_subcaption` in `script.py` to rewrite
- **Colors** — change the brand constants at the top (`TEAL`, `ORANGE`, etc.)
- **Logo** — replace `assets/stracker-logo-transparent.png` with your own
- **Length** — add/remove `self.wait()` calls or trim `add_subcaption` durations

## License
Internal Stracker marketing asset.
