# Amendment 30 — Prior Art

_A survey of what political science has already said about direct, deliberative, and sortition-based democracy at scale. Compiled for we-the-repo to make sure we're not reinventing — and to be honest about what's actually new._

---

## TL;DR

- **Direct democracy is not a new idea.** It's one of the oldest political ideas (Athens, 5th c. BCE) and the academic literature on modernizing it is deep — going back to Robert Dahl in the 1950s and accelerating sharply since ~2000.
- **Three big modern schools** dominate: **deliberative democracy** (Habermas, Fishkin, Cohen), **sortition / lottocracy** (Van Reybrouck, Guerrero, Landemore), and **digital / liquid democracy** (Bryan Ford, Audrey Tang, Decidim/Pol.is).
- **Several real systems already run at meaningful scale**: Switzerland (cantonal direct democracy, ~180 years), Ireland's Citizens' Assembly (drove the 2018 abortion referendum), Taiwan's vTaiwan (binding consultation on national tech policy), Iceland's 2010–2013 crowdsourced constitution, Barcelona/Madrid's Decidim platform.
- **The literature converges on the same five problems**: scale, deliberation quality, low-information voting, sybil/identity, and tyranny-of-majority. Every serious proposal addresses these or it isn't taken seriously.
- **What's genuinely novel about we-the-repo** is narrow but real: using **git as the substrate** (full history, branchable forks, PRs as the deliberation primitive) and using **AI to give every citizen drafting parity with corporate legal teams**. The political theory itself is well-trodden; the implementation surface is not.

---

## 1. Theoretical models

### Pure direct democracy (referendum-based)

- **One-line def:** every binding decision goes to a vote of all citizens.
- **Canonical advocate today:** very few political theorists endorse the pure form for a nation-state — it's mostly defended at the cantonal or municipal level.
- **Key historical works:** Rousseau, _The Social Contract_ (1762); Benjamin Barber, _Strong Democracy_ (1984).
- **Modern reality check:** even Switzerland — the closest thing to working direct democracy — is a hybrid (federal parliament + regular national referenda + cantonal direct democracy). Nobody in the literature seriously argues for pure-referendum government of 330M people.

### Deliberative democracy

- **One-line def:** legitimacy comes from reasoned public deliberation, not just vote-counting.
- **Key theorists:** Jürgen Habermas (_Between Facts and Norms_, 1992); Joshua Cohen ("Deliberation and Democratic Legitimacy," 1989); James Fishkin (_Democracy and Deliberation_, 1991; _When the People Speak_, 2009).
- **Signature mechanism:** **Deliberative Polling** (Fishkin) — random sample of citizens, briefed by balanced materials, deliberates with experts and each other, then votes. Run dozens of times across 40+ countries since 1988.
- **Big proposal:** Bruce Ackerman & James Fishkin, _Deliberation Day_ (2004) — a national holiday before elections where citizens deliberate in structured small groups.
- **What they claim works:** deliberation measurably shifts opinion toward more informed positions and reduces polarization in controlled trials.

### Sortition / lottocracy

