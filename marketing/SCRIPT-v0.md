# Video v0 — Script & Storyboard

**Working title:** "How a Bill Becomes a Law (In The Repo)"
**Runtime target:** 45s (hard cap 60s)
**Format:** 1920x1080, MP4 H.264, captions burned in
**Audience:** politically literate but not technical. Working-class adults. Schoolhouse Rock energy — no condescension, but no jargon either.

---

## Three Acts (15s each)

### Act 1 — THE PROPOSAL (0:00–0:15)

**Narration:**
> "Right now, a bill becomes a law like this: a lobbyist writes it, a lawmaker signs it, and you find out when it's already done. We think there's a better way. We're drafting a new American constitution — in public, on GitHub, in plain English. Anyone can read it. Anyone can change it."

**Visual:**
- 0:00–0:04: Old-school Schoolhouse Rock bill character (rolled scroll, sad eyes) being handed from a lobbyist (briefcase $$$ ) to a politician (suit, podium). Voter (regular person) stands outside the door, locked out.
- 0:04–0:08: Hard cut. Screen wipes. Background turns into a clean grid (git commit graph aesthetic).
- 0:08–0:15: A new "bill" character appears — but instead of a scroll, it's a Markdown file with a green commit dot. Camera pulls back to show a repo structure: amendments/, process/, digital-bill-of-rights/.

### Act 2 — HOW TO CONTRIBUTE (0:15–0:30)

**Narration:**
> "Want to help write it? Fork the repo. Open a pull request. Propose an amendment, fix a typo, argue for a better idea. Every change is reviewed in public. Every voice counts the same — yours, mine, anyone's."

**Visual:**
- 0:15–0:19: A character (everyday person — could be a nurse, a teacher, a construction worker — rotate through three) walks up to the repo. Clicks "Fork."
- 0:19–0:23: Split screen — three different people, three different PRs. Diff view shows red/green lines. Plain English text visible.
- 0:23–0:30: PRs converge into a "Discussion" panel. Comments, reactions. A green "Merged" checkmark lands. Bill character (the Markdown one) levels up — gains a star/badge.

### Act 3 — HOW TO SUPPORT (0:30–0:45)

**Narration (CTA-heavy):**
> "We don't take corporate money. We never will. If you believe government should belong to the people who live under it — star the repo, share the project, or chip in at [opencollective.com/we-the-repo]. Let's refactor democracy. People over politics. Truth over power."

**Visual:**
- 0:30–0:34: Three icons appear: ⭐ Star, 🔁 Share, 💵 Support.
- 0:34–0:39: Open Collective ledger screen — transparent, every contributor named. Counter ticks up.
- 0:39–0:43: Map of the U.S. fills with little commit dots — every state contributing.
- 0:43–0:45: End card: **we-the-repo.org** / GitHub URL / "People over politics. Truth over power."

---

## Narration delivery notes (for sag/ElevenLabs)

- Voice: Warm baritone or alto. Slight rasp OK. NOT a news anchor. NOT a kid show.
- Model: `eleven_v3` (expressive) — or `eleven_multilingual_v2` (stable) if v3 sounds theatrical.
- Pace: ~155 wpm. Conversational. Slight pauses at sentence breaks.
- Emotion arc: Act 1 = slightly weary/honest. Act 2 = warming, inviting. Act 3 = resolute, not preachy.

## Captions

Burned in (silent watch on social). Yellow on black bar, bottom third. Sentence-case, not ALL CAPS.

## Color palette

- Background: Off-white #FAF7F0 (paper)
- Ink lines: Near-black #1A1A1A
- Accent red: #C8102E (sparingly — for the lobbyist/old system)
- Accent green: #2E7D32 (for commits/merges/the new system)
- Accent blue: #1565C0 (for the repo/process)

Red + blue together visible but balanced. Non-partisan signal.

## Open questions before final cut

1. Voice talent: AI narration via ElevenLabs, or you record it?
2. Is the Open Collective URL real yet? If not, the Act 3 CTA falls back to "star the repo + share."
3. End card domain: do we own `we-the-repo.org`? If not — `github.com/we-the-repo/constitution`.
