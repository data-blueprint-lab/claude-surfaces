# Copilot or Claude Code: which chair, whose pocket, and can it reach Fabric?

**Written 2026-09-03 · statuses verified 2026-09-03 · facts basis: `copilot-vs-claude-research.md`**

A plain-language comparison of GitHub Copilot and the Claude Code CLI for a team running a
Microsoft Fabric platform — including whether Copilot can reach Fabric from VS Code, and what
each one costs from which budget.

Companion to [Code, Cowork, and Fabric](../claude-surfaces/claude-code-vs-cowork.md), which
compares Claude's own two surfaces. That page asks *whose identity acts and what survives as
evidence*. This one adds the question a second vendor forces: **which pocket pays, and what
else does that pocket fund?**

Every claim traces to a dated first-party source. Several items are preview. Re-check before
you rely on them.

---

## 00 · The short answer

**"Copilot" is at least three products, and only one of them is comparable to Claude Code.**
GitHub Copilot is a coding assistant in your editor. Copilot in Fabric is Fabric's own AI,
different in each workload, billed to your Fabric capacity. The Microsoft 365 / Studio / Azure
Copilots are something else again. Any comparison that doesn't say which one is comparing
nothing.

**"Copilot vs Claude" is a false choice at the model layer.** Claude models are available
*inside* GitHub Copilot — Haiku, Sonnet and Opus across several versions, plus the Fable
frontier models. The Fabric-specific agent runs on Claude Sonnet 4.5, Claude Opus 4.6, or
GPT-5.2. You can already be using Claude *through* Copilot. What you are actually choosing is
the **harness**: where the agent sits, what it can reach, and who gets billed.

**Yes, Copilot reaches Fabric from VS Code — and for notebooks it is ahead of Claude Code.**
The Fabric Data Engineering extension browses lakehouses, runs notebooks on remote Spark, and
edits workspace items in place. On top of it sits a Fabric-aware agent inside Copilot Chat
that knows the `spark` session variable and Fabric's lakehouse path conventions. Claude Code
has no Fabric awareness; it reaches Fabric through the MCP or CLI routes described in the
companion page.

**So:** run both, with roles. Copilot in the editor for notebook authoring. Claude Code in the
terminal for anything scripted, cross-repo, or CLI-driven. The genuinely hard decision is not
Copilot-vs-Claude at all — it is **whether to enable Copilot in Fabric**, where the deciders
are cross-geo data processing and capacity throttling, not output quality.

---

## 01 · Which Copilot are we talking about?

| | **GitHub Copilot** | **Copilot in Fabric** |
|---|---|---|
| What it is | Coding assistant: completions, chat, agent mode | Fabric's own AI, separate per workload |
| Where it runs | VS Code, on your machine | Inside the Fabric service |
| Who pays | Per-user seat + pooled AI credits | **Your Fabric capacity (CUs)** |
| Comparable to Claude Code? | Yes — same job, different chair | No — different layer entirely |
| Can throttle your pipelines? | No | **Yes** |

The Microsoft 365 Copilot, Copilot Studio and Azure Copilot are named here only so the set is
complete. They are not developer tooling and they play no part below.

> **Why the naming matters more than it should.** These products share a brand and almost
> nothing else — different billing, different governance, different failure modes. When someone
> says "we already have Copilot", the useful reply is "which one, and on what capacity?"

---

## 02 · Same job, different chair

GitHub Copilot's agent mode and Claude Code have converged more than the marketing suggests.
Both read a codebase, edit across multiple files, run terminal commands, react to test
failures in a loop, and speak MCP.

What still differs:

| | **Claude Code** | **GitHub Copilot** |
|---|---|---|
| Where it lives | The terminal — also IDE and cloud sessions | The editor |
| Scriptable / headless | Yes — this is the point of it | Weaker; built around an interactive editor |
| Drives arbitrary CLIs | Yes, including `fab` | Can run commands, but the editor is the centre of gravity |
| Fabric awareness | None built in | **Yes** — a Fabric-specific agent (see §03) |
| Model choice | Claude models | Claude, OpenAI, Microsoft, and open-weight models |

> **In plain terms.** Think of it as where you sit. Claude Code sits in the terminal, so it is
> good at things that look like commands and pipelines. Copilot sits in the editor, so it is
> good at things that look like files you are already looking at. Both can now do the other's
> job badly.

The practical read: if the work is "author and debug this notebook", the editor wins. If it is
"do this across six repos, then run it on a schedule", the terminal wins.

