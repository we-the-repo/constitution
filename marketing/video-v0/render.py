#!/usr/bin/env python3
"""
we-the-repo v0 explainer video.

Renders a 45s 1920x1080 30fps MP4. Silent (narration added later via sag/ElevenLabs).
Style: flat shapes, off-white paper background, hand-drawn-ish wobble, Schoolhouse Rock DNA
with a modern git/repo motif. Three 15s acts.

Run: python3 render.py [--fast]
  --fast renders 480p at 15fps for quick preview.
"""
from __future__ import annotations
import argparse
import math
import os
import random
from pathlib import Path

import imageio.v2 as imageio
import numpy as np
from PIL import Image, ImageDraw, ImageFilter, ImageFont

# ---------- Config ----------
FPS = 30
DURATION = 45  # seconds
W, H = 1920, 1080

# Palette (per SCRIPT-v0.md)
PAPER = (250, 247, 240)
INK = (26, 26, 26)
RED = (200, 16, 46)
GREEN = (46, 125, 50)
BLUE = (21, 101, 192)
YELLOW = (255, 213, 79)
DIM = (140, 140, 140)

OUT_DIR = Path(__file__).parent
OUT_FILE = OUT_DIR / "we-the-repo-v0.mp4"

# Bundled fonts
FONT_DIR = Path(__file__).parent / "fonts"
FONT_REG = FONT_DIR / "Lato-Regular.ttf"
FONT_BOLD = FONT_DIR / "Lato-Bold.ttf"
FONT_HAND = FONT_DIR / "Caveat-Bold.ttf"


def font(size: int, bold: bool = False, hand: bool = False) -> ImageFont.ImageFont:
    if hand and FONT_HAND.exists():
        try:
            return ImageFont.truetype(str(FONT_HAND), size)
        except Exception:
            pass
    path = FONT_BOLD if bold else FONT_REG
    if path.exists():
        try:
            return ImageFont.truetype(str(path), size)
        except Exception:
            pass
    return ImageFont.load_default()


def ease_in_out(t: float) -> float:
    return 0.5 - 0.5 * math.cos(math.pi * max(0.0, min(1.0, t)))


def clamp01(t: float) -> float:
    return max(0.0, min(1.0, t))


def paper_bg(seed: int = 0) -> Image.Image:
    """Off-white paper with subtle noise."""
    img = Image.new("RGB", (W, H), PAPER)
    rng = np.random.default_rng(seed)
    # Light grain
    noise = rng.integers(-4, 4, size=(H, W, 1), dtype=np.int16)
    arr = np.array(img, dtype=np.int16) + noise
    arr = np.clip(arr, 0, 255).astype(np.uint8)
    return Image.fromarray(arr)


def wobble(p, amount=2, seed=0):
    """Add hand-drawn wobble to a point."""
    rng = random.Random(seed)
    return (p[0] + rng.uniform(-amount, amount), p[1] + rng.uniform(-amount, amount))


def hand_line(draw, p1, p2, fill=INK, width=4, seed=0, segments=12):
    """Draw a wobbly line for hand-drawn feel."""
    rng = random.Random(seed)
    pts = []
    for i in range(segments + 1):
        t = i / segments
        x = p1[0] + (p2[0] - p1[0]) * t
        y = p1[1] + (p2[1] - p1[1]) * t
        if 0 < i < segments:
            x += rng.uniform(-2, 2)
            y += rng.uniform(-2, 2)
        pts.append((x, y))
    draw.line(pts, fill=fill, width=width, joint="curve")


def hand_rect(draw, box, fill=None, outline=INK, width=4, seed=0):
    x1, y1, x2, y2 = box
    if fill is not None:
        draw.rectangle(box, fill=fill)
    hand_line(draw, (x1, y1), (x2, y1), outline, width, seed)
    hand_line(draw, (x2, y1), (x2, y2), outline, width, seed + 1)
    hand_line(draw, (x2, y2), (x1, y2), outline, width, seed + 2)
    hand_line(draw, (x1, y2), (x1, y1), outline, width, seed + 3)


