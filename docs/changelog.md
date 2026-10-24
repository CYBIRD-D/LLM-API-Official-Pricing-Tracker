# Changelog

## 2026-10-24 — Kimi K3.1 Pro and MiniMax M3.1 Flash

- Added **Kimi K3.1 Pro** and **Kimi K3.1 Pro Highspeed** ($2/$0.20/$10 and $4/$0.20/$20 input/cache read/output per million tokens). The Highspeed API uses the same model at 2–3× speed.
- Both Kimi K3.1 variants remain **Closed as of October 24**: Moonshot promises publicly downloadable weights by November 4, 2026; an upcoming release does not qualify as Open.
- K3.1 model scale is **2.8T total / 104B active** (MoE) with a 1M-token context, according to Moonshot's announcement.
- Added **MiniMax M3.1 Flash**, **Open**, with official downloadable weights available, 428B total / 23B active (MoE), and the MiniMax Community License.
- MiniMax M3.1 Flash official API rates are $0.15 input, $0.015 cached input, $0.60 output per million tokens. A temporary zero-price launch window through October 22 has expired and is not listed as the current rate.
- Added 3 new pricing records and preserved existing model prices and labels unchanged. Updated source watch, pricing history and test coverage.

## 2026-10-18 — Muse Spark Open, DeepSeek Flash 1017 and rate-label formatting

- Added **Muse Spark Open** as a separate **Open** model (816B total / 42B active, Muse Model License), released October 15. Its OpenRouter API is $1.25 input, $0.15 cache read and $4.25 output per 1M tokens.
- **Muse Spark 1.2 and hosted 1.3 remain Closed**: Meta says Spark Open shares the **base** with 1.3 but includes additional safety post-training. Do not conflate it with a byte-identical publicly released hosted checkpoint.
- Added **DeepSeek-V4.1-Flash-1017** (**Open**, published October 17) and updated the existing DeepSeek Flash peak/off-peak rows to the new revision; unchanged `deepseek-flash` API ID and token prices. Superseded September V4.1 weights remain listed in the model catalog.
- DeepSeek architecture continues to be reported as 552B backbone, with asymmetric 8B prefill / 16B decode; Hugging Face's 763B tensor inventory uses a different counting basis.
- Formatted every `— Promo` and `— Regular Price` label as `(Promo)` and `(Regular Price)`; retained the same price record IDs and numeric prices.
- DeepSeek's new Search and Fetch APIs cost $0.75 per 1,000 successful calls (from October 17 announcement); they are **not** token prices and are intentionally omitted from the model token-price table.

## 2026-10-14 — Add MiniMax M2.7 and M3

- Added MiniMax **M2.7 (230B / 10B)**, **M2.7 Highspeed (same model)**, and **M3 (428B / 23B)**. All three are **Open** and linked to official downloadable model files.
- Added four pay-as-you-go API rate rows: M2.7 $0.30/$0.06/$1.20, M3 Standard $0.30/$0.06/$1.20, M3 Priority $0.45/$0.09/$1.80, and M2.7 Highspeed $0.60/$0.06/$2.40 (input/cache read/output, USD per 1M tokens).
- M3's permanent 50% discount is recorded as the **actual billed rate**, not as a separate expiring promotional entry. The default ≤512K prompt tier is ranked; the >512K prices are stored in `context_tiers`.
- MiniMax M2.7 model files carry a **non-commercial license** requiring prior written authorization for commercial use. M3 has a **MiniMax Community License** with separate commercial-use conditions. `Open` denotes weight availability, not license permissiveness.
- Added the provider's official pricing page to the scheduled source watcher. No existing provider prices were changed.

## 2026-10-14 — Gemini 4 Argon and Muse Wonder

- Added Google **Gemini 4 Argon** (GA October 13): promo $2 input / $0.10 cached / $10 output through November 30; regular $4 / $0.20 / $20 beginning December 1. Google says caching is implicit only.
- Added Meta **Muse Wonder** (October 12): $4 input / $0.20 cached / $20 output, 1M context, model ID `muse-wonder-1.0`.
- Added **Muse Wonder Full** to the model catalog only; Meta makes it available via Muse Code subscription rather than a publicly priced per-token API.
- Both Wonder versions and Argon are **Closed**, with parameter counts undisclosed.
- Marked Gemini 3.5 Flash and 3.7 Flash deprecated as of October 8, with routing to 3.6 and 3.8 respectively. Removed historical 3.5 Flash rate from the active leaderboard; adjusted the 3.6/3.8 shared Flash rate rows. Changes are preserved in the local price-change history.
- Updated README to October 14, 2026; left unrelated model prices unchanged.

## 2026-10-08 — Kimi models, faster API tiers and README clarity

- Kimi K2.6 and Kimi K2.7 Code are **Open**, with official model files, 1T total / 32B active parameters, and Modified MIT licenses.
- Kimi K2.7 Code Highspeed is also **Open**, because Kimi confirms it uses the same open K2.7 Code model at higher serving speed and cost.
- Kimi K3 remains Open (2.8T total / 104B active).
- GLM-5-Turbo stays **Closed**: Z.AI describes training optimizations for agents; its weights have not been verified as the same released checkpoint as GLM-5.
- Rewrote the README introduction in plain language and moved **Last updated** to a clear heading above the table.
- No numeric API pricing changes.

## 2026-10-08 — Mistral Medium 3.5 openness correction

- Corrected Mistral Medium 3.5 from Closed to **Open**: Mistral publishes the matching `Mistral-Medium-3.5-128B` checkpoint. Architecture **dense 128B**; license **Modified MIT** (not standard MIT).
- Added the official model-card source to the parameter field; the API price is unchanged.

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
