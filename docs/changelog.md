# Changelog

## 2026-10-08 — Openness audit and formatting cleanup

- Standardized the leaderboard to `Open / Closed` only, while retaining licensing and the evidence trail in the model catalog.
- Verified published Qwen counterparts: 3.5 Flash (35B/3B), 3.5 Plus (397B/17B), 3.6 Flash (35B/3B), 3.8 Flash (125B/6B core), and 3.8 Max (2.4T/95B). Marked 3.7 Flash/Plus, 3.6 Plus and 3.7 Max Closed pending an exact public checkpoint.
- Verified DeepSeek V4 Pro and V4.1 Flash public checkpoints; corrected V4.1 Flash to 552B with mode-dependent 8B–16B activation.
- Verified published GLM-5/5.1/5.2/5.3/5.3 Flash counterparts and corrected GLM-5-family backbone numbers; GLM-5 Turbo is a separate hosted SKU and is not assumed public.
- Added attributed **unverified Elon Musk X statements** as approximate Grok 4.5/4.6/4.7 parameter information; no fabricated active count.
- Replaced float display formatting so values like `$0.300000` become `$0.30`; added tests against regressions.
- Pricing amounts and special price tiers are otherwise unchanged.

## 2026-10-08 — Initial catalog

- Imported the previously assembled multi-provider text-model API pricing snapshot.
- Added Mistral Large 4 at its **regular published** price only, without a separate temporary launch promo row.
- Added Claude Haiku 5.5 short-prompt pricing and its distinct long-prompt notes.
- Reflected Claude Sonnet 5.5 lower cache-read rate; retained Sonnet 5 as a separate record.
- Added per-model weight availability, licenses (where known), parameter disclosures and source URLs.
- Included strict validation, deterministic README generation, local price-change history, tests, and scheduled source-page checks.

Entries imported from the prior comparison have not all been independently reverified on this date; source links and per-record review flags allow stepwise correction.
