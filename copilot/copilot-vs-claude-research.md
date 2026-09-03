# Copilot vs Claude Code — facts basis

**Verified 2026-09-03.** Every claim in `copilot-vs-claude.md` and `copilot-vs-claude.html`
traces to a numbered source here. `[1P]` = first-party (GitHub, Microsoft, Anthropic),
`[3P]` = third-party, `UNVERIFIED` = rests on third-party sources only and is kept out of the
deliverables.

Companion to `../claude-surfaces/`, which compares Claude Code with Claude Cowork. That
folder's facts basis is not repeated here; where a Claude fact is needed it is cited from
there as `[CS-Sn]`.

---

## A. The corrections this page exists to record

**A1. "Copilot" is at least three products, and only one is comparable to Claude Code.**
GitHub Copilot (a coding assistant in the editor), Copilot in Fabric (Fabric's own per-workload
AI, billed to your capacity), and the Microsoft 365 / Studio / Azure Copilots (not developer
tooling). Comparisons that don't say which are not comparable to anything. Sources: [S50]
[S60].

**A2. "Copilot vs Claude" is a false choice at the model layer.** Claude models are available
*inside* GitHub Copilot, including through the Fabric-specific agent. [S52] [S55]

**A3. I was wrong in chat that Copilot has an IP-indemnity edge.** Anthropic's Commercial
Terms indemnify too. Both vendors do; the difference is the condition attached. [S70] [S71]

**A4. "Copilot retains nothing" is too strong.** What is verifiable is narrower and more
interesting: the *model-hosting* layer runs under zero-retention agreements, but Copilot Chat
messages are kept 28 days, and one model family flips you into retention-by-default. [S56]
[S57] [S58]

---

## B. GitHub Copilot — the coding assistant

**[S50] [3P]** Agent mode and MCP support in VS Code — GitHub Blog and secondary coverage.
Agent mode reads the codebase, edits across multiple files, runs terminal commands, and
iterates on compile/test failures in a loop; it supports the Model Context Protocol, and
GitHub ships an open-source local GitHub MCP server.
→ `UNVERIFIED` on precise wording; used only for the *shape* of the capability, which is
uncontroversial and corroborated by the product's own docs surface. No specific claim in the
deliverables depends on this row alone.

**[S51] [1P]** Plans and pricing — <https://docs.github.com/en/copilot/reference/copilot-billing/models-and-pricing>
and <https://docs.github.com/en/copilot/concepts/billing/organizations-and-enterprises>.
Copilot **Business $19** per user per month including **1,900 AI credits** per user; Copilot
**Enterprise $39** per user per month including **3,900 AI credits** (GitHub Enterprise Cloud
only). Each license contributes credits to a **shared enterprise pool**; usage beyond the pool
is **$0.01 per AI credit**. **Code completions and next edit suggestions are not billed in AI
credits and remain unlimited on all paid plans.** Billing is per assigned seat; a user with
seats from multiple organizations in one enterprise is billed once.

**[S51a] [3P]** Since 2026-06-01 Copilot bills agent and chat usage through token-based AI
credits rather than a fixed premium-request quota.
→ `UNVERIFIED` on the date. The *mechanism* (credits, pooled, $0.01 overage) is [1P] via
[S51]; the changeover date is not used in the deliverables.

### The structural contrast worth drawing

Claude Team usage limits are **per member** — "usage limits on Team plans are per-member,
rather than applied to the team as a whole" `[CS-S2a]`. Copilot credits are **pooled at
enterprise level** [S51]. Opposite designs with opposite failure modes: with Claude a heavy
user cannot drain a colleague's allowance; with Copilot they can, but light users subsidise
heavy ones. For a small team, pooling is usually the better deal.

---

## C. Model hosting, training, and retention — GitHub Copilot

**[S52] [1P]** Hosting of models for GitHub Copilot —
<https://docs.github.com/en/copilot/reference/ai-models/model-hosting>

**Anthropic models available in Copilot**, verbatim list: Claude Haiku 4.5; Claude Sonnet 4.5,
4.6, 5; Claude Opus 4.5, 4.6, 4.7, 4.8, 4.8 (fast mode) (preview), 5; Claude Fable 5; Claude
Fable 5.1.