---

## 03 · Reaching Fabric from VS Code

This is the part that surprised me, and it is a genuine point for Copilot.

### The extension

The **Fabric Data Engineering extension** (`SynapseVSCode.synapse`) brings Fabric into VS Code:

- **Workspaces** — manage one or several
- **Lakehouses** — browse tables and files, preview data, copy paths for your code
- **Notebooks** — create, edit, and run, either locally or on **remote Spark compute**
- **Spark job definitions** — full create/read/update/delete
- **Environments** — inspect hardware profiles, libraries, Spark configuration

Two ways to work:

- **Local mode** — download items, edit locally, sync changes back.
- **VFS mode** — a virtual file system. Edit remote Fabric items directly with no download,
  and open **multiple workspaces in one window**. Changes sync on save.

For runtimes 1.3 and higher there is no local conda environment; you select a **Microsoft
Fabric Runtime** kernel and the notebook runs on remote Spark. That matters when your code has
hard dependencies that only exist remotely — `MSSparkUtils` and `NotebookUtils` are the usual
examples. Local conda still earns its place for working disconnected or testing a library
before uploading it. Microsoft also publishes a dev-container image with JDK, Conda and Jupyter
preinstalled if you would rather keep all of it off your machine.

### The Fabric-aware agent

Inside **GitHub Copilot Chat** you can select a **Fabric Notebook custom agent** — currently
**in preview**. It is not a general coding agent; it knows Fabric notebook patterns:

- It recognises the built-in `spark` variable for your current session, so it writes code that
  uses the existing session instead of creating a new one.
- It knows Fabric's data-access conventions — relative paths for the default lakehouse, full
  ABFSS paths for non-default ones.

Two constraints worth knowing before you plan around it:

- **Local session type only.** Background and Cloud sessions are not supported for this agent.
- **Specific base models:** Claude Sonnet 4.5, Claude Opus 4.6, or GPT-5.2. Pick another and
  you should switch back.

Microsoft's own division of labour: use the agent for notebook authoring; use the extension's
other features for workspace and item operations.

> **Note what this means.** The Fabric-native agent in Microsoft's tooling runs on Claude
> models. If you were choosing between "Copilot" and "Claude" as if they were rival brains, the
> premise doesn't hold.

---

## 04 · Three cost models, and the third is a trap

| | How you pay | Whose budget |
|---|---|---|
| **Claude Team** | $20–25/seat standard, $100–125 premium. Usage pool is **per member** | Software subscription |
| **GitHub Copilot** | Business **$19**/user (1,900 AI credits), Enterprise **$39**/user (3,900). Credits go into a **shared enterprise pool**; overage **$0.01/credit**. Completions unbilled and unlimited | Software subscription |
| **Copilot in Fabric** | **No seat.** Consumes **capacity units** on your F2+ / P1+ Fabric capacity. Token consumption drives billing | **Your data platform's compute budget** |

Three observations that change decisions:

**Claude's pool is per person; Copilot's is pooled across the org.** Opposite designs. With
Claude, a heavy user cannot drain a colleague. With Copilot, they can — but light users
subsidise heavy ones. For a team of a dozen, pooling is usually the better deal, and it removes
the per-person upgrade decision entirely.

**Completions are free on Copilot, and that is not a small thing.** The unlimited, unbilled
part is the part developers use most. The credits only start moving when you use chat or agent
mode.

**Copilot in Fabric competes with your production workloads.** This is the one nobody costs
properly. Its consumption comes out of the same capacity your pipelines and reports run on, and
Microsoft is explicit that overconsumption "can lead to throttling and disruption of your other
Fabric operations." Their own mitigations are to scale the capacity up, or to run a
**split-capacity strategy** — Copilot isolated on a separate F64-or-higher SKU, which Microsoft
notes "produces higher cost". There is also a **Fabric Copilot Capacity**, billed only for
Copilot consumption, with downstream operations still charged to the item's own capacity.

Nothing in the Claude world can throttle your Fabric estate. That asymmetry is the biggest
operational difference on this page.

> **For the implementer.** Copilot in Fabric consumption is visible in the Fabric Capacity
> Metrics app, in capacity units, filtered to the "Copilot in Fabric" operation, with a 30-day
> item-history breakdown. Microsoft processes it as a *background* operation deliberately, to
> smooth spikes rather than let it burst. Downstream work it triggers — DAX queries, refreshes,
> subscriptions — bills separately through the normal paths. Measure it there for a cycle before
> you budget it.

