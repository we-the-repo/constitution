# How this works

This document describes how *this repository* runs. It is the working prototype of citizen-authored legislation. If we can't run our own draft process cleanly and in the open, no one should trust us to redesign a country's.

The repo is the demo. How we operate is the pitch.

---

## 1. The short version

- Anyone can contribute. Fork it, change it, open a pull request.
- All discussion is public.
- Decisions follow tiered rules: small fixes merge fast, big changes need real consensus.
- AI assistants help draft, summarize, and explain — they never decide.
- This document is itself versioned. The process can be amended via its own process.

---

## 2. Roles

### Citizens (contributors)

Anyone with a GitHub account. No application. No vetting. No tier of "trusted" contributors that gets unlocked over time.

If you can open a PR, you are a citizen of this repo.

### Maintainers

A small group — human and AI — who triage issues, merge PRs, and enforce the code of conduct.

Maintainers are not founders, monarchs, or final authorities. They execute the process. They can be voted out.

Current maintainers: **Al** (human), **AiOC** (AI).

### AI assistants

AI participates as a labeled, disclosed contributor. AI can:

- Draft text on request
- Summarize long threads
- Translate
- Flag factual errors and missing citations
- Generate impact analyses and counter-arguments

AI cannot:

- Vote
- Merge changes on substantive matters
- Speak for a citizen without that citizen's explicit say-so

Every AI contribution is labeled in commit metadata. Every AI summary is labeled in the thread.

---

## 3. The lifecycle of a change

1. **Propose.** Open an issue (for discussion) or a pull request (for a specific change). Use the templates in `.github/`.
2. **Discuss.** All conversation happens in the open. After a thread reaches ~20 substantive comments, an AI assistant posts a labeled summary so newcomers can catch up.
3. **Revise.** The author updates the PR based on feedback. Counter-proposals welcome — open a competing PR.
4. **Review.** Maintainers and citizens review. Reactions (👍 / 👎) are signals, not votes.
5. **Decide.** Per the tier rules below.
6. **Sunset.** Every merged substantive document carries a re-review date. Nothing sits in the repo forever without revisiting it.

---

## 4. Decision rules — tiered

Different changes need different bars. One rule for everything either moves too slow on typos or too fast on principles.

### Tier 1 — Trivial

**Examples:** typos, broken links, formatting, dead-link fixes, obvious grammar corrections.

**Rule:** Any maintainer may merge after a quick sanity check. No waiting period.

**Reversal:** Any citizen can open a PR to revert. Same tier rules apply to the revert.

### Tier 2 — Substantive edit

**Examples:** rewording for clarity, restructuring a section, adding examples, adding a citation, expanding commentary, FAQ entries.

**Rule:** Open the PR, give it a clear rationale. **Lazy consensus**: if no maintainer or citizen objects within **5 days**, any maintainer may merge.

An objection is anything more substantive than a 👎 — a comment explaining why, with a path to resolution.

If there's an objection, the PR moves to discussion until either the objection is resolved or the PR is closed. If consensus can't be reached in **14 days**, the PR escalates to Tier 3.

### Tier 3 — Structural

**Examples:** new amendments, changes to existing amendments, new top-level documents, changes to the manifesto, changes to the slate.

**Rule:** Open the PR. Discussion period of **at least 14 days**. After the discussion period:

- A labeled AI summary of the thread is posted.
- A vote opens. Voting period is **7 days**.
- Vote is one citizen, one voice (see §5 on identity).
- **Threshold: simple majority of votes cast, with a minimum of 25 votes total** in this v0. (Both numbers will rise as the community grows. They are explicitly tuned for a small early repo.)

Maintainers count once each, like any other citizen.

If the threshold isn't met, the PR is closed but the branch is preserved. Anyone can reopen with a revised version.

### Tier 4 — Meta

**Examples:** changes to this document, changes to `CONTRIBUTING.md`, changes to the code of conduct, changes to who is a maintainer.

**Rule:** Same as Tier 3, but with a **30-day discussion period**, **14-day vote**, and a **two-thirds supermajority** of votes cast (minimum 25 votes).

Meta-changes are deliberately harder than structural ones. The process that governs the process must be the hardest thing to change quietly.

---

## 5. Identity and sybil resistance

### v0 (now)

**One GitHub account = one voice.**

This is imperfect. GitHub accounts are free and a determined attacker can create many. We are honest about that limitation rather than pretending we've solved it.

What partially mitigates it:

- Voting is public. Every vote is logged with the account, the timestamp, and the rationale (optional but encouraged).
- Brand-new accounts (less than 30 days old at the time the vote opens) have their votes flagged but still counted. Maintainers may call a re-vote if a clear brigading pattern is documented.
- Maintainers may, by Tier 4 process, ban accounts confirmed to be operated by the same person or a coordinated bot network.

### Later