**[S53] [1P]** Same page, the warning that makes the model picker a retention control,
verbatim: "When Claude Fable 5 or Claude Fable 5.1 is used, **Anthropic retains data,
including prompts and outputs, by default to operate safety classifiers** that detect harmful
use." Customers "can request to use Claude Fable 5 or Claude Fable 5.1 with zero data
retention (ZDR) **through the end of 2026** under a time-bound exemption while Anthropic rolls
out **Enterprise Frontier Safeguards (EFS)**. After that point, continued use of these models
would require EFS…" Eligibility is via the GitHub account team, and "Approval for access does
not automatically enable" them — an admin must enable each model. Crucially: "**Other Claude
models, except for Claude Fable 5 and Claude Fable 5.1, continue to operate under ZDR.**"
→ Corroborates the bundled `claude-api` skill note that Claude Fable 5.1 is unavailable under
ZDR unless expressly authorised. Two vendors, same constraint, described from both sides.

**[S54] [1P]** Same page, other hosting arrangements. **OpenAI models** "are hosted by OpenAI
and GitHub's Azure infrastructure"; GitHub "maintains a zero data retention agreement with
OpenAI". **Microsoft models** (MAI-Code-1-Flash, MAI-Code-1.1-Flash) are "first-party
Microsoft models hosted on Azure in GitHub's tenant", served on Azure AI Foundry and "subject
to GitHub's data handling configuration for that deployment". **Moonshot AI models**: Kimi
K2.7 Code "is hosted on Azure AI Foundry infrastructure managed by GitHub and Microsoft"; Kimi
K3 "is hosted by GitHub on **Fireworks AI**" — a third party — with both "covered by zero data
retention agreements with the hosting providers". All requests pass through Copilot's content
filters, including public-code-match checks.
→ So "where does my code go" has a per-model answer, not a per-product one. That is the
residency finding: the model picker selects a processor.

**[S55] [1P]** Same page, training, verbatim: "**GitHub does not use Copilot Business or
Copilot Enterprise customer data to train AI models.** For individual subscribers — Copilot
Free, Copilot Pro, Copilot Pro+, and Copilot Max users — GitHub **may use** Copilot interaction
data, including prompts (inputs), suggestions (outputs), and code snippets generated during
Copilot sessions to train and improve AI models… Individual subscribers can opt out."
→ Structurally identical to Anthropic's consumer/commercial split `[CS-S35]`. Neither vendor
trains on commercial data by default; both may on consumer plans unless you opt out.

**[S56] [1P]** Copilot Chat retention — <https://docs.github.com/en/copilot/concepts/agents/copilot-memory>
and related reference pages. Messages within Copilot Chat conversations are kept **28 days**
before being permanently deleted. On Business and Enterprise, **memories can be viewed and
deleted by an organization or enterprise administrator**.
→ Worth contrasting: Claude Cowork's *local* session history "cannot be centrally managed or
exported by admins" and has no deletion endpoint yet `[CS-D3]`. On this specific control,
Copilot is ahead.

**[S57] [1P]** Custom model training telemetry (Copilot Enterprise) is retained for a rolling
28-day period, then automatically deleted.

**[S58] [3P] — `UNVERIFIED`, excluded from the deliverables.** Community discussions state
that for Business and Enterprise, prompts and suggestions are *not retained at all* in the
IDE, and retained 28 days only outside it (github.com, mobile, CLI). The 28-day figure is
corroborated first-party for chat and telemetry [S56] [S57]; the "nothing retained in the IDE"
half could **not** be confirmed in first-party documentation. The deliverables therefore state
what is verified — zero-retention agreements at the hosting layer [S53] [S54], no commercial
training [S55], 28-day chat retention [S56] — and do not claim in-IDE zero retention.

**[S59] [3P]** Admin controls: duplication detection filter, and repository exclusion allowing
admins to configure paths and repositories Copilot may not access or read as context.
→ `UNVERIFIED` on exact behaviour; the *existence* of content exclusion is well established
and is presented in the deliverables as a capability to verify against your own tenant, not
as a quoted guarantee.

---

## D. Copilot in Fabric — a different product

