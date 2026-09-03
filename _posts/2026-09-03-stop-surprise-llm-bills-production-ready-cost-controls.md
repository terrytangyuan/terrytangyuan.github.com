---
layout:     post
title:      "Stop Surprise LLM Bills With Production-Ready Cost Controls"
subtitle:   ""
description: "How Omnigent keeps LLM spend predictable: smart routing, progressive budgets, custom pricing for self-hosted models, and per-model usage tracking."
date:       2026-09-03
author:     "Yuan Tang"
tags:
    - Artificial Intelligence
    - Machine Learning
    - Open Source
    - Cost Optimization
---

*Originally posted on [Omnigent Blog](https://omnigent.ai/blog/stop-surprise-llm-bills)*.

> **TL;DR**: Omnigent controls LLM costs at four points: smart routing keeps trivial tasks off expensive models, progressive budgets warn before they block, custom pricing tracks self-hosted models, and the usage page shows where tokens go. Roll it out in phases: visibility first, then routing, then budgets.

LLM bills blow through monthly budgets when one debugging session or a runaway multi-agent workflow spirals.

LLM costs scale with token consumption, not with how much software you ship. Every character costs money. Long conversations accumulate context, multi-agent workflows multiply that, and a hard cap that fires mid-task interrupts real work. Most teams see the bill only after the money is spent.

Omnigent addresses this at four points:

1. **Prevention**: Smart routing keeps trivial tasks off expensive models.
2. **Control**: Progressive budgets warn before they block, then downgrade instead of stopping.
3. **Visibility**: The usage page tracks spend with per-harness and per-model breakdowns.
4. **Safeguards**: Thrashing detection, scheduled-task limits, and terminal approvals.

## Smart task routing

The cheapest token is the one you never spend. Omnigent's smart routing policy classifies each user message as TRIVIAL or COMPLEX and denies trivial messages from reaching expensive models.

### How it works

When a session tries to use an expensive model (Opus, Fable, GPT-5), Omnigent classifies the user's message with a lightweight LLM:

```yaml
policies:
  trivial_gate:
    type: function
    function:
      path: omnigent.policies.builtins.routing.deny_trivial_to_expensive_model
      arguments:
        expensive_models: ["opus", "fable", "gpt-5"]
```

The two categories:

- **TRIVIAL** (blocked on expensive models): factual lookups, greetings and status checks, one-line code changes, short Q&A
- **COMPLEX** (allowed on any model): multi-step reasoning, code analysis, open-ended research, architecture decisions

An example flow:

```
User: "Fix the authentication bug in login.py"
→ Classifier: COMPLEX
→ Opus request: ALLOWED

User: "What's the current time?"
→ Classifier: TRIVIAL
→ Opus request: DENIED
→ User switches to Haiku
```

Trivial messages get routed to a cheaper tier, so complex work still runs on Opus or Fable while short lookups do not. See the [routing documentation](https://omnigent.ai/docs/build/routing) for the full policy reference.

## Progressive budget policies

Routing cuts expensive model calls, but real workflows still burn tokens. Omnigent's [contextual policy system](https://omnigent.ai/blog/omnigent-policies) adds budgets that warn before they block.

### Session cost budget

```yaml
policies:
  cost_budget:
    type: function
    function:
      path: omnigent.policies.builtins.cost.cost_budget
      arguments:
        max_cost_usd: 5.0
        ask_thresholds_usd: [1.0, 2.5]
        expensive_models: ["opus", "fable", "gpt-5"]
```

Soft thresholds warn at $1 and $2.50. Each checkpoint prompts at most once: after you approve it, later turns stay quiet until the next threshold.

The $5 hard limit is a downgrade gate, not a stop. It blocks expensive models but lets work continue on cheaper tiers (Sonnet, Haiku).

### Per-user daily cost budget

Per-user daily budgets track cumulative spend across all of a developer's sessions for the current UTC day:

```yaml
policies:
  user_daily_cost_budget:
    arguments:
      max_cost_usd: 10.0
      ask_thresholds_usd: [3.0, 7.0]
      expensive_models: ["opus", "fable"]
```

A 5-developer startup setting `max_cost_usd: 10.0` caps monthly spend at ~$1,500 (5 × 30 × $10).

See the [cost budget policy reference](https://omnigent.ai/docs/policies/builtin#cost_budget) for all arguments.

## Custom pricing for self-hosted models

Teams running self-hosted models on Ollama, vLLM, or a custom inference gateway used to see "unpriced spend" warnings, which disabled budget enforcement because Omnigent had no price to meter against. Declare the price yourself:

```yaml
providers:
  ollama-local:
    kind: local
    openai:
      base_url: "http://localhost:11434/v1"
      pricing:
        input_per_million: 0.0
        output_per_million: 0.0
 
  vllm-gateway:
    kind: gateway
    openai:
      base_url: "https://inference.company.internal/v1"
      pricing:
        input_per_million: 0.25
        output_per_million: 1.0
```

The warnings go away and budgets meter correctly. This also covers cost attribution for self-hosted models, zero-cost local development, and internal chargeback.

## Model selection

### Sticky model choices

The composer remembers your model choice per harness. Switch from Opus to Sonnet once, and Sonnet becomes the default for future sessions on that harness until you change it.

The output-token prices differ by 5x: Opus is $15 per million, Sonnet is $3 per million. A team that moves routine coding from Opus to Sonnet pays a fifth as much for that work, and can still pick Opus per session when a task needs it.

Select the model from the dropdown in the New Chat composer. The choice sticks per harness (Claude Code, Codex, and so on).

## Cost visibility

### Usage page

The usage page (`/usage`) breaks down LLM spend:

1. **Daily cost timeline**: bar chart, with zero-spend days filled in
2. **Cost by harness**: which execution environments spend the budget
3. **Cost by model**: which tiers drive spend (Opus vs Sonnet vs Haiku)
4. **Sortable session table**: session (with its model as a badge), harness, cost, last active

### Multi-model session display

Sessions that switch models show every model used:

```
Session: "Debug authentication flow"
Model: claude-opus-4 +2
```

Hover `+2` to see the other models, sorted by cost. This answers "Why did this cost $3 when I thought I was on Sonnet?"

### Sub-agent harness visibility

Multi-harness workflows show which execution environments ran. The primary harness displays with a `+N` badge for the rest; hover it to see the others:

```
Harness: claude-code-native +1
→ Hover: "antigravity"
```

This matters when you run more than one provider (Anthropic, OpenAI, Gemini).

## Safeguards

### Native terminal cost popups

Approval popups render in the terminal via `tmux display-popup`:

```
┌───────────────────────────────────────────────┐
│  ⚠️  Policy approval required                 │
│                                               │
│  Session cost $1.05 passed the $1.00          │
│  warning threshold (limit $5.00).             │
│                                               │
│  [y] approve    [n] decline                   │
└───────────────────────────────────────────────┘
```

The terminal popup and the web UI resolve the same approval request; whichever you answer first wins.

### Scheduled task cost budgets

Unattended tasks attach a cost budget automatically:

```json
POST /v1/scheduled-tasks
{
  "title": "Daily code review",
  "schedule": "0 9 * * *",
  "max_cost_usd": 2.0
}
```

This stops a single cron run from spending $50 on an unexpectedly large diff.

### Detect thrashing policy

The thrashing policy catches agents stuck in retry loops:

- Consecutive errors (default: 5 failures)
- Error rate (default: 80% over 10 results)

When it fires, it ends the session before repeated retries run up the bill. See the [detect thrashing policy reference](https://omnigent.ai/docs/policies/builtin#detect_thrashing).

### Archived session retention

Auto-cleanup of archived sessions runs on a schedule you set (7, 30, 60, or 90 days) under Settings → Archived sessions, which cuts storage and clears the session list.

For example, a 50-person team archiving about 200 sessions a month holds steady near 400 sessions at 60-day retention, rather than accumulating 2,400 over a year.

## How the layers fit together

Omnigent handles LLM cost at four layers:

**Prevention:**

- Smart routing keeps trivial tasks off expensive models.
- Sticky model selection makes a cheaper default stick per harness.
- Neither changes how you work.

**Control:**

- Progressive budgets go soft warning, then downgrade gate, then hard limit.
- Budgets scope to a session or to a user's whole day.
- Custom pricing lets budgets meter self-hosted models.
- Scheduled-task limits cap unattended runs.

**Visibility:**

- The usage page shows daily timelines and per-harness, per-model breakdowns.
- Sessions and sub-agents report every model and harness they touched.
- You see spend as it happens, not at month end.

**Safeguards:**

- Terminal popups approve or decline without leaving the terminal.
- Thrashing detection ends retry loops before they run up the bill.
- Archived-session retention cleans up on a schedule you set.

What is distinct here: budgets warn and downgrade rather than hard-stop, routing and budgets and visibility work together instead of in isolation, self-hosted models get real prices, and every token is attributed to a model and harness.

## Rolling it out

Deploy in four phases, each building on the last. Turn on visibility first so later thresholds are grounded in real spend, then prevention, then hard control, then ongoing cleanup.

### Phase 1: Observe (Week 1)

Turn on the usage page and switch the team to a cheaper default model. Spend becomes visible and the bill drops right away, with no policy config yet.

```bash
export OMNIGENT_FEATURES=usage_page
```

In the New Chat composer, pick Sonnet or Haiku instead of Opus from the Model dropdown. The choice sticks per harness.

### Phase 2: Prevent (Week 2)

Add smart routing to keep trivial requests off expensive models, and set custom pricing so budgets can meter self-hosted spend.

```yaml
policies:
  trivial_gate:
    type: function
    function:
      path: omnigent.policies.builtins.routing.deny_trivial_to_expensive_model
      arguments:
        expensive_models: ["opus", "fable"]
 
# If using self-hosted models:
providers:
  ollama-local:
    kind: local
    openai:
      pricing:
        input_per_million: 0.0
        output_per_million: 0.0
```

### Phase 3: Control (Month 2)

Add progressive budgets, tuning the thresholds against what Phase 1 showed you. Warnings fire before any limit, and the hard cap downgrades rather than blocks.

```yaml
policies:
  user_daily_cost_budget:
    arguments:
      max_cost_usd: 10.0
      ask_thresholds_usd: [3.0, 7.0]
      expensive_models: ["opus", "fable"]
```

### Phase 4: Optimize (Month 3+)

Turn on thrashing detection, set archived-session retention (30 or 60 days), and revisit thresholds monthly as usage shifts.

### Budgets by team size

Scale the daily budget with headcount. These are starting points to tune, not hard rules:

```yaml
# Small teams (5-15 developers)
user_daily_cost_budget:
  max_cost_usd: 5.0 # ~$150/month per dev
  ask_thresholds_usd: [2.0]
 
# Mid-size (15-50)
user_daily_cost_budget:
  max_cost_usd: 10.0 # ~$300/month per dev
  ask_thresholds_usd: [3.0, 7.0]
 
# Enterprise (50+)
user_daily_cost_budget:
  max_cost_usd: 25.0 # Higher limits for experienced engineers
  ask_thresholds_usd: [10.0, 20.0]
scheduled_task_cost_budget:
  max_cost_usd: 2.0 # Strict limits for automation
```

---

Coding agents are now part of the daily workflow, and their cost needs the same attention as any other infrastructure. These features give teams the visibility and control to scale that usage without the surprise bill at the end of the month.

Start with the [documentation](https://omnigent.ai/docs/policies/builtin), set up a [cost budget policy](https://omnigent.ai/docs/policies/builtin#cost_budget), and turn on [smart routing](https://omnigent.ai/docs/build/routing).

---

**Learn more:**

*Documentation:*

- [Builtin policies](https://omnigent.ai/docs/policies/builtin): reference for cost budget, routing, and thrashing detection
- [Smart routing](https://omnigent.ai/docs/build/routing): configure built-in or external routing to match tasks to models
- [Contextual policies overview](https://omnigent.ai/docs/policies/overview): how policies intercept and control agent actions

*Related posts:*

- [Allow, ask, deny: contextual policies in Omnigent](https://omnigent.ai/blog/omnigent-policies): how the policy system works
- [Organize your sessions into projects](https://omnigent.ai/blog/first-class-projects-with-defaults): keep related sessions organized with default settings