- **One-line def:** select decision-makers by random lottery from the citizenry instead of (or alongside) elections.
- **Key theorists:** Bernard Manin, _The Principles of Representative Government_ (1997) — the foundational modern history of how we lost sortition; David Van Reybrouck, _Against Elections: The Case for Democracy_ (2013) — the popular case; Alexander Guerrero, _Lottocracy: A New Kind of Democracy_ (Oxford UP, 2024) — the most fully developed contemporary theoretical model, proposing single-issue legislatures chosen by lot; Hélène Landemore, _Democratic Reason_ (2013) and _Open Democracy_ (2020) — defends "lottocratic" representation on epistemic grounds (cognitive diversity beats expertise).
- **Signature mechanism:** randomly selected citizens' assemblies with paid time, expert briefings, and binding or quasi-binding output.
- **What they claim works:** sortition eliminates campaign finance, defeats lobbying (you can't lobby a body whose members rotate out), produces deeper deliberation than elected bodies, and represents the population descriptively rather than via self-selected ambitious people.

### Liquid democracy (delegative)

- **One-line def:** every citizen can vote directly _or_ delegate their vote on specific issues to anyone they trust; delegations are revocable and transitive.
- **Key works:** Bryan Ford, "Delegative Democracy" (2002) — the canonical paper; Christian Blum & Christina Zuber, "Liquid Democracy: Potentials, Problems, and Perspectives" (_Journal of Political Philosophy_, 2016) — the best critical treatment.
- **Real-world tests:** Germany's Pirate Party used LiquidFeedback internally (2010–2015); Google's internal "Google Votes" experiment.
- **What they claim works:** scales deliberation by letting low-information voters delegate to trusted high-information ones, without locking that delegation in for years like elections do.
- **What broke:** in every real trial, delegations concentrated on a few "super-voters" — a different kind of oligarchy.

### Hybrid models

- **Landemore's "Open Democracy" (2020)** — five principles: participatory rights, deliberation, majoritarian decision, democratic representation by lot, and transparency. Explicitly multi-mechanism.
- **Carne Ross, _The Leaderless Revolution_ (2011)** — networked self-organization, less formalized.
- **Most serious contemporary proposals are hybrids** because every pure model fails on at least one of the five open problems below.

---

## 2. Real-world implementations

| Jurisdiction | Mechanism | Scale | What worked | What failed / limits |
|---|---|---|---|---|
| **Switzerland (federal + cantonal)** | Regular binding referenda; cantonal direct assemblies (Landsgemeinde) | National (~8.7M); cantons 16k–1.5M | Stable for ~175 years; high voter trust; meaningful policy outcomes | Low turnout (~45%); slow on rights for minorities (women's suffrage 1971 federally; Appenzell Innerrhoden 1990) |
| **Vermont Town Meeting** | Annual in-person town legislative assembly | Town-level (hundreds to thousands) | Functioning continuous direct democracy since 1762 | Doesn't scale past town size; declining attendance |
| **Iceland 2010–2013 constitutional process** | Crowdsourced draft via a 25-member elected council using social media | National (~330k) | Produced a draft constitution with broad public input; 2/3 approval in 2012 advisory referendum | Parliament shelved the result. Lesson: process without binding force can be ignored. |
| **Ireland Citizens' Assembly (2016–2018)** | 99 randomly selected citizens deliberate on constitutional questions | National | Recommendations led directly to the 2018 abortion referendum and 2015 same-sex marriage referendum, both of which passed | Advisory only; needed government buy-in to advance to referendum |
| **Taiwan vTaiwan + Pol.is** | Online structured consultation using Pol.is (statement-clustering), feeding into binding regulation | National (24M) | Resolved Uber/ride-share dispute, alcohol e-commerce, and other tech policy; ~26 cases through 2020 | Scope limited to "uncontroversial-once-deliberated" topics; doesn't handle deeply polarized questions well |
| **France's Convention Citoyenne pour le Climat (2019–2020)** | 150 randomly selected citizens deliberate on climate policy | National | Produced 149 proposals; some adopted | Macron promised "without filter" implementation, then filtered. Same lesson as Iceland. |
| **Decidim (Barcelona, 2016–)** | Open-source participatory platform: proposals, debate, voting, participatory budgeting | Municipal, now used by 400+ orgs/cities globally | Real budget and policy decisions; full audit trail | Participation skews toward already-engaged citizens |
| **Madrid Decide (2015–2019)** | Similar platform; binding citizen proposals if threshold met | Municipal | Several binding city decisions | Politically dismantled when administration changed |
| **Porto Alegre participatory budgeting (1989–)** | Neighborhood assemblies allocate municipal budget | City (~1.5M) | Now replicated in 1500+ cities worldwide; measurable improvements in poor neighborhoods | Effectiveness degraded when political support weakened |
| **OurSay / GovHack / Better Reykjavík** | Various municipal e-participation platforms | Municipal | Lower-stakes proof-of-concept; sustained citizen engagement | Mostly advisory |
| **Estonia e-government / i-Voting (2005–)** | Cryptographic remote voting using national ID | National (~1.3M) | First nation to run binding internet voting in general elections; ~50% of votes are online | Voting only — not deliberation. Identity model relies on state-issued ID. |

---

## 3. Open problems the literature flags

Every serious model wrestles with these. If a proposal doesn't address them, the literature dismisses it.

1. **Scale of deliberation.** You can deliberate well with 100 people. With 100 million you can't. Sortition addresses this by deliberating with a representative sample; deliberative democracy addresses it via mini-publics; pure direct democracy mostly hand-waves it. (See: Fishkin, _When the People Speak_, 2009.)

2. **Low-information voting.** Most citizens are rationally ignorant about most policy — the cost of becoming informed exceeds the marginal value of one vote. (Anthony Downs, _An Economic Theory of Democracy_, 1957; Bryan Caplan, _The Myth of the Rational Voter_, 2007.) Deliberative + sortition models try to solve this with structured briefing and time.

3. **Tyranny of the majority.** Madison's _Federalist 10_ problem, still unsolved. Most proposals layer in entrenched rights (constitutional floor, super-majority for rights changes) — exactly what tiered decision rules do.

4. **Sybil / identity.** Any digital system needs one-person-one-account. Estonia uses state ID; some proposals use proof-of-personhood (Worldcoin, BrightID, social-graph attestation). The literature here is thinner and rapidly evolving.

5. **Capture and manipulation.** Lobbying, astroturfing, foreign interference, recommendation-algorithm capture. Sortition is the strongest answer the literature offers because you can't lobby random rotating citizens; deliberative + transparency norms are second-best.

6. **Continuous vs. episodic participation.** Real life can't pause for civics. Most existing systems are episodic (annual referenda, one-off assemblies). Continuous-participation models exist in software (Decidim, Pol.is) but haven't been tested as the primary lawmaking mechanism for a large polity.

---

## 4. What's actually novel about we-the-repo

Honest assessment — most of what we're proposing has prior art. Three things might be genuinely new:

1. **Git as the constitutional substrate.** Every other system above stores law in databases or PDF. Treating the legal code itself as a versioned, branchable, forkable Markdown repo — where amendments _are_ pull requests and the merge history _is_ the legislative record — is, as far as I can find, untested at the constitutional level. Iceland used Facebook/Twitter for input; Decidim uses a proposal database; nobody has used git's primitives (branch, fork, PR, merge, blame) as the legislative primitives themselves.

2. **AI-assisted drafting as a parity tool.** The literature acknowledges that ordinary citizens can't out-draft K Street lawyers. It usually proposes paid expert drafters for citizens' assemblies (Ireland's model). We propose AI as the equalizer — every citizen gets the same legislative-drafting capability that's currently a paid corporate advantage. The political theory hasn't caught up to this technical possibility yet (Landemore 2020 gestures at it; nobody has built it).

3. **Continuous deliberation by default.** Most direct-democracy proposals are episodic — periodic referenda, one-off assemblies. A git repo is _always open_. PRs sit in queue, are debated continuously, and merge when consensus rules are met. This collapses the distinction between "ordinary politics" and "constitutional moments" that Bruce Ackerman built his career on.

What is **not** novel: direct democracy as a goal, sortition for representativeness, deliberation as a legitimacy source, tiered decision rules, digital voting, AI-assisted policy analysis. All of these have been proposed and most have been tried.

---

## 5. Recommended reading order

For Al (and any contributor), in priority order:

1. **David Van Reybrouck, _Against Elections: The Case for Democracy_ (2013).** Short, polemical, accessible. Best entry point. Argues elections are not the same thing as democracy.
2. **Hélène Landemore, _Open Democracy: Reinventing Popular Rule for the Twenty-First Century_ (Princeton UP, 2020).** The single most relevant book to what we're doing. Lays out the five-principle framework. Read this one if you read only one.
3. **James Fishkin, _When the People Speak: Deliberative Democracy and Public Consultation_ (Oxford UP, 2009).** The empirical case that deliberation works, with twenty years of evidence.
4. **Bernard Manin, _The Principles of Representative Government_ (Cambridge UP, 1997).** The history lesson. Explains how we ended up with elections rather than sortition, and what we lost.
5. **Bryan Ford, "Delegative Democracy" (2002), available at https://bford.info/deleg/deleg.pdf.** The founding paper on liquid democracy. Short, technical, foundational for Amendment 30 Model B/C territory.

---

## 6. Full source list

### Books

- Ackerman, Bruce & Fishkin, James. _Deliberation Day_. Yale UP, 2004.
- Barber, Benjamin. _Strong Democracy: Participatory Politics for a New Age_. UC Press, 1984.
- Caplan, Bryan. _The Myth of the Rational Voter_. Princeton UP, 2007.
- Dahl, Robert. _Democracy and Its Critics_. Yale UP, 1989.
- Downs, Anthony. _An Economic Theory of Democracy_. Harper, 1957.
- Fishkin, James. _Democracy and Deliberation: New Directions for Democratic Reform_. Yale UP, 1991.
- Fishkin, James. _When the People Speak: Deliberative Democracy and Public Consultation_. Oxford UP, 2009.
- Guerrero, Alexander. _Lottocracy: A New Kind of Democracy_. Oxford UP, 2024.
- Habermas, Jürgen. _Between Facts and Norms_. MIT Press, 1996 (German orig. 1992).
- Landemore, Hélène. _Democratic Reason: Politics, Collective Intelligence, and the Rule of the Many_. Princeton UP, 2013.
- Landemore, Hélène. _Open Democracy: Reinventing Popular Rule for the Twenty-First Century_. Princeton UP, 2020.
- Manin, Bernard. _The Principles of Representative Government_. Cambridge UP, 1997.
- Rousseau, Jean-Jacques. _The Social Contract_. 1762.
- Ross, Carne. _The Leaderless Revolution_. Blue Rider Press, 2011.
- Van Reybrouck, David. _Against Elections: The Case for Democracy_. Bodley Head, 2013 (English 2016).

### Papers & articles

- Cohen, Joshua. "Deliberation and Democratic Legitimacy." In _The Good Polity_, ed. Hamlin & Pettit, 1989.
- Ford, Bryan. "Delegative Democracy." 2002. https://bford.info/deleg/deleg.pdf
- Blum, Christian & Zuber, Christina I. "Liquid Democracy: Potentials, Problems, and Perspectives." _Journal of Political Philosophy_, 24(2), 2016.
- Madison, James. _Federalist 10_. 1787. (For the tyranny-of-majority problem.)

### Real-world systems / pilots

- Switzerland: https://en.wikipedia.org/wiki/Voting_in_Switzerland
- Iceland constitutional process: https://en.wikipedia.org/wiki/2012%E2%80%9313_Icelandic_constitutional_referendum
- Ireland Citizens' Assembly: https://citizensassembly.ie/ ; https://en.wikipedia.org/wiki/Citizens%27_Assembly_(Ireland)
- Taiwan vTaiwan: https://info.vtaiwan.tw/ ; case study: https://www.technologyreview.com/2018/08/21/240284/the-simple-but-ingenious-system-taiwan-uses-to-crowdsource-its-laws/
- Pol.is: https://pol.is/
- Decidim: https://decidim.org/
- Madrid Decide: https://decide.madrid.es/
- Porto Alegre participatory budgeting: https://en.wikipedia.org/wiki/Participatory_budgeting_in_Porto_Alegre
- France Convention Citoyenne pour le Climat: https://www.conventioncitoyennepourleclimat.fr/
- Estonia i-Voting: https://e-estonia.com/solutions/e-governance/i-voting/

### Background / nav

- https://en.wikipedia.org/wiki/Direct_democracy
- https://en.wikipedia.org/wiki/Sortition
- https://en.wikipedia.org/wiki/Liquid_democracy
- https://en.wikipedia.org/wiki/Deliberative_democracy
- https://en.wikipedia.org/wiki/E-democracy
- https://en.wikipedia.org/wiki/Crowdsourcing_legislation

---

_Compiled by AiOC, 2026-06-16. Pull requests welcome._
