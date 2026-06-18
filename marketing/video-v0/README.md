# video-v0

Silent, programmatically-rendered v0 of the 45s explainer video.

## What's here

- `render.py` — the renderer (Python + Pillow + imageio-ffmpeg)
- `fonts/` — bundled Lato + Caveat for consistent rendering
- `we-the-repo-v0.mp4` — output (silent, captions integrated into scenes)

## Why programmatic

Every frame is reproducible from source. Treat the video like code: PRs against `render.py` change the video. Diffs are reviewable. No proprietary file format. No "lost the .ai file" risk.

## Run it

```bash
pip install pillow imageio imageio-ffmpeg numpy
python3 render.py          # full 1920x1080 30fps
python3 render.py --fast   # 15fps preview (still 1080p)
python3 render.py --scrub 22  # render a single PNG at t=22s for debug
```

## Status

This is v0. Known limitations:

- No narration yet (waiting on ElevenLabs API key or human voice talent)
- File tree and CTA icons use crisp digital shapes — should be hand-drawn for full Schoolhouse Rock consistency
- No audio bed / music

## How to contribute

Open a PR against `render.py`. Scrub specific timestamps with `--scrub N.N` for fast iteration. Frame composition assumes 1920x1080 — don't change W/H constants without re-laying-out scenes.
