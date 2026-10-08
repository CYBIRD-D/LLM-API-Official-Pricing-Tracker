# LLM API Official Pricing Tracker

## Last updated: **2026-10-08**

> [!IMPORTANT]
> **All prices are in US dollars per 1 million tokens.** This is an updated reference table, not a live price feed. Some older prices still need rechecking, so click the provider's Source link before relying on a number.

Compare AI API prices from OpenAI, Anthropic, Google, xAI, Qwen, DeepSeek, Kimi, GLM, Mistral, and Meta/OpenRouter.

## How to read the table

- **Input:** what you pay for the text you send.
- **Cached Input:** the lower price for reused input. **—** means the price is unknown, not free.
- **Output:** what you pay for the model's answer.
- **Combined:** Input + Output, counting 1 million tokens of each. It's a way to rank prices, not a prediction of your bill.
- **Open:** downloadable model files exist, or the vendor confirms a faster API option uses the same public model.
- **Closed:** we haven't verified downloadable files for that exact version. Other open models in the same family don't automatically count.
- **Parameters:** model size. For MoE models, we show **total / active** parameters.

The cheapest **Combined** price comes first. Ties use the cheaper confirmed cached-input price. Promotional prices and peak/off-peak rates get separate rows.

**Faster service isn't always a new model.** Kimi K2.7 Code HighSpeed is the same open model served faster for more money. GLM-5-Turbo was separately optimized during training for agent tasks; we cannot assume it uses exactly the same public files as GLM-5.

More detail: [How the numbers are collected](docs/methodology.md) · [Suggest a correction](CONTRIBUTING.md)