def draw_person(draw, cx, cy, scale=1.0, color=INK, seed=0):
    """Schoolhouse Rock-ish stick person."""
    s = scale
    # Head
    r = int(40 * s)
    draw.ellipse([cx - r, cy - 160 * s, cx + r, cy - 160 * s + 2 * r], outline=color, width=int(5 * s))
    # Body
    hand_line(draw, (cx, cy - 120 * s), (cx, cy + 20 * s), color, int(5 * s), seed)
    # Arms
    hand_line(draw, (cx, cy - 90 * s), (cx - 70 * s, cy - 40 * s), color, int(5 * s), seed + 1)
    hand_line(draw, (cx, cy - 90 * s), (cx + 70 * s, cy - 40 * s), color, int(5 * s), seed + 2)
    # Legs
    hand_line(draw, (cx, cy + 20 * s), (cx - 50 * s, cy + 120 * s), color, int(5 * s), seed + 3)
    hand_line(draw, (cx, cy + 20 * s), (cx + 50 * s, cy + 120 * s), color, int(5 * s), seed + 4)


def draw_briefcase(draw, cx, cy, scale=1.0):
    w, h = int(120 * scale), int(80 * scale)
    box = (cx - w // 2, cy - h // 2, cx + w // 2, cy + h // 2)
    hand_rect(draw, box, fill=(60, 40, 30), outline=INK, width=3)
    # Handle (top, above the case)
    hh = int(20 * scale)
    handle_top_y = cy - h // 2 - hh
    hand_line(draw, (cx - 30 * scale, cy - h // 2),
              (cx - 30 * scale, handle_top_y), INK, 3, seed=99)
    hand_line(draw, (cx - 30 * scale, handle_top_y),
              (cx + 30 * scale, handle_top_y), INK, 3, seed=100)
    hand_line(draw, (cx + 30 * scale, handle_top_y),
              (cx + 30 * scale, cy - h // 2), INK, 3, seed=101)
    # $$$ on the case
    f = font(int(32 * scale), bold=True)
    draw_text_centered(draw, "$$$", int(cx), int(cy), size=int(32 * scale), color=YELLOW, bold=True)


def draw_scroll(draw, cx, cy, scale=1.0, color=INK, with_eyes=True, sad=True):
    """Schoolhouse Rock 'Bill' character — a scroll."""
    w, h = int(140 * scale), int(180 * scale)
    box = (cx - w // 2, cy - h // 2, cx + w // 2, cy + h // 2)
    hand_rect(draw, box, fill=(255, 245, 200), outline=color, width=4, seed=11)
    # Curl top
    draw.arc([cx - w // 2 - 10, cy - h // 2 - 20, cx + w // 2 + 10, cy - h // 2 + 20],
             180, 360, fill=color, width=4)
    # Lines (text marks)
    for i in range(3):
        y = cy - 30 * scale + i * 25 * scale
        hand_line(draw, (cx - 40 * scale, y), (cx + 40 * scale, y), color, 2, seed=20 + i)
    if with_eyes:
        # eyes
        draw.ellipse([cx - 25 * scale, cy - 70 * scale, cx - 10 * scale, cy - 55 * scale], fill=color)
        draw.ellipse([cx + 10 * scale, cy - 70 * scale, cx + 25 * scale, cy - 55 * scale], fill=color)
        # mouth
        if sad:
            draw.arc([cx - 20 * scale, cy - 45 * scale, cx + 20 * scale, cy - 25 * scale],
                     0, 180, fill=color, width=3)
        else:
            draw.arc([cx - 20 * scale, cy - 50 * scale, cx + 20 * scale, cy - 30 * scale],
                     180, 360, fill=color, width=3)


def draw_markdown_file(draw, cx, cy, scale=1.0, commit_dot=True, happy=True):
    """The new 'Bill' character: a Markdown file with a green commit dot."""
    w, h = int(160 * scale), int(200 * scale)
    box = (cx - w // 2, cy - h // 2, cx + w // 2, cy + h // 2)
    # Page
    hand_rect(draw, box, fill=(255, 255, 255), outline=INK, width=4, seed=31)
    # folded corner
    fx, fy = cx + w // 2, cy - h // 2
    draw.polygon([(fx - 30 * scale, fy), (fx, fy + 30 * scale), (fx - 30 * scale, fy + 30 * scale)],
                 fill=(230, 230, 230), outline=INK)
    # MD label
    f = font(int(28 * scale), bold=True)
    draw.text((cx - 35 * scale, cy - h // 2 + 15 * scale), ".md", fill=INK, font=f)
    # Heading line (#)
    f2 = font(int(20 * scale), bold=True)
    draw.text((cx - 60 * scale, cy - 30 * scale), "# Amendment", fill=BLUE, font=f2)
    for i in range(3):
        y = cy + (i * 22 - 5) * scale
        hand_line(draw, (cx - 60 * scale, y), (cx + 60 * scale, y), INK, 2, seed=40 + i)
    if commit_dot:
        # Green commit dot top-left
        r = int(18 * scale)
        draw.ellipse([cx - w // 2 - r, cy - h // 2 - r, cx - w // 2 + r, cy - h // 2 + r],
                     fill=GREEN, outline=INK, width=2)
    # Happy face
    if happy:
        eye_y = cy + 70 * scale
        draw.ellipse([cx - 25 * scale, eye_y, cx - 12 * scale, eye_y + 13 * scale], fill=INK)
        draw.ellipse([cx + 12 * scale, eye_y, cx + 25 * scale, eye_y + 13 * scale], fill=INK)
        draw.arc([cx - 25 * scale, eye_y + 5 * scale, cx + 25 * scale, eye_y + 40 * scale],
                 180, 360, fill=INK, width=3)


def draw_text_centered(draw, text, cx, cy, size=48, color=INK, bold=True, hand=False):
    f = font(size, bold=bold, hand=hand)
    bbox = draw.textbbox((0, 0), text, font=f)
    tw = bbox[2] - bbox[0]
    th = bbox[3] - bbox[1]
    draw.text((cx - tw // 2, cy - th // 2 - bbox[1]), text, fill=color, font=f)


def draw_caption(img, text, y_offset=80):
    """Burned-in caption — yellow on black bar bottom third."""
    draw = ImageDraw.Draw(img, "RGBA")
    f = font(38, bold=True)
    bbox = draw.textbbox((0, 0), text, font=f)
    tw = bbox[2] - bbox[0]
    th = bbox[3] - bbox[1]
    pad = 24
    bar_w = tw + pad * 2
    bar_h = th + pad
    bx = (W - bar_w) // 2
    by = H - y_offset - bar_h
    draw.rectangle([bx, by, bx + bar_w, by + bar_h], fill=(0, 0, 0, 210))
    draw.text((bx + pad, by + pad // 2 - 4), text, fill=YELLOW, font=f)


# ---------- Scenes ----------

def caption_for_time(t: float) -> str | None:
    """Rough caption sync with narration (for silent v0).
    Returns None when captions would clobber an illustrated focal point.
    """
    # Act 1
    if 0.5 <= t < 4.5:
        return "A lobbyist writes the bill."
    if 4.5 <= t < 8.0:
        return "A lawmaker signs it. You find out later."
    if 8.0 <= t < 12.0:
        return "We think there's a better way."
    if 12.0 <= t < 15.0:
        return None  # title text on screen — don't double caption
    # Act 2
    if 15.0 <= t < 19.0:
        return "Fork the repo."
    if 19.0 <= t < 23.0:
        return "Open a pull request."
    if 23.0 <= t < 27.0:
        return "Every voice counts the same."
    if 27.0 <= t < 30.0:
        return None  # merged stamp is the focal point
    # Act 3
    if 30.0 <= t < 34.0:
        return "No corporate money. Ever."
    if 34.0 <= t < 39.0:
        return "Star. Share. Support."
    if 39.0 <= t < 45.0:
        return None  # end card has its own taglines
    return None


def scene_act1(t: float) -> Image.Image:
    """0–15s: The old system."""
    img = paper_bg(seed=int(t * 30))
    draw = ImageDraw.Draw(img)
    local_t = t  # 0..15

    if local_t < 4.5:
        # Beat 1: Lobbyist writes the bill
        anim = ease_in_out(min(local_t / 1.5, 1.0))
        draw_text_centered(draw, "How a bill becomes a law.", W // 2, 100, size=64, color=INK, bold=True)
        draw_text_centered(draw, "(today)", W // 2, 175, size=42, color=DIM, bold=False, hand=True)
        lob_x = int(W // 2)
        hand_rect(draw, (lob_x - 320, 760, lob_x + 320, 850), fill=(180, 140, 90), outline=INK, width=4, seed=50)
        draw_person(draw, lob_x - 160, 660, scale=1.5, color=INK, seed=1)
        draw_briefcase(draw, lob_x + 220, 720, scale=1.2)
        sx = lob_x + 30
        sy = 700
        draw_scroll(draw, sx, sy, scale=0.7, color=RED, with_eyes=True, sad=True)
        pen_x = sx + int(30 * math.sin(local_t * 8))
        pen_y = sy - 30
        hand_line(draw, (pen_x, pen_y - 70), (pen_x + 5, pen_y), INK, 5, seed=int(local_t * 100))
        for i in range(int(5 * anim)):
            mx = lob_x - 320 + (i * 50)
            my = 320 + int(40 * math.sin(local_t * 3 + i))
            f3 = font(54, bold=True)
            draw.text((mx, my), "$", fill=GREEN, font=f3)
        if local_t > 1.5:
            draw_text_centered(draw, "A lobbyist writes the bill…", W // 2, 950, size=52, color=INK, bold=True)

    elif local_t < 8.0:
        # Beat 2: lawmaker signs. Voter locked out.
        anim = ease_in_out(min((local_t - 4.5) / 1.5, 1.0))
        draw_text_centered(draw, "How a bill becomes a law.", W // 2, 100, size=64, color=INK, bold=True)
        draw_text_centered(draw, "(today)", W // 2, 175, size=42, color=DIM, bold=False, hand=True)
        pol_x = 1450
        draw_person(draw, pol_x, 660, scale=1.5, color=INK, seed=2)
        hand_rect(draw, (pol_x - 110, 720, pol_x + 110, 880), fill=(180, 140, 90), outline=INK, width=4, seed=50)
        if anim > 0.5:
            hand_rect(draw, (pol_x - 95, 770, pol_x + 95, 840), fill=RED, outline=INK, width=3, seed=51)
            draw_text_centered(draw, "PASSED", pol_x, 805, size=38, color=(255, 255, 255), bold=True)
        scroll_x = int(pol_x - 230 - 60 * (1 - anim))
        draw_scroll(draw, scroll_x, 620, scale=0.7, color=RED, with_eyes=True, sad=True)
        hand_line(draw, (pol_x - 280, 460), (pol_x - 210, 620), INK, 6, seed=70)
        draw_text_centered(draw, "…a lawmaker signs it.  You find out later.", W // 2, 950, size=46, color=INK, bold=True)
        # Voter — outside, locked out (left side)
        v_x, v_y = 450, 800
        # door (closed government building)
        hand_rect(draw, (v_x - 100, v_y - 250, v_x + 100, v_y + 100), fill=(200, 200, 210), outline=INK, width=4, seed=60)
        # door panels
        draw.line([(v_x, v_y - 250), (v_x, v_y + 100)], fill=INK, width=2)
        # doorknobs
        draw.ellipse([v_x - 25, v_y - 80, v_x - 10, v_y - 65], fill=INK)
        draw.ellipse([v_x + 10, v_y - 80, v_x + 25, v_y - 65], fill=INK)
        # drawn padlock
        lk_cx, lk_cy = v_x, v_y - 70
        draw.arc([lk_cx - 30, lk_cy - 45, lk_cx + 30, lk_cy], 180, 360, fill=INK, width=6)
        hand_rect(draw, (lk_cx - 38, lk_cy - 10, lk_cx + 38, lk_cy + 40), fill=YELLOW, outline=INK, width=3, seed=62)
        draw.ellipse([lk_cx - 6, lk_cy + 5, lk_cx + 6, lk_cy + 18], fill=INK)
        # voter standing outside, looking up sadly
        vp_x = v_x - 250
        draw_person(draw, vp_x, 800, scale=1.0, color=INK, seed=80)
        # question mark over voter's head
        draw_text_centered(draw, "?", vp_x, 560, size=72, color=DIM, bold=True)

    if local_t >= 8.0:
        # Transition: clean grid, repo appears
        anim = clamp01((local_t - 8.0) / 3.0)
        # grid
        grid_alpha = int(80 * anim)
        if grid_alpha > 0:
            grid = Image.new("RGBA", (W, H), (0, 0, 0, 0))
            gd = ImageDraw.Draw(grid)
            for x in range(0, W, 60):
                gd.line([(x, 0), (x, H)], fill=(BLUE[0], BLUE[1], BLUE[2], grid_alpha), width=1)
            for y in range(0, H, 60):
                gd.line([(0, y), (W, y)], fill=(BLUE[0], BLUE[1], BLUE[2], grid_alpha), width=1)
            img = Image.alpha_composite(img.convert("RGBA"), grid).convert("RGB")
            draw = ImageDraw.Draw(img)

        # Big title
        draw_text_centered(draw, "There's a better way.", W // 2, 130, size=72, color=INK, bold=True)

        # Repo tree on left, scaled up
        if local_t > 9.0:
            tree_anim = ease_in_out(clamp01((local_t - 9.0) / 2.0))
            base_x = int(120 - 200 * (1 - tree_anim))
            f = font(44, bold=True)
            lines = [
                ("folder", "we-the-repo/", 0),
                ("folder", "amendments/", 1),
                ("file",   "28-digital-bill-of-rights.md", 2),
                ("file",   "30-direct-democracy.md", 2),
                ("folder", "process/", 1),
                ("file",   "MANIFESTO.md", 1),
                ("file",   "README.md", 1),
            ]
            for i, (kind, label, indent) in enumerate(lines):
                y = 320 + i * 80
                x = base_x + indent * 56
                if kind == "folder":
                    draw.rectangle([x, y + 14, x + 56, y + 52], fill=YELLOW, outline=INK, width=3)
                    draw.rectangle([x + 6, y + 4, x + 32, y + 18], fill=YELLOW, outline=INK, width=3)
                    color = BLUE
                else:
                    draw.rectangle([x + 6, y + 4, x + 50, y + 54], fill=(255, 255, 255), outline=INK, width=3)
                    draw.polygon([(x + 38, y + 4), (x + 50, y + 16), (x + 38, y + 16)], fill=(220, 220, 220), outline=INK)
                    for ln in range(3):
                        draw.line([(x + 12, y + 22 + ln * 9), (x + 44, y + 22 + ln * 9)], fill=DIM, width=2)
                    color = INK
                draw.text((x + 70, y + 8), label, fill=color, font=f)

        # New bill on right — happy markdown character
        if local_t > 10.5:
            new_anim = ease_in_out(clamp01((local_t - 10.5) / 2.0))
            mx = int(1500)
            my = int(950 - 350 * new_anim)
            draw_markdown_file(draw, mx, my, scale=1.4, commit_dot=True, happy=True)

        if local_t > 12.5:
            draw_text_centered(draw, "Plain English. Public. On GitHub.",
                               W // 2, 970, size=48, color=BLUE, bold=True)
    return img


def scene_act2(t: float) -> Image.Image:
    """15–30s: How to contribute."""
    img = paper_bg(seed=int(t * 30))
    draw = ImageDraw.Draw(img)
    local_t = t - 15.0  # 0..15

    # Title
    draw_text_centered(draw, "Want to help write it?", W // 2, 100, size=64, color=INK, bold=True)

    if local_t < 4.0:
        anim = ease_in_out(clamp01(local_t / 3.0))
        px = int(300 + 700 * anim)
        draw_person(draw, px, 700, scale=1.2, color=INK, seed=10)
        if local_t > 1.2:
            ax_start = px + 90
            ax_end = 1280
            ay = 660
            draw.line([(ax_start, ay), (ax_end, ay)], fill=INK, width=4)
            draw.polygon([(ax_end, ay), (ax_end - 22, ay - 12), (ax_end - 22, ay + 12)], fill=INK)
        btn_box = (1300, 590, 1760, 730)
        btn_color = GREEN if local_t > 2.5 else (220, 220, 230)
        hand_rect(draw, btn_box, fill=btn_color, outline=INK, width=4, seed=80)
        icon_x, icon_y = 1370, 660
        draw.line([(icon_x, icon_y - 30), (icon_x, icon_y + 30)], fill=INK, width=6)
        draw.line([(icon_x, icon_y - 30), (icon_x - 25, icon_y - 55)], fill=INK, width=6)
        draw.line([(icon_x, icon_y - 30), (icon_x + 25, icon_y - 55)], fill=INK, width=6)
        draw.ellipse([icon_x - 10, icon_y - 65, icon_x + 10, icon_y - 45], fill=INK)
        draw.ellipse([icon_x - 35, icon_y - 65, icon_x - 15, icon_y - 45], fill=INK)
        draw.ellipse([icon_x + 15, icon_y - 65, icon_x + 35, icon_y - 45], fill=INK)
        draw_text_centered(draw, "Fork", 1560, 660, size=54, color=INK, bold=True)
        if local_t > 0.8:
            draw_text_centered(draw, "Fork the repo.", W // 2, 980, size=56, color=GREEN, bold=True)
        if local_t > 3.0:
            # click effect
            r = int(20 + (local_t - 3.0) * 60)
            d2 = ImageDraw.Draw(img, "RGBA")
            d2.ellipse([1500 - r, 660 - r, 1500 + r, 660 + r],
                       outline=(GREEN[0], GREEN[1], GREEN[2], 180), width=4)

    elif local_t < 9.0:
        # Three contributors, three PRs
        sub_t = local_t - 4.0
        anim = ease_in_out(clamp01(sub_t / 2.0))
        positions = [(W // 4 - 40, 520), (W // 2, 520), (3 * W // 4 + 40, 520)]
        labels = ["a nurse", "a teacher", "a builder"]
        for i, (px, py) in enumerate(positions):
            ax = int(px)
            ay = int(py)
            draw_person(draw, ax, ay, scale=0.95 * (anim if anim > 0 else 0.01), color=INK, seed=20 + i)
            # label above the person
            draw_text_centered(draw, labels[i], ax, ay - 230, size=32, color=DIM, bold=False, hand=True)
            # diff panel below each
            box = (ax - 180, ay + 140, ax + 180, ay + 360)
            hand_rect(draw, box, fill=(255, 255, 255), outline=INK, width=3, seed=90 + i)
            # PR header bar
            hand_rect(draw, (ax - 180, ay + 140, ax + 180, ay + 180), fill=(235, 240, 250), outline=INK, width=3, seed=200 + i)
            f2 = font(22, bold=True)
            draw.text((ax - 165, ay + 148), f"PR #{i + 5}", fill=BLUE, font=f2)
            # diff lines
            f = font(26, bold=False)
            diff_sets = [
                ["- lobbyist text", "+ a typo fix", "+ clearer line", "+ a citation"],
                ["- buried clause", "+ plain English", "+ a better word", "+ a question"],
                ["- vague law", "+ a real fix", "+ a test case", "+ an example"],
            ]
            for j, ln in enumerate(diff_sets[i]):
                color = RED if ln.startswith("-") else GREEN
                draw.text((ax - 165, ay + 195 + j * 40), ln, fill=color, font=f)

    else:
        # Merged
        sub_t = local_t - 9.0
        anim = ease_in_out(clamp01(sub_t / 1.5))
        # central PR converging
        cx, cy = W // 2, H // 2 + 40
        # Discussion panel
        box = (cx - 350, cy - 150, cx + 350, cy + 180)
        hand_rect(draw, box, fill=(255, 255, 255), outline=INK, width=4, seed=120)
        f = font(28, bold=False)
        # speech bubble icon + comments
        bx = cx - 320
        by = cy - 125
        draw.ellipse([bx, by, bx + 28, by + 22], outline=INK, width=3)
        draw.polygon([(bx + 6, by + 18), (bx + 4, by + 30), (bx + 14, by + 22)], fill=PAPER, outline=INK)
        draw.text((bx + 44, by - 4), "12 comments", fill=INK, font=f)
        # reactions row — drawn icons
        ry = cy - 80
        # thumbs up
        draw.rectangle([bx + 4, ry + 10, bx + 18, ry + 28], outline=INK, width=2)
        draw.line([(bx + 10, ry + 10), (bx + 10, ry + 2)], fill=INK, width=2)
        draw.line([(bx + 10, ry + 2), (bx + 18, ry + 6)], fill=INK, width=2)
        draw.text((bx + 30, ry - 4), "47", fill=INK, font=f)
        # heart
        hx = bx + 110
        draw.ellipse([hx, ry + 4, hx + 10, ry + 14], fill=RED, outline=INK)
        draw.ellipse([hx + 8, ry + 4, hx + 18, ry + 14], fill=RED, outline=INK)
        draw.polygon([(hx, ry + 11), (hx + 9, ry + 26), (hx + 18, ry + 11)], fill=RED, outline=INK)
        draw.text((hx + 30, ry - 4), "23", fill=INK, font=f)
        # star
        sx = bx + 220
        sy = ry + 14
        star_pts = []
        import math as _m
        for k in range(10):
            ang = -_m.pi/2 + k * _m.pi/5
            r = 12 if k % 2 == 0 else 5
            star_pts.append((sx + r * _m.cos(ang), sy + r * _m.sin(ang)))
        draw.polygon(star_pts, fill=YELLOW, outline=INK)
        draw.text((sx + 20, ry - 4), "8", fill=INK, font=f)
        # MERGED stamp — checkmark on left, text well clear
        if anim > 0.4:
            hand_rect(draw, (cx - 280, cy + 20, cx + 280, cy + 150),
                      fill=GREEN, outline=INK, width=5, seed=130)
            cv_x, cv_y = cx - 220, cy + 85
            draw.line([(cv_x - 22, cv_y), (cv_x, cv_y + 28)], fill=(255, 255, 255), width=11)
            draw.line([(cv_x, cv_y + 28), (cv_x + 42, cv_y - 28)], fill=(255, 255, 255), width=11)
            draw_text_centered(draw, "MERGED", cx + 60, cy + 85, size=66, color=(255, 255, 255), bold=True)

        if sub_t > 3.5:
            draw_text_centered(draw, "Every voice counts the same.",
                               W // 2, 970, size=50, color=INK, bold=True)
    return img


def scene_act3(t: float) -> Image.Image:
    """30–45s: How to support."""
    img = paper_bg(seed=int(t * 30))
    draw = ImageDraw.Draw(img)
    local_t = t - 30.0  # 0..15

    if local_t < 4.0:
        # No corporate money
        anim = ease_in_out(clamp01(local_t / 2.0))
        draw_text_centered(draw, "No corporate money.", W // 2, 220,
                           size=88, color=INK, bold=True)
        draw_text_centered(draw, "Ever.", W // 2, 340, size=110, color=RED, bold=True)
        # big briefcase being crossed out
        if local_t > 1.0:
            draw_briefcase(draw, W // 2, 720, scale=2.2)
            # red X
            if anim > 0.5:
                hand_line(draw, (W // 2 - 220, 560), (W // 2 + 220, 880), RED, 14, seed=200)
                hand_line(draw, (W // 2 + 220, 560), (W // 2 - 220, 880), RED, 14, seed=201)

    elif local_t < 9.0:
        # Three CTAs: Star, Share, Support
        sub_t = local_t - 4.0
        draw_text_centered(draw, "If you believe government should belong to the people…",
                           W // 2, 160, size=42, color=INK)
        ctas = [
            ("star", "Star the repo", BLUE),
            ("share", "Share the project", GREEN),
            ("money", "Chip in", RED),
        ]
        for i, (kind, label, color) in enumerate(ctas):
            anim = ease_in_out(clamp01((sub_t - i * 0.6) / 1.0))
            if anim <= 0:
                continue
            cx = W // 4 + i * (W // 4)
            cy = int(620 - 30 * anim)
            # circle
            r = int(140 * anim)
            d2 = ImageDraw.Draw(img, "RGBA")
            d2.ellipse([cx - r, cy - r, cx + r, cy + r],
                       fill=(color[0], color[1], color[2], 40),
                       outline=color, width=int(6 * anim))
            # drawn icon centered
            if kind == "star":
                pts = []
                rad = int(80 * anim)
                for k in range(10):
                    ang = -math.pi/2 + k * math.pi/5
                    rr = rad if k % 2 == 0 else rad * 0.45
                    pts.append((cx + rr * math.cos(ang), cy + rr * math.sin(ang)))
                draw.polygon(pts, fill=YELLOW, outline=INK)
            elif kind == "share":
                # two circles connected by lines (network share)
                rad = int(20 * anim)
                # source
                draw.ellipse([cx - 60 - rad, cy - rad, cx - 60 + rad, cy + rad], fill=GREEN, outline=INK, width=3)
                # two targets
                draw.ellipse([cx + 40 - rad, cy - 60 - rad, cx + 40 + rad, cy - 60 + rad], fill=GREEN, outline=INK, width=3)
                draw.ellipse([cx + 40 - rad, cy + 60 - rad, cx + 40 + rad, cy + 60 + rad], fill=GREEN, outline=INK, width=3)
                # connectors
                draw.line([(cx - 40, cy - 10), (cx + 20, cy - 50)], fill=INK, width=4)
                draw.line([(cx - 40, cy + 10), (cx + 20, cy + 50)], fill=INK, width=4)
            else:  # money / heart-hand
                # dollar sign in a circle
                rad = int(70 * anim)
                draw.ellipse([cx - rad, cy - rad, cx + rad, cy + rad], fill=(255, 245, 220), outline=INK, width=4)
                f2 = font(int(110 * anim), bold=True)
                draw_text_centered(draw, "$", cx, cy, size=int(110 * anim), color=GREEN)
            draw_text_centered(draw, label, cx, cy + 230, size=int(40 * anim), color=INK)

    else:
        # End card
        sub_t = local_t - 9.0
        anim = ease_in_out(clamp01(sub_t / 1.5))
        # we-the-repo title
        size_t = max(1, int(180 * anim))
        draw_text_centered(draw, "we-the-repo", W // 2, 320, size=size_t, color=INK, bold=True)
        if anim > 0.5:
            # URL in a drawn box
            url = "github.com/we-the-repo/constitution"
            f = font(56, bold=True)
            bbox = draw.textbbox((0, 0), url, font=f)
            tw = bbox[2] - bbox[0]
            box_pad = 30
            box_y = 480
            hand_rect(draw, (W // 2 - tw // 2 - box_pad, box_y - 10,
                             W // 2 + tw // 2 + box_pad, box_y + 80),
                      fill=(235, 240, 250), outline=BLUE, width=4, seed=300)
            draw_text_centered(draw, url, W // 2, box_y + 35, size=56, color=BLUE, bold=True)
        if sub_t > 2.5:
            draw_text_centered(draw, "People over politics.", W // 2, 680, size=68, color=INK, bold=True)
            draw_text_centered(draw, "Truth over power.", W // 2, 770, size=68, color=INK, bold=True)
        # commit dots filling along bottom — chain of dots like a git graph
        if sub_t > 1.0:
            n = int(60 * clamp01((sub_t - 1.0) / 4.0))
            prev = None
            for i in range(n):
                x = 100 + i * 30
                y = 950 + int(20 * math.sin(i * 0.4 + sub_t))
                if prev is not None:
                    draw.line([prev, (x, y)], fill=GREEN, width=3)
                draw.ellipse([x - 10, y - 10, x + 10, y + 10], fill=GREEN, outline=INK, width=2)
                prev = (x, y)
    return img


def render_frame(t: float) -> Image.Image:
    if t < 15:
        img = scene_act1(t)
    elif t < 30:
        img = scene_act2(t)
    else:
        img = scene_act3(t)
    # ensure correct output size
    if img.size != (W, H):
        img = img.resize((W, H), Image.LANCZOS)
    # caption_for_time is now mostly redundant — scenes have integrated text
    return img


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--fast", action="store_true", help="15fps preview, still 1080p (compositions assume 1920x1080)")
    parser.add_argument("--scrub", type=float, default=None, help="render a single frame at this t (debug)")
    args = parser.parse_args()

    global FPS
    if args.fast:
        FPS = 15

    if args.scrub is not None:
        frame = render_frame(args.scrub)
        out = OUT_DIR / f"scrub_{args.scrub:.2f}.png"
        frame.save(out)
        print(f"✓ Wrote scrub {out}")
        return

    n_frames = int(DURATION * FPS)
    print(f"Rendering {n_frames} frames @ {W}x{H} {FPS}fps → {OUT_FILE}")

    writer = imageio.get_writer(
        str(OUT_FILE),
        fps=FPS,
        codec="libx264",
        quality=8,
        macro_block_size=2,
    )
    try:
        for i in range(n_frames):
            t = i / FPS
            frame = render_frame(t)
            if frame.size != (W, H):
                frame = frame.resize((W, H), Image.LANCZOS)
            writer.append_data(np.asarray(frame))
            if i % FPS == 0:
                print(f"  t={t:5.2f}s  frame {i}/{n_frames}", flush=True)
    finally:
        writer.close()
    print(f"✓ Wrote {OUT_FILE}")


if __name__ == "__main__":
    main()