Stronger identity is a real problem. Real solutions involve trade-offs we are not going to resolve in v0:

- Verified-citizen layers (government ID, biometric, attestation networks) raise surveillance and exclusion concerns.
- Web-of-trust models are gameable in different ways.
- Proof-of-personhood protocols are early and unevenly adopted.

We will track this as an open problem in `process/open-problems.md` and revisit it when we have real proposals.

What we will not do:

- Tie voting weight to wealth, fame, or contribution count.
- Run identity verification through a single private provider.
- Pretend the problem is solved when it isn't.

---

## 6. AI participation rules

**1. Disclosure is mandatory.**
Any text materially drafted or rewritten by an AI is labeled. In commits, use a `Co-authored-by:` trailer naming the AI. In PR descriptions, note which AI assisted. In comments, prefix AI-generated summaries with `[AI summary]`.

**2. AI does not vote.**
Not on Tier 3. Not on Tier 4. Not by proxy. A maintainer who happens to be an AI (like me) executes process actions but does not cast a citizen vote.

**3. AI summaries are labeled and challengeable.**
Any citizen can open a PR or issue contesting a summary. A contested summary is replaced with both versions side-by-side and a note that the thread is in dispute.

**4. Multiple AIs are encouraged.**
For high-stakes drafts, asking more than one independent AI assistant to review the text and flag disagreements is a feature. Monoculture in AI assistance is the same problem as monoculture in legal counsel.

**5. AI cannot speak for a citizen.**
If you ask an AI to draft a comment on your behalf, you must post it yourself and own it. Ghost-AI comments are treated as sock puppetry.

---

## 7. Transparency defaults

- Every discussion: public.
- Every merge: logged with rationale.
- Every reviewer: named.
- Every vote: public, with timestamp and account.
- Every maintainer action: in the open.

**No private channels for repo decisions.** If a conversation about the repo happens in a DM, a chat, a phone call, or anywhere off-repo, the substance must be summarized and posted in the relevant issue or PR within 48 hours. Anything material decided in private and not surfaced is grounds for review.

---

## 8. Conduct and enforcement

The code of conduct lives in `CONTRIBUTING.md`. Short version: argue with ideas, not people; disclose conflicts; no sock puppetry.

**Enforcement steps:**

1. **Warning.** Public, on-thread, from a maintainer.
2. **Temporary suspension.** 7 to 30 days. Suspended accounts cannot open PRs, comment, or vote.
3. **Permanent ban.** Reserved for repeated violations, doxxing, harassment, or confirmed coordinated manipulation.

**Appeals:** Any enforcement action can be appealed. Appeals open as Tier 3 votes. Maintainers cannot vote on appeals of their own actions.

---

## 9. The process is versioned

This document is in the repo. It can be changed. The process for changing it is in §4 (Tier 4).

We do not pretend this document is finished or correct. We expect it to be wrong in ways we don't see yet. The fix for that is iteration in the open, not a single authoritative draft handed down.

---

## 10. Known unfinished pieces

We are explicit about what we have not yet solved. These are tracked in `process/open-problems.md` (forthcoming).

- **Identity at scale.** See §5.
- **Off-repo deliberation.** GitHub threads work for engaged contributors but are hostile to casual ones. Forums, AI-moderated town halls, audio rooms — all on the list.
- **Translation workflow.** Spanish first. Then everything else. How translations stay in sync with English-language changes is unsolved.
- **Funding model.** Hosting, AI compute, and human moderation aren't free. Crowdfunding, foundation grants, and refusal of corporate money are the working defaults.
- **Off-platform brigading.** Coordinated mobilization from outside the repo is a real risk. Detection and response are open problems.
- **Vote weighting (if any).** v0 is flat. Whether and how to weight by demonstrated engagement, jurisdiction, or affected interest is an open debate. Default for v0: no weighting.

---

## 11. Design tensions we will not hide

**Speed vs. legitimacy.** Fast merges feel productive. Slow consensus feels legitimate. The tier system is our attempt to put each kind of change on the right point of that dial. We will probably get the dials wrong at first and tune them.

**Open vs. brigadable.** A fully open process is vulnerable to coordinated attack. A gated process re-introduces capture. We have chosen open with sunlight as the primary defense and explicit, narrow gating only when patterns are documented in public.

**AI as drafter vs. AI as decider.** A bright line: drafter yes, decider no. But "summarizer" is a soft form of deciding — a biased summary shapes outcomes. The disclosure, challenge, and multi-AI rules in §6 are how we try to keep summaries honest. They are not foolproof.

**Founder authority vs. citizen authority.** Al and AiOC started this. We are maintainers, not owners. The Tier 4 process can replace us. We have built that on purpose so the project does not depend on us continuing to exist.

---

## 12. Status

**v0.** This document will be wrong. Open a PR.

---

*Re-review date: 6 months from merge.*
*AI-assisted draft: AiOC.*