---

## 05 · What is retained, and by which surface

Both vendors have surface-dependent retention, and summaries of both flatten it.

### GitHub Copilot

- **Model hosting runs under zero-retention agreements.** OpenAI models are hosted by OpenAI
  and GitHub's Azure infrastructure with a zero-retention agreement in place. Microsoft's own
  models run on Azure in GitHub's tenant. Open-weight models are covered by zero-retention
  agreements with their hosting providers — one of which is a third party, Fireworks AI.
- **Claude models in Copilot "continue to operate under ZDR"** — with one exception below.
- **Copilot Chat messages are kept 28 days**, then permanently deleted. On Business and
  Enterprise, **memories can be viewed and deleted by an org or enterprise administrator**.
- **No training on Business or Enterprise data.** On individual plans — Free, Pro, Pro+, Max —
  GitHub *may* use prompts, suggestions and code snippets to train, with an opt-out.

**The model picker is a retention control, and almost nobody treats it as one.** Per GitHub's
own docs: when Claude **Fable 5 or Fable 5.1** is used, "Anthropic retains data, including
prompts and outputs, **by default** to operate safety classifiers that detect harmful use."
There is a time-boxed zero-retention exemption available **through the end of 2026** while
Anthropic rolls out Enterprise Frontier Safeguards; after that, continued use requires EFS.
Eligibility runs through your GitHub account team, and an admin must still enable each model.
Every other Claude model in Copilot stays under zero retention.

So on Copilot, choosing a frontier model can change your retention posture — silently, from a
dropdown.

### Claude Code

From the companion page: 30 days for API inputs and outputs; saved Team and Enterprise sessions
retained **until someone deletes them**, not capped at 30 days; **five years** for anything
submitted as feedback or a bug report; no training on commercial terms unless an admin opts in.

### Where they land

| | GitHub Copilot | Claude Code |
|---|---|---|
| Training on commercial data | No | No |
| Training on consumer plans | May, with opt-out | May, with opt-out |
| Hosting-layer retention | Zero-retention agreements | 30-day default; ZDR is Enterprise-only and negotiated |
| Chat/session history | 28 days; admin can view and delete memories | Saved sessions until deleted; local Cowork sessions not admin-manageable |
| Model choice affects retention | **Yes** — Fable models retain by default | Yes — the same Fable constraint, from the other side |

On one specific control, **Copilot is ahead**: an administrator can view and delete Copilot
memories. Claude Cowork's local session history cannot be centrally managed or exported, and
has no deletion endpoint yet.

---

## 06 · Where Copilot is genuinely better

Stated plainly, because a comparison written by a Claude Code user should be suspected of bias:

- **The Fabric-native notebook agent.** Nothing on the Claude side knows what a default
  lakehouse is. For notebook work this is a real advantage, preview status notwithstanding.
- **VFS mode and the remote Spark kernel.** Editing workspace items in place and running on
  remote compute, from the editor, with no sync dance.
- **Completions are unlimited and unbilled** on every paid plan. The most-used feature costs
  nothing per use.
- **Pooled credits suit a small team.** No per-person allowance to manage, no upgrade decision
  per head.
- **Admin-managed memory.** Viewable and deletable by an administrator — a control Claude's
  local Cowork sessions lack.
- **Content exclusion.** Administrators can define paths and repositories Copilot may not read
  as context. Worth verifying against your own tenant rather than taking from a summary.
- **Model breadth.** Claude, OpenAI, Microsoft and open-weight models behind one seat, with
  per-model hosting disclosed.

### And the indemnity claim I had wrong

I initially said Copilot had an IP-indemnity edge. **It does not.** Anthropic's Commercial
Terms §K.1 commit Anthropic to defend the customer and indemnify judgments on third-party
claims that paid use of the Services "or Outputs generated through such authorized use violates
any third-party intellectual property right." GitHub and Microsoft make a comparable
commitment for Business and Enterprise.

**Both vendors indemnify.** Each attaches conditions — GitHub's is generally tied to having
duplication filters enabled; Anthropic's to use being in accordance with the Terms. Read your
own contract; do not take either from a comparison table, including this one.

One detail for a European entity: Anthropic contracts through **Anthropic Ireland, Limited**
for customers in the EEA, Switzerland and the UK, with venue in the **courts of Ireland**.

---