## Price leaderboard
<!-- CATALOG:START -->
| Rank | Provider | Model | Open/Closed | Parameters (Total / Active) | Input | Cached Input | Output | Combined | Notes | Pricing source |
|---:|---|---|---|---|---:|---:|---:|---:|---|---|
| 1 | Qwen | Qwen3.7 Flash | Closed | Not disclosed | $0.03 | — | $0.13 | **$0.16** | ≤32K; 32K–256K: $0.10/$0.40; 256K–1M: $0.20/$0.80 | [Source](https://www.alibabacloud.com/help/en/model-studio/model-pricing) |
| 2 | Meta / OpenRouter | Muse Spark 1.2/1.3 Contributor | Closed | Not disclosed | $0.10 | $0.002 | $0.20 | **$0.30** | 1M context; prompts/outputs may be used to improve Meta products | [Source](https://openrouter.ai/meta/muse-spark-1.3-contributor) |
| 3 | Qwen | Qwen3.5 Flash | Open | [35B / 3B active](https://huggingface.co/Qwen/Qwen3.5-35B-A3B) | $0.10 | — | $0.40 | **$0.50** | International | [Source](https://www.alibabacloud.com/help/en/model-studio/model-pricing) |
| 4 | Anthropic | Claude Haiku 5.5 | Closed | Not disclosed | $0.10 | $0.01 | $0.50 | **$0.60** | ≤100K; >100K: $0.50 input / $0.05 cache / $2.50 output | [Source](https://platform.claude.com/docs/en/models/haiku-5-5/overview) |
| 5 | OpenAI | GPT-6 Luna | Closed | Not disclosed | $0.10 | $0.01 | $0.50 | **$0.60** | 1.05M context; >272K: $0.20/$0.75 | [Source](https://developers.openai.com/api/docs/pricing) |
| 6 | Qwen | Qwen3.8 Flash | Open | [125B / 6B active](https://huggingface.co/Qwen/Qwen3.8-Flash-Next) | $0.15 | — | $0.47 | **$0.62** | International; 1M context | [Source](https://www.alibabacloud.com/help/en/model-studio/model-pricing) |
| 7 | GLM / Z.AI | GLM-5.3-Flash | Open | [320B / 18B active](https://huggingface.co/zai-org/GLM-5.3-Flash) | $0.15 | $0.03 | $0.50 | **$0.65** | Standard price | [Source](https://docs.z.ai/guides/overview/pricing) |
| 8 | DeepSeek | DeepSeek V4.1 Flash — Off-peak | Open | [552B / 8B–16B active](https://huggingface.co/deepseek-ai/DeepSeek-V4.1-Flash) | $0.15 | $0.003 | $0.60 | **$0.75** | 1M context; off-peak pricing | [Source](https://api-docs.deepseek.com/quick_start/pricing/) |
| 9 | Mistral | Mistral Small 4 | Open | [119B / 6.5B active](https://huggingface.co/mistralai/Mistral-Small-4-119B-2603) | $0.15 | $0.015 | $0.60 | **$0.75** | 256K context | [Source](https://docs.mistral.ai/models/mistral-small-4-0-26-03) |
| 10 | OpenAI | GPT-5.6 Luna | Closed | Not disclosed | $0.20 | $0.02 | $1.20 | **$1.40** | >272K: $0.40/$1.80 | [Source](https://developers.openai.com/api/docs/pricing) |
| 11 | Meta / OpenRouter | Muse Glimmer 30B | Open | [30B](https://openrouter.ai/meta/muse-glimmer-30b) | $0.30 | $0.04 | $1.10 | **$1.40** | 131K context | [Source](https://openrouter.ai/meta/muse-glimmer-30b) |
| 12 | OpenAI | GPT-5.4 nano | Closed | Not disclosed | $0.20 | $0.02 | $1.25 | **$1.45** | — | [Source](https://developers.openai.com/api/docs/pricing) |
| 13 | DeepSeek | DeepSeek V4.1 Flash — Peak | Open | [552B / 8B–16B active](https://huggingface.co/deepseek-ai/DeepSeek-V4.1-Flash) | $0.30 | $0.006 | $1.20 | **$1.50** | 1M context; peak pricing | [Source](https://api-docs.deepseek.com/quick_start/pricing/) |
| 14 | Qwen | Qwen3.7 Plus — Promo | Closed | [397B / 17B active](https://huggingface.co/Qwen/Qwen3.8-Flash-Next) | $0.32 | — | $1.28 | **$1.60** | International alias; 20% off; regular $0.40/$1.60 | [Source](https://www.alibabacloud.com/help/en/model-studio/model-pricing) |
| 15 | Google | Gemini 3.1 Flash-Lite | Closed | Not disclosed | $0.25 | $0.025 | $1.50 | **$1.75** | — | [Source](https://ai.google.dev/gemini-api/docs/pricing) |
| 16 | Qwen | Qwen3.6 Flash | Open | [35B / 3B active](https://www.alibabacloud.com/blog/qwen3-6-35b-a3b-thinking-open-weights-uncompromised-agentic-coding_603043) | $0.25 | — | $1.50 | **$1.75** | ≤256K; International | [Source](https://www.alibabacloud.com/help/en/model-studio/model-pricing) |
| 17 | Qwen | Qwen3.7 Plus — Regular Price | Closed | [397B / 17B active](https://huggingface.co/Qwen/Qwen3.8-Flash-Next) | $0.40 | — | $1.60 | **$2.00** | ≤256K | [Source](https://www.alibabacloud.com/help/en/model-studio/model-pricing) |
| 18 | DeepSeek | DeepSeek V4 Pro — Off-peak | Open | [1.6T / 49B active](https://huggingface.co/deepseek-ai/DeepSeek-V4-Pro) | $0.66 | $0.022 | $1.98 | **$2.64** | Off-peak pricing | [Source](https://api-docs.deepseek.com/quick_start/pricing/) |
| 19 | Google | Gemini 3.5 Flash-Lite | Closed | Not disclosed | $0.30 | $0.03 | $2.50 | **$2.80** | — | [Source](https://ai.google.dev/gemini-api/docs/pricing) |
| 20 | Qwen | Qwen3.5 Plus | Open | [397B / 17B active](https://huggingface.co/Qwen/Qwen3.5-397B-A17B) | $0.40 | — | $2.40 | **$2.80** | ≤256K; International | [Source](https://www.alibabacloud.com/help/en/model-studio/model-pricing) |
| 21 | xAI | Grok Build 0.1 | Closed | Not disclosed | $1.00 | $0.20 | $2.00 | **$3.00** | <200K; ≥200K: $2/$4 | [Source](https://docs.x.ai/developers/pricing) |
| 22 | Qwen | Qwen3.6 Plus | Closed | Not disclosed | $0.50 | — | $3.00 | **$3.50** | ≤256K; International | [Source](https://www.alibabacloud.com/help/en/model-studio/model-pricing) |
| 23 | xAI | Grok 4.20/4.3 | Closed | Not disclosed | $1.25 | $0.20 | $2.50 | **$3.75** | <200K; ≥200K: $2.50/$5 | [Source](https://docs.x.ai/developers/pricing) |
| 24 | GLM / Z.AI | GLM-5 | Open | [744B / 40B active](https://huggingface.co/zai-org/GLM-5) | $1.00 | $0.20 | $3.20 | **$4.20** | — | [Source](https://docs.z.ai/guides/overview/pricing) |
| 25 | Google | Gemini 3.6/3.7/3.8 Flash — Promo | Closed | Not disclosed | $0.75 | $0.075 | $3.75 | **$4.50** | Introductory price through Dec 31, 2026 | [Source](https://ai.google.dev/gemini-api/docs/pricing) |
| 26 | Kimi | Kimi K2.6 | Open | [1T / 32B active](https://huggingface.co/moonshotai/Kimi-K2.6) | $0.95 | $0.16 | $4.00 | **$4.95** | ~262K context | [Source](https://www.kimi.com/) |
| 27 | Kimi | Kimi K2.7 Code | Open | [1T / 32B active](https://huggingface.co/moonshotai/Kimi-K2.7-Code) | $0.95 | $0.19 | $4.00 | **$4.95** | ~262K context | [Source](https://www.kimi.com/) |
| 28 | GLM / Z.AI | GLM-5-Turbo | Closed | Not disclosed | $1.20 | $0.24 | $4.00 | **$5.20** | 200K context; agent-tuned Turbo variant | [Source](https://docs.z.ai/guides/overview/pricing) |
| 29 | OpenAI | GPT-5.4 mini | Closed | Not disclosed | $0.75 | $0.075 | $4.50 | **$5.25** | — | [Source](https://developers.openai.com/api/docs/pricing) |
| 30 | DeepSeek | DeepSeek V4 Pro — Peak | Open | [1.6T / 49B active](https://huggingface.co/deepseek-ai/DeepSeek-V4-Pro) | $1.32 | $0.044 | $3.96 | **$5.28** | Peak pricing | [Source](https://api-docs.deepseek.com/quick_start/pricing/) |
| 31 | Meta / OpenRouter | Muse Spark 1.1/1.2/1.3 | Closed | Not disclosed | $1.25 | $0.15 | $4.25 | **$5.50** | 1M context; standard data policy | [Source](https://openrouter.ai/meta/muse-spark-1.3) |
| 32 | Mistral | Mistral Large 4 | Closed | [1.05T / 49B active](https://huggingface.co/mistralai/Mistral-Large-4.0-1T05-A52B) | $1.36 | $0.14 | $4.18 | **$5.54** | 1M context; public preview; regular published price | [Source](https://docs.mistral.ai/models/mistral-large-4-0) |
| 33 | GLM / Z.AI | GLM-5.1 | Open | [744B / 40B active](https://huggingface.co/zai-org/GLM-5.1) | $1.40 | $0.26 | $4.40 | **$5.80** | 200K context | [Source](https://docs.z.ai/guides/overview/pricing) |
| 34 | GLM / Z.AI | GLM-5.2/5.3 | Open | 744B / 40B active | $1.40 | $0.26 | $4.40 | **$5.80** | 1M context | [Source](https://docs.z.ai/guides/overview/pricing) |
| 35 | xAI | Grok 4.5 | Closed | [≈1.5T (Musk claim)](https://x.com/elonmusk/status/2078289996323148076) | $2.00 | $0.30 | $6.00 | **$8.00** | <200K; ≥200K: $4/$12 | [Source](https://docs.x.ai/developers/pricing) |
| 36 | xAI | Grok 4.6 | Closed | [≈1.5T (Musk claim)](https://x.com/elonmusk/status/2082123925283041545) | $2.00 | $0.50 | $6.00 | **$8.00** | <200K; ≥200K: $4/$12 | [Source](https://docs.x.ai/developers/pricing) |
| 37 | xAI | Grok 4.7 | Closed | [≈2.1T (Musk claim)](https://x.com/elonmusk/status/2082123925283041545) | $2.00 | $0.50 | $6.00 | **$8.00** | 500K context; ≥200K: $4/$12 | [Source](https://docs.x.ai/developers/pricing) |
| 38 | Qwen | Qwen3.8 Max | Open | [2.4T / 95B active](https://huggingface.co/Qwen/Qwen3.8-2.4T-A95B) | $2.00 | — | $6.00 | **$8.00** | International; 1M context | [Source](https://www.alibabacloud.com/help/en/model-studio/model-pricing) |
| 39 | Google | Gemini 3.6/3.7/3.8 Flash — Regular Price | Closed | Not disclosed | $1.50 | $0.15 | $7.50 | **$9.00** | Standard price from Jan 1, 2027 | [Source](https://ai.google.dev/gemini-api/docs/pricing) |
| 40 | Mistral | Mistral Medium 3.5 | Open | [128B / 128B active](https://huggingface.co/mistralai/Mistral-Medium-3.5-128B) | $1.50 | $0.15 | $7.50 | **$9.00** | 256K context | [Source](https://docs.mistral.ai/models/) |
| 41 | Kimi | Kimi K2.7 Code Highspeed | Open | [1T / 32B active](https://huggingface.co/moonshotai/Kimi-K2.7-Code) | $1.90 | $0.38 | $8.00 | **$9.90** | ~262K; same K2.7 Code model, faster output | [Source](https://www.kimi.com/) |
| 42 | Qwen | Qwen3.7 Max | Closed | Not disclosed | $2.50 | — | $7.50 | **$10.00** | International; 1M context | [Source](https://www.alibabacloud.com/help/en/model-studio/model-pricing) |
| 43 | Google | Gemini 3.5 Flash | Closed | Not disclosed | $1.50 | $0.15 | $9.00 | **$10.50** | Thinking tokens billed as output | [Source](https://ai.google.dev/gemini-api/docs/pricing) |
| 44 | Anthropic | Claude Sonnet 5.5 | Closed | Not disclosed | $2.00 | $0.10 | $10.00 | **$12.00** | Cache read reduced to $0.10 on Oct 7 | [Source](https://platform.claude.com/docs/en/about-claude/pricing) |
| 45 | OpenAI | GPT-6.1 Sol | Closed | Not disclosed | $2.00 | $0.10 | $10.00 | **$12.00** | 1.05M context; >272K: $4/$0.20/$15 | [Source](https://developers.openai.com/api/docs/pricing) |
| 46 | Anthropic | Claude Sonnet 5 | Closed | Not disclosed | $2.00 | $0.20 | $10.00 | **$12.00** | — | [Source](https://platform.claude.com/docs/en/about-claude/pricing) |
| 47 | OpenAI | GPT-6 Sol | Closed | Not disclosed | $2.00 | $0.20 | $10.00 | **$12.00** | 1.05M context; >272K: $4/$0.40/$15 | [Source](https://developers.openai.com/api/docs/pricing) |
| 48 | Google | Gemini 3.1 Pro Preview | Closed | Not disclosed | $2.00 | $0.20 | $12.00 | **$14.00** | ≤200K; >200K: $4/$18 | [Source](https://ai.google.dev/gemini-api/docs/pricing) |
| 49 | OpenAI | GPT-5.6 Terra | Closed | Not disclosed | $2.00 | $0.20 | $12.00 | **$14.00** | >272K: $4/$18 | [Source](https://developers.openai.com/api/docs/pricing) |
| 50 | OpenAI | GPT-5.4 | Closed | Not disclosed | $2.50 | $0.25 | $15.00 | **$17.50** | >272K long-context surcharge | [Source](https://developers.openai.com/api/docs/pricing) |
| 51 | Anthropic | Claude Sonnet 4.6 | Closed | Not disclosed | $3.00 | $0.30 | $15.00 | **$18.00** | — | [Source](https://platform.claude.com/docs/en/about-claude/pricing) |
| 52 | Kimi | Kimi K3 | Open | [2.8T / 104B active](https://huggingface.co/moonshotai/Kimi-K3) | $3.00 | $0.30 | $15.00 | **$18.00** | 1M context | [Source](https://www.kimi.com/) |
| 53 | Anthropic | Claude Opus 5.5 | Closed | Not disclosed | $4.00 | $0.20 | $20.00 | **$24.00** | 1M context | [Source](https://platform.claude.com/docs/en/about-claude/pricing) |
| 54 | OpenAI | GPT-5.6 Sol — Promo | Closed | Not disclosed | $4.00 | $0.40 | $20.00 | **$24.00** | Promo available at least through Nov 21, 2026; regular $5/$30 | [Source](https://developers.openai.com/api/docs/pricing) |
| 55 | Anthropic | Claude Opus 4.7/4.8/5 | Closed | Not disclosed | $5.00 | $0.50 | $25.00 | **$30.00** | — | [Source](https://platform.claude.com/docs/en/about-claude/pricing) |
| 56 | OpenAI | GPT-5.5 | Closed | Not disclosed | $5.00 | $0.50 | $30.00 | **$35.00** | — | [Source](https://developers.openai.com/api/docs/pricing) |
| 57 | OpenAI | GPT-5.6 Sol — Regular Price | Closed | Not disclosed | $5.00 | $0.50 | $30.00 | **$35.00** | Original price; currently $4/$20 promo | [Source](https://developers.openai.com/api/docs/pricing) |
| 58 | Anthropic | Claude Fable 5.1 | Closed | Not disclosed | $10.00 | $0.25 | $50.00 | **$60.00** | 1M context; low 0.025x cache-read multiplier | [Source](https://platform.claude.com/docs/en/about-claude/pricing) |
| 59 | Anthropic | Claude Fable 5 | Closed | Not disclosed | $10.00 | $1.00 | $50.00 | **$60.00** | — | [Source](https://platform.claude.com/docs/en/about-claude/pricing) |
| 60 | OpenAI | GPT-6 Astra | Closed | Not disclosed | $10.00 | $1.00 | $50.00 | **$60.00** | 1.05M context; >272K: $20/$2/$75 | [Source](https://developers.openai.com/api/docs/pricing) |
| 61 | OpenAI | GPT-5.4/5.5 Pro | Closed | Not disclosed | $30.00 | — | $180.00 | **$210.00** | Maximum-compute tier | [Source](https://developers.openai.com/api/docs/pricing) |
<!-- CATALOG:END -->

## Use the repository

Requires **Python 3.10+**; runtime and tests use only Python's standard library.

```bash
python scripts/validate_data.py
python scripts/generate_readme.py
python -m unittest discover -s tests -v
python scripts/check_sources.py --out source-report.json
```

When editing a model or price:

1. Update `data/models.json` (weights/parameters) or `data/pricing.json` (one or more rate entries). Retain source links and add an actual `pricing_verified_at` when you have checked the source.
2. Run `python scripts/update_history.py` to record changes to the **local catalog** in `data/pricing-history.json`. This is not a backfilled history of the vendor's original announcements.
3. Run `python scripts/generate_readme.py`, `python scripts/generate_models.py`, and `python scripts/validate_data.py`; commit the changed JSON, snapshot, history and README.
4. Submit changes by pull request with vendor source, timestamp, currency and context tier. See [CONTRIBUTING.md](CONTRIBUTING.md).

The `source-watch.yml` scheduled workflow checks a small set of monitored pages for expected snippets and saves a report artifact. A missing snippet is **only a manual-review flag** (websites may use client-side rendering, blocked bots, or changed layouts). It never silently overwrites token prices. `validate.yml` checks data integrity and a reproducible README on pull requests.

## Data and documentation

| File | Purpose |
|---|---|
| [`docs/model-catalog.md`](docs/model-catalog.md) | Generated per-model open-weight/license/parameter index |
| [`data/models.json`](data/models.json) | Per-model name, provider, open-weight status, license, total/active parameters, links |
| [`data/pricing.json`](data/pricing.json) | Per-rate input, cached input, output, pricing type, source and review state |
| [`data/pricing-history.json`](data/pricing-history.json) | Changes subsequently recorded **within this repository** |
| [`data/last-recorded-prices.json`](data/last-recorded-prices.json) | Baseline for audit-friendly local history generation |
| [`data/source-watches.json`](data/source-watches.json) | Monitored source-page snippets; edit cautiously |
| [`docs/methodology.md`](docs/methodology.md) | Detailed price, parameter, license, and validation methodology |
| [`docs/changelog.md`](docs/changelog.md) | Human-readable catalog update notes |

## Contributing and licensing

Dataset/editorial code is made available under the **MIT License**; this **does not** relicense any third-party model weights, text, trademarks, or vendors' documentation. Always read the actual license of each model. For corrections, open a pull request or issue and include official citations.
