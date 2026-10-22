# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## What this repo is

`we-the-repo/constitution` is a **content repository, not a software project**. It is a v0 draft
of a citizen-authored U.S. federal government — constitutional amendments, a manifesto, and the
governance process — written entirely in Markdown. There is no build, no test suite, no
dependencies. The "product" is the prose and the process that produces it.

The git repository root is this directory (`we-the-repo/constitution/`), one level below the
working directory `proj/`. Run `git` and `gh` commands from here.

## Hard constraints on all content

These are non-negotiable and apply to every change you make to the prose:

- **8th-grade reading level or below.** No Latin, no legalese, no nested subclauses. If a sentence
  needs a lawyer to parse, rewrite it. This is the central premise of the project, not a style preference.
- **Cite sources for factual claims.** Link to evidence. Unsupported assertions get rejected.
- **Plain-English structure.** Each amendment has three parts in this order: (1) the constitutional
  text, (2) plain-language commentary, (3) rationale. Follow that pattern for new amendments.
- **Disclose AI authorship.** Any text you materially draft or rewrite must be labeled:
  - In commits: a `Co-authored-by:` trailer naming the AI (this repo's convention; note it differs
    from any global commit-trailer instruction).
  - In PR descriptions: note which AI assisted.
  - In issue/PR comments: prefix AI-generated summaries with `[AI summary]`.

## The governance process governs your edits too

`process/00-how-this-works.md` defines tiered decision rules. Which tier a change falls under
determines how it should be proposed and merged — match your workflow to the tier:

- **Tier 1 (trivial):** typos, broken links, formatting — fast merge.
- **Tier 2 (substantive edit):** rewording, restructuring, adding citations/examples — PR with
  rationale, 5-day lazy consensus.
- **Tier 3 (structural):** new or changed amendments, new top-level docs, manifesto changes — PR,
  14-day discussion, vote.
- **Tier 4 (meta):** changes to the process doc, `CONTRIBUTING.md`, code of conduct, maintainer
  list — hardest bar, 30-day discussion, supermajority.

**AI never decides.** You may draft, summarize, translate, flag errors, and generate analysis. You
may not vote or merge substantive (Tier 3/4) changes, and you may not post on a citizen's behalf.

## Structure and current state

- `README.md` — entry point and project overview.
- `MANIFESTO.md` — the beliefs and the political argument.
- `CONTRIBUTING.md` — contribution rules + code of conduct.
- `amendments/` — currently only `00-index.md`, which lists amendments 28–33. **The individual
  amendment files (`28-…md` through `33-…md`) and the directories `digital-bill-of-rights/`,
  `new-new-deal/`, `roadmap/`, `faq/`, and `process/open-problems.md` are referenced but do not
  exist yet.** Creating them is expected, in-progress work — verify before assuming a linked file is present.
- `process/` — how the repo itself is run; this is the working prototype of the governance model.

Work in progress lives on remote branches (e.g. `amendment-30/hybrid`, `amendment-30/pure-dd`,
`amendment-30/sortition`, `research/amendment-30-prior-art`). Check `git branch -a` before drafting
an amendment that may already have competing versions in flight — counter-proposals are tracked as
separate branches/PRs, not edits to one file.

## Tone

Direct, plain, populist, anti-capture. "We the People, not We the Donors." Match the existing
voice: short declarative sentences, concrete examples, honesty about what is unsolved (see the
"open problems" and "design tensions" sections in the process doc — name limitations rather than
hiding them).