## 07 · Where Copilot in Fabric is worse

These are about Copilot **in Fabric**, not GitHub Copilot. They are the reason this is a
decision rather than a default.

- **Cross-geo processing.** If your capacity sits in a region where Azure OpenAI is not natively
  available, Copilot does not work until an admin enables a tenant setting whose own description
  is that data "can be processed **outside your capacity's geographic region, compliance
  boundary, or national cloud instance**." If data residency is part of your architecture, this
  is the line that decides it.
- **No Private Link or closed-network support.**
- **Not available in sovereign clouds**, on GPU-availability grounds.
- **Paid capacity required** — F2+ or P1+ — plus a tenant-level admin toggle. Trial-capacity
  support differs by workload: the Data Engineering and Data Science docs list trial capacities
  as supported, while the Power BI docs say trial SKUs are not. Confirm for the workload you
  actually intend to use rather than trusting either statement generally.
- **Region availability limits** independent of everything above.
- **It can throttle production**, per §04.

> **The honest summary.** GitHub Copilot's governance story is good and in places better than
> Claude's. Copilot in Fabric's is the weakest of the three surfaces on this page — not because
> Microsoft built it badly, but because it runs inside a shared capacity and may route data
> outside your compliance boundary to work at all.

---

## 08 · What I'd run — and the case against it

**Run both, with roles.**

- **GitHub Copilot in VS Code** for notebook and in-editor work. The Fabric extension plus the
  Fabric-aware agent is the best notebook-authoring setup available for a Fabric team today.
  Copilot Business at $19/user with pooled credits and free completions is good value for a
  team of a dozen.
- **Claude Code in the terminal** for everything scripted, cross-repo, CLI-driven or
  unattended — including the `fab` route into Fabric from the companion page.
- **Copilot in Fabric: decide deliberately, and probably not yet.** If you need the cross-geo
  setting enabled to make it work at all, that is a data-residency decision, not a tooling one,
  and it belongs with whoever owns your compliance posture. If you do enable it, isolate it —
  a Fabric Copilot Capacity or a split capacity — so it cannot throttle your pipelines.

Whichever you run, the rule from the companion page still holds and is not vendor-specific:
**don't point any of them at production data**, and keep a named human in the audit log rather
than a shared service principal.

### The case against all of that

**Running both is how tool sprawl gets justified.** Two agent subscriptions is $39–120 per
person per month for heavily overlapping capability, plus two sets of permissions, two audit
trails, two vendors to keep current, and a team that has to remember which tool to reach for.
"Use the right tool for the job" is the argument every organisation makes on the way to paying
for five things that each do 80% of the same work. A single tool used well usually beats two
used casually.

**And my Fabric caution may be miscalibrated.** I am recommending against Copilot in Fabric
largely on cross-geo processing — but if your capacity is in a region where Azure OpenAI *is*
natively available, that setting never comes up and the objection evaporates. I have not
checked which regions those are for your tenant, so treat my caution as a question to answer,
not a conclusion to adopt.

**If forced to pick one for a twelve-person Fabric team, I'd pick GitHub Copilot** — not
because it is the better agent, but because the Fabric-native integration, the free
completions and the pooled credits fit that team's actual shape, and notebook work is the bulk
of the job. I'd expect to miss Claude Code's terminal within a month.

---

## Notes

**Facts basis.** Every claim traces to a numbered, dated source in
`copilot-vs-claude-research.md`. Prices are US list, excluding tax, and subject to change.

**Corrections recorded in this document.** Two of my own claims were wrong before verification:
that Copilot held an IP-indemnity advantage (both vendors indemnify), and that Copilot "retains
nothing" (the hosting layer runs under zero-retention agreements, but chat is kept 28 days, and
Fable models retain by default). One claim — that nothing at all is retained in-IDE — could not
be confirmed first-party and is deliberately absent.

**Shelf life.** Verified 2026-09-03. The Fabric Notebook custom agent is in preview. The
zero-retention exemption for Fable models is explicitly time-boxed to the end of 2026. Copilot
pricing and credit allowances have changed at least once in 2026. Re-check any status claim.

**Companion.** [Code, Cowork, and Fabric](../claude-surfaces/claude-code-vs-cowork.md) —
Claude Code vs Claude Cowork on cost, retention and governance, plus the MCP-vs-CLI routes into
Fabric.

**The organisation is invented.** No real organisation, person, workspace or object name
appears anywhere in this document.