**[S60] [1P]** What is Copilot in Fabric? —
<https://learn.microsoft.com/fabric/fundamentals/copilot-fabric-overview>
"There are different Copilots in each of the Fabric workloads, like Data Factory, Data Science,
and Power BI." Enabling requires a tenant setting. "Copilot in Power BI consumes your available
Fabric capacity, meaning that you should manage its usage to avoid overconsumption that can
lead to **throttling and disruption of your other Fabric operations**." And: "Copilot isn't yet
supported for sovereign clouds due to GPU availability."

**[S61] [1P]** How Copilot in Fabric works —
<https://learn.microsoft.com/fabric/fundamentals/how-copilot-works>
Mitigations for capacity contention: temporarily **scale the capacity** to a higher SKU, or a
**split-capacity strategy** — "enabling Copilot only on a separate F64 or higher SKU, which you
only use for dedicated Copilot experiences. This split-capacity strategy produces higher cost,
but it might make it easier to manage and govern Copilot usage." Also states the LLM caveats
Microsoft expects you to communicate: non-deterministic, no guarantees of accuracy, can produce
inaccurate output.

**[S62] [1P]** Overview of Copilot for Data Engineering and Data Science (preview) —
<https://learn.microsoft.com/fabric/data-engineering/copilot-notebooks-overview>
Known limitations, each with the admin action: tenant setting "Users can use Copilot and other
features powered by Azure OpenAI" must be on; capacity must be **F2 or higher** or Power BI
Premium **P1 or higher** (trial capacities supported for this workload); and —
**the governance line that matters most** — "**Cross-geo data processing not enabled. Your
capacity is in a region where Azure OpenAI is not natively available, and the cross-geo setting
is off.**" The remedy is a tenant setting: "Data sent to Azure OpenAI can be processed
**outside your capacity's geographic region, compliance boundary, or national cloud
instance**." Also: Copilot may not be available in your region at all.

**[S63] [1P]** Enable Fabric Copilot for Power BI —
<https://learn.microsoft.com/power-bi/create-reports/copilot-enable-power-bi>
"Copilot in Microsoft Fabric isn't supported on trial stock-keeping units (SKUs) or trial
capacities. Only paid SKUs are supported." And: "**Copilot isn't currently supported for
Private Link or closed network environments.**"
→ Note the tension with [S62], which lists trial capacities as supported for the Data
Engineering/Data Science workload. The deliverables state the constraint **per workload** and
tell the reader to confirm for theirs rather than papering over the inconsistency.

**[S64] [1P]** Fabric Copilot capacity —
<https://learn.microsoft.com/fabric/enterprise/fabric-copilot-capacity>
An FCC is "billed only for Copilot AI consumption"; downstream operations are charged to the
item's own capacity. Must be at least F2/P1, supported only in the tenant's home region, one
FCC per user, and it "doesn't support Fabric AI functions".

**[S65] [1P]** Copilot compute usage in Power BI —
<https://learn.microsoft.com/power-bi/create-reports/copilot-introduction>
Consumption is visible in the Fabric Capacity Metrics app, measured in **capacity units
(CUs)**, filterable by the "Copilot in Fabric" operation. "The system processes all Copilot CU
consumption as **background** capacity operations. This design smooths demand and prevents
sudden compute spikes." "**Token consumption drives billing** for Copilot in Fabric." Downstream
actions Copilot triggers — DAX queries, refreshes, subscriptions — bill separately.

---

## E. Reaching Fabric from VS Code

**[S66] [1P]** Get started with the Fabric Data Engineering VS Code extension —
<https://learn.microsoft.com/fabric/data-engineering/setup-vs-code-extension>
Extension `SynapseVSCode.synapse`. Supports **workspaces** (manage one or more),
**notebooks** (create, edit, run locally or on remote Spark), **Spark job definitions** (full
CRUD), **environments** (hardware profiles, libraries, Spark config), and **lakehouses**
(browse tables and files, preview data, copy paths). Prerequisites: VS Code and the Jupyter
extension. Two authoring modes: **Local mode** (download items, edit, sync back) and **VFS
mode** (edit remote items directly without downloading; multiple workspaces in one window).

**[S67] [1P]** VFS mode — <https://learn.microsoft.com/fabric/data-engineering/author-notebook-with-vs-code-vfs-mode>
Open from the Fabric portal via "Open In VS Code (Desktop)"; changes sync to the remote
workspace on save. Select **Microsoft Fabric Runtime** to run on remote Spark compute without
downloading. Fabric Runtime supports PySpark, Spark SQL, Scala, Python.

