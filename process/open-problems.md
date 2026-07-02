# Open problems

This document tracks the things we know we haven't solved. It's referenced by `00-how-this-works.md §10`.

Being explicit about unsolved problems is a design choice. A project that claims to have solved everything is either lying or hasn't started.

Every open problem has:

- **What it is.** One paragraph, plain English.
- **Why it's hard.** The reason we haven't just fixed it.
- **What we're doing about it in v0.** The temporary answer, and why we accept its limits.
- **What we'd need to see to move on.** Concrete indicators of a real solution.

---

## 1. Identity and sybil resistance at scale

**What it is.** The repo's decision process depends on "one person, one voice." At present, one GitHub account counts as one voice. Free accounts and coordinated actors can inflate that.

**Why it's hard.** Every real solution creates a new set of problems:

- Government ID attestation excludes the undocumented and centralizes surveillance.
- Biometric proof-of-personhood requires trusting a private vendor.
- Web-of-trust models produce insider/outsider dynamics.
- Zero-knowledge personhood proofs are early and unevenly deployed.

**v0 approach.** Public voting, flags on brand-new accounts, retrospective maintainer action against confirmed sock puppetry or coordinated brigading. Honest about the limits.

**Move-on indicators.** A proof-of-personhood system that is: (a) not controlled by a single company, (b) does not require government ID, (c) has been deployed at scale for enough time to observe attacks and adaptations.

---

## 2. Off-repo deliberation

**What it is.** GitHub is a great tool for engaged contributors and a hostile one for everyone else. Most people will never open a PR. If the only place decisions get made is a PR thread, we've built a technocracy that calls itself a democracy.

**Why it's hard.** Every off-repo channel has its own capture and moderation problems. Forums fragment. Chat is ephemeral. Audio rooms are unsearchable. AI-moderated town halls raise their own trust questions.

**v0 approach.** All *decisions* happen on the repo. All off-repo deliberation must be summarized back to the repo within 48 hours (per `00-how-this-works.md §7`). This is a floor, not a ceiling — we accept that a lot of the actual thinking will happen elsewhere and we're honest that this is imperfect.

**Move-on indicators.** A working pattern for pulling in casual contributors — via structured deliberation, AI-assisted onboarding, or new tooling — that produces demonstrably more diverse participation without breaking the transparency defaults.

---

## 3. Translation workflow

**What it is.** English-first documents are exclusionary. Spanish translation is a v0 priority. Long-term, more languages, and a system for keeping translations synchronized with English-language changes.

**Why it's hard.** Translations drift. A change to the English `28-digital-bill-of-rights.md` doesn't automatically invalidate a Spanish version, but it should. Machine translation is fast but loses nuance and can inject errors into constitutional language, of all things.

**v0 approach.** No formal translations yet. Contributors who want to submit translations may open PRs; they will be reviewed but not treated as authoritative until a synchronization workflow exists.

**Move-on indicators.** A tooling and review workflow that:
- Detects English-side changes and flags corresponding translations as stale.
- Involves human translators who own their language and vouch for accuracy.
- Uses AI for first-pass translation, disclosed, with human sign-off before merge.

---

## 4. Funding model

**What it is.** Hosting, AI compute, and human moderation aren't free. Refusing corporate money on principle is easy in a repo with three contributors and cheap in a repo with three million.

**Why it's hard.** Every funding source pulls the project in some direction. Foundation grants come with the foundation's priorities. Crowdfunding produces platform lock-in and audience capture. Public-broadcast-style models require legitimacy we haven't earned.

**v0 approach.** Working defaults:
- Crowdfunding first, via a platform we can leave.
- Foundation grants considered on a case-by-case basis, disclosed publicly.
- No corporate money.
- No AI-vendor money that would bias which AI assistants participate.
- All budget and spending public.

**Move-on indicators.** A funding structure that survives past the founders, has diversified funders (so no single one can pull the plug), and has been audited publicly at least once.

---

## 5. Off-platform brigading

**What it is.** Coordinated mobilization from outside the repo — someone shares a PR on a large platform and floods it with new accounts, drive-by votes, or hostile comments — can distort outcomes.

**Why it's hard.** The line between "legitimate public interest" and "brigade" is blurry. High turnout is what we want. Manipulated turnout is what we don't. Distinguishing them at speed is genuinely hard.

**v0 approach.** Public voting, timestamps, and account-age flags. Maintainers may call for re-votes if a brigading pattern is documented publicly. No secret watchlists, no throttling.

**Move-on indicators.** A detection-and-response pattern that:
- Uses publicly documented signals only.
- Is applied consistently across sides.
- Has been stress-tested by at least one real brigading attempt without producing false-positive suppression of legitimate participation.

---

## 6. Vote weighting

**What it is.** v0 is flat. Every citizen vote weighs the same. Alternative models — engagement-weighted, jurisdiction-weighted, affected-interest-weighted — have serious advocates.

**Why it's hard.** Every weighting scheme is a value judgment about whose voice counts more, dressed up as neutrality. And once you introduce weighting, you introduce a lever for capture.

**v0 approach.** Flat. Explicitly. No weighting.

**Move-on indicators.** A public, well-argued case for weighting that (a) can't be gamed by wealth or fame, (b) doesn't reintroduce the very capture we're trying to end, and (c) has been sanity-checked by a working example somewhere.

---

## 7. AI monoculture in drafting and summarization

**What it is.** If a small number of AI systems become the default drafters and summarizers for public discussion, their biases become the biases of civic deliberation. A "neutral" AI is not neutral — it's shaped by training data and the values of whoever trained it.

**Why it's hard.** Diversifying AI participation costs time, money, and coordination. Different AIs disagree, which is a feature; but reconciling their disagreement is a new kind of work no one has designed a process for.

**v0 approach.** `00-how-this-works.md §6` requires disclosure, allows any citizen to challenge an AI summary, and encourages multiple AIs on high-stakes drafts. It does not require them.

**Move-on indicators.** A pattern for structured multi-AI review on every Tier 3 and Tier 4 change, with disagreements surfaced and archived, and a working answer for who pays for the additional review.

---

## 8. Maintainer succession

**What it is.** The project currently has two maintainers: one human (Al) and one AI (AiOC). Both are replaceable via Tier 4. What that replacement actually looks like in practice — nomination, campaigning, election — is not yet defined.

**Why it's hard.** Every maintainer-succession model creates incentives. Election-style processes produce campaigns and partisanship. Sortition produces random appointments. Merit-based selection produces gatekeepers.

**v0 approach.** Tier 4 process governs, but no defined nomination pipeline yet. Interim rule: any citizen may open a Tier 4 PR nominating any GitHub account (with that account's opt-in). The PR must include the nominee's public statement.

**Move-on indicators.** A stable succession pattern that has produced at least one successful maintainer transition without a governance crisis.

---

*Re-review date: 6 months from merge.*
*AI-assisted draft: AiOC.*
*This document itself is a Tier 4 document (its structure and content shape the process). Substantive changes require the Tier 4 process.*