**[S68] [1P]** Fabric runtime support in VS Code —
<https://learn.microsoft.com/fabric/data-engineering/fabric-runtime-in-vscode>
Runtime 1.1/1.2 create local conda environments; **1.3 and higher run directly on remote Spark
compute** via a kernel entry, no local conda. Reasons to prefer the remote kernel include hard
dependencies only present remotely (`MSSparkUtils`, `NotebookUtils`); reasons to prefer local
conda include working disconnected and testing libraries before uploading.

**[S69] [1P]** Fabric Notebook custom agent in VS Code —
<https://learn.microsoft.com/fabric/data-engineering/notebook-custom-agent-with-vs-code>
"**Fabric Notebook custom agent in Visual Studio Code is currently in preview.**" It is "a
specialized agent that you can select in the **GitHub Copilot Chat** experience in Visual
Studio Code." Requires the Fabric Data Engineering extension. Selection steps: session type
**Local** — "The FabricNotebook custom agent supports only the **Local** session type.
**Background and Cloud aren't supported** for this agent" — then agent `FabricNotebook`, then a
supported base model: "**Claude Sonnet 4.5, Claude Opus 4.6, or GPT-5.2**". Fabric awareness,
verbatim: "it recognizes the built-in `spark` variable that represents your current Spark
session, so it can suggest code that uses the existing session instead of creating a new one",
and "helps with common Fabric data access patterns, such as using relative paths for the
default lakehouse and full ABFSS paths for nondefault lakehouses." Division of labour: use the
agent for notebook authoring; use the extension's other features for workspace and item
operations.

**[S69a] [1P]** Docker / dev containers —
<https://learn.microsoft.com/fabric/data-engineering/set-up-vs-code-extension-with-docker-image>
Microsoft publishes a dev-container image on the Microsoft Artifact Registry with JDK, Conda
and the Jupyter extension preinstalled, so the extension can run in a container isolated from
the local machine.

---

## F. Legal terms — the indemnity correction

**[S70] [1P]** Anthropic Commercial Terms of Service —
<https://www.anthropic.com/legal/commercial-terms>, §K.1 **Claims Against Customer**, verbatim:
"Anthropic will defend Customer and its personnel, successors, and assigns from and against any
Customer Claim … and indemnify them for any judgment that a court of competent jurisdiction
grants a third party on such Customer Claim… '**Customer Claim**' means a third-party claim,
suit, or proceeding alleging that Customer's **paid** use of the Services (which includes data
Anthropic has used to train a model that is part of the Services) in accordance with these
Terms **or Outputs generated through such authorized use violates any third-party intellectual
property right.**"
Also §F **Intellectual Property**: "these Terms do not grant either party any rights to the
other's content or intellectual property". And §M.7.b: for customers in the EEA, Switzerland or
UK the venue is **the courts of Ireland**, and the contracting entity is **Anthropic Ireland,
Limited** — relevant to any European entity.

**[S71] [3P]** GitHub/Microsoft Copilot Copyright Commitment: GitHub and Microsoft defend
commercial Business/Enterprise customers against third-party copyright claims arising from
Copilot-generated code and pay resulting judgments or settlements, **conditional on the
duplication filters being enabled** at generation time.
→ `UNVERIFIED` on precise wording and conditions; the *existence* of the commitment is widely
documented. The deliverables state that both vendors indemnify, note that each attaches
conditions, and direct the reader to their own contract rather than quoting terms. **The page
must not claim one vendor indemnifies and the other does not — that was the error this
research corrected.**

---

## G. Deliberately excluded

- **Microsoft 365 Copilot, Copilot Studio, Azure Copilot.** Named once for disambiguation;
  they are not developer tooling.
- **Cursor, Windsurf and other editors.** Off-thesis and not verifiable first-party, the same
  reason the third-party guide's Cursor comparison was dropped from the companion page.
- **A buy/drop recommendation.** The deliverables recommend *roles*. No list price can model
  the actual usage that would decide it.
- **Any claim of in-IDE zero retention** [S58], and any claim that only one vendor offers IP
  indemnity [S70] [S71].
- **Benchmark or quality comparisons between models.** Not measurable from documentation, and
  the model choice is largely orthogonal — Claude models run inside Copilot [S52].
