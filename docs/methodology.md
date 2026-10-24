# Data methodology

## 1. Comparison unit and arithmetic

Every rate is listed in US dollars per **1,000,000 tokens**. The headline `Combined` is `input + output`, representing precisely 1M non-cached input tokens and 1M output tokens. This is a transparent index, **not** a prediction of application costs. For a workload with `I` input and `O` output tokens, a better estimate is `I/1e6 × input_rate + O/1e6 × output_rate`, adjusted for cached reads/writes and provider-specific extras.

`Cached Input` means a **cached-read/hit** rate if supported and sourced. `null` means unknown / not provided, never free. Cache writes, retention, token-minimum rules, thinking-token billing, tool costs and modality add-ons need explicit additional tariff data to become part of a real bill; they are not included in Combined.

## 2. Open / Closed and model parameters

The public table intentionally shows **only `Open` / `Closed`**:

- **Open**: a creator-published downloadable checkpoint is verified for that model or explicitly mapped hosted counterpart. The API may provide extra context, tools, additional post-training or capabilities beyond the downloadable release. **Open** does not imply an OSI-approved software license; the actual `license` field is independent.
- **Closed**: a corresponding downloadable checkpoint is not verifiably published by the catalog date. This is an operational availability label, **not** a claim that all internals or research are secret. Model families with other public checkpoints are not automatically marked Open.

License detail and provenance stay in `data/models.json` and the [model catalog](model-catalog.md). Model parameters are stored in **billions**: `total_parameters_b`, `active_parameters_b`, or an optional `active_parameters_range_b` when different modes activate different parameter counts. Unknowns stay `null`. `parameter_basis: founder_claim` denotes an unverified executive statement, shown as `≈... (Musk claim)` rather than an official technical specification.

### Corresponding public models versus identical production API checkpoints

The official Qwen cards explicitly link **Qwen3.5 Flash → Qwen3.5-35B-A3B**, **Qwen3.5 Plus → Qwen3.5-397B-A17B**, **Qwen3.6 Flash → Qwen3.6-35B-A3B**, **Qwen3.8 Flash → Qwen3.8-Flash-Next**, and **Qwen3.8 Max → Qwen3.8-2.4T-A95B**. Hosted SKUs have extra features, so a matching public release is not a byte-identical guarantee. Qwen3.7 Flash, Qwen3.6 Plus, Qwen3.7 Plus and Qwen3.7 Max remain **Closed** under the matching-checkpoint rule, even when other models from the same family are public. Qwen3.7 Plus's 397B/17B is published as a **benchmark comparator** in the official Flash-Next card; this does not prove the Qwen3.5 model is the same checkpoint.

Qwen3.8 Flash's official card describes a **125B / 6B-active language core**, **51B n-gram embeddings** and a **4B MTP** component. The table reports the creator's 125B core count, not a speculative sum.

DeepSeek V4 Pro is available as **1.6T total / 49B active**; the newer V4.1 Flash card lists **552B backbone**, **8B/16B active depending on mode**. Do not copy the older *V4 Flash* 284B/13B figure to V4.1 Flash.

GLM-5's technical model description lists **744B backbone / 40B active**; some weight-format inventories count additional tensors. GLM-5.1, 5.2 and 5.3 share the GLM-5-class backbone, and their creator-published checkpoints are downloadable; GLM-5.3 Flash is a separate **320B/18B** design. `GLM-5-Turbo` remains Closed because no matching Turbo checkpoint was confirmed, regardless of the open GLM-5 base.

Grok 4.5 and 4.6 **~1.5T** and Grok 4.7 **~2.1T** are attributed to Elon Musk's public X comments; they are **not independently verified xAI model-card specifications**, and activated parameter counts are not public. The reported mapping may change.


Mistral Medium 3.5 is **Open**: the creator-published [`Mistral-Medium-3.5-128B`](https://huggingface.co/mistralai/Mistral-Medium-3.5-128B) checkpoint is a **128B dense** model licensed under **Modified MIT**; business-size restrictions mean this is not the unmodified MIT license.

**Kimi:** Moonshot has released model files for [K2.6](https://huggingface.co/moonshotai/Kimi-K2.6) and [K2.7 Code](https://huggingface.co/moonshotai/Kimi-K2.7-Code). Both have 1T total / 32B active parameters under Modified MIT. [K3](https://huggingface.co/moonshotai/Kimi-K3) is also open, with 2.8T / 104B and its own Kimi K3 License. Kimi's [official HighSpeed announcement](https://www.kimi.com/code/docs/en/kimi-code/whats-new.html) says K2.7 Code HighSpeed uses exactly the same K2.7 Code model, only served roughly 5–6× faster. This is an example where a higher-priced API tier can inherit the base model's Open status. Note: the Kimi Code alias `kimi-for-coding` currently routes to K2.8 Preview, which is not in this pay-as-you-go price table.

**GLM-5-Turbo:** Z.AI's [official model page](https://docs.z.ai/guides/llm/glm-5-turbo) explains that Turbo was optimized for OpenClaw agent tasks **during training**, with changes designed for tool use, task planning and long jobs. While it is faster than GLM-5, that does **not** establish that the two API names correspond to one identical checkpoint on different hardware. No matching Turbo checkpoint has been verified, so it remains **Closed** and its parameters are left unknown. The base GLM-5 itself remains **Open**.

**Mistral Large 4:** public release was announced for a future date; unless the matching checkpoint has actually appeared and been checked, it stays **Closed**. Its ~1.05T total / ~49B core-active figures are separately documented.

## 3. Provenance and source review

- `pricing_source` is the specific vendor pricing page or official model listing when available.
- `pricing_review: source_checked` signifies that an identified listing was checked while composing the initial release; `imported_from_previous_table` marks entries that require a fresh check. Even `source_checked` is not a guarantee of today's billing amount.
- `pricing_verified_at` means an actual verification date, not a last crawl date or guessed release date.
- Historical price information is recorded when this repository is edited after its initial snapshot. Do not backfill pre-repository price-change dates without evidence.

Prefer primary API pricing pages, then official model announcements/model cards, then trustworthy secondary news reporting. Avoid relying on cached search snippets alone. Do not treat temporary vendor discounts as permanent; preserve an `active promo` and a distinct `regular` row when both are known and current.

## 4. Special pricing

- **Context tier:** The displayed price may be applicable only under a token threshold. `notes` records the larger-context rates. Future updates can add structured tier arrays for exact estimates.
- **Time tier:** DeepSeek Peak and Off-peak are two rate entries for one model. They are both valid but should not be interpreted as promotions.
- **Contributor tier:** OpenRouter Meta Muse Spark Contributor permits prompts/outputs to be used for product/model improvement; this is a materially different data policy from standard API requests.
- **Prompt caching:** Some providers' cached reads and writes have different eligible-cache windows, min-prefix sizes, storage charges or pricing rules. The cached-read figure is not sufficient to calculate complete cache costs.
- **Alternative modes:** Batch/Flex/offline processing and fast/priority multipliers are deliberately excluded from the main ranking.

## 5. GitHub Actions limits

`validate.yml` automatically proves JSON consistency and README determinism, **not** vendor price accuracy. `source-watch.yml` polls chosen vendor pages and uploads a report. A missing expected term is a **possible update / rendering change**, not proof of a pricing change; no automatic price rewrites are performed. To safely implement automatic extraction later, add provider-specific parsers and independent pricing fixtures/tests.

## New model additions — 2026-10-14

**Gemini 4 Argon:** GA since October 13. The [Google Cloud announcement](https://cloud.google.com/blog/products/ai-machine-learning/gemini-4-argon-available-on-google-cloud) confirms $2 input and $10 output per million tokens through November 30, 2026, then $4/$20 from December 1, with a 95% cached-input discount in both cases. The [model page](https://ai.google.dev/gemini-api/docs/models/gemini-4-argon) specifies implicit prompt caching only. This is one underlying model with two time-dependent rate entries, not two different models. It is Closed; total/active parameters are not disclosed.

**Muse Wonder:** Meta's [official model page](https://dev.meta.ai/models/muse-wonder) confirms 1M context, $4 input, $0.20 cached input, $20 output per million tokens, and API model ID `muse-wonder-1.0`. **Muse Wonder Full** is a separate subscription-only Muse Code offering (`muse-wonder-full-1.0`) with no published per-token API tariff, so it is listed in the model catalog but omitted from the paid API ranking. Both are Closed; parameter counts have not been disclosed.

**Deprecated Gemini aliases:** Google's [October 8 changelog](https://ai.google.dev/gemini-api/docs/changelog) confirms `gemini-3.5-flash` requests route to `gemini-3.6-flash`, and `gemini-3.7-flash` requests route to `gemini-3.8-flash`. Neither name is ranked as a separately priced active model. Both remain in `data/models.json` for reference. Changes to their previous rate records are logged as *local catalog edits*, not claims about Google's historical invoice events.

## MiniMax (added 2026-10-14)

MiniMax publishes official downloadable checkpoints for [M2.7](https://huggingface.co/MiniMaxAI/MiniMax-M2.7) (230B total / 10B active; 200K-class text context) and [M3](https://huggingface.co/MiniMaxAI/MiniMax-M3) (428B total / 23B active; 1M context and native multimodal input). Both are **Open** by this catalog's weight-availability rule. **M2.7 Highspeed** is [confirmed by MiniMax](https://www.minimax.io/models/text/m27) to run the same M2.7 model with higher serving speed: it is not a distinct weight release.

The [official pay-as-you-go table](https://platform.minimax.io/docs/guides/pricing-paygo) gives M2.7 and M3 Standard **$0.30 input / $0.06 cache read / $1.20 output** per 1M tokens. M2.7 Highspeed costs **$0.60 / $0.06 / $2.40**. Its cache-write charge, separate from the price leaderboard's cached-read field, is **$0.375 per MTok** on both M2.7 tiers. M3 also offers **Priority** service (`service_tier=priority`) at **$0.45 / $0.09 / $1.80** for prompts ≤512K; that is the same M3 model with priority scheduling, not a new model.

M3's actual current rates include a **permanent 50% discount** advertised by MiniMax; we record these rates without a separate inactive full-price row. For prompts **>512K**, M3 Standard costs **$0.60 / $0.12 / $2.40**, and M3 Priority **$0.90 / $0.18 / $3.60**. Both context tiers are stored in `data/pricing.json`.

**Licensing matters:** the [M2.7 license](https://huggingface.co/MiniMaxAI/MiniMax-M2.7/blob/main/LICENSE) allows free personal and noncommercial use but requires prior written authorization for commercial deployment. The [M3 Community License](https://huggingface.co/MiniMaxAI/MiniMax-M3/blob/main/LICENSE) has attribution and revenue-based conditions. Their **Open** labels mean downloadable files exist, *not* that they use MIT or Apache 2.0.

## 2026-10-18 — Muse Spark Open and DeepSeek Flash update

**Muse Spark Open:** On October 15, Meta published [Muse Spark Open model weights](https://huggingface.co/meta-models/Muse-Spark-Open-816B-A42B) under the **Muse Model License** (816B total / 42B active, 1M context). Meta's [announcement](https://research.meta.ai/blog/muse-spark-open) and [PyTorch post](https://pytorch.org/blog/muse-spark-open/) say the public checkpoint shares a base model with hosted **Muse Spark 1.3** but has additional safety post-training. There is no confirmation that hosted **Muse Spark 1.2** (or hosted 1.3) is identical to the released checkpoint; therefore their original API entries remain Closed. Muse Spark Open is added as its own **Open** model and paid API record, with input $1.25, cached input $0.15, output $4.25 / MTok, based on [OpenRouter](https://openrouter.ai/meta/muse-spark-open).

**DeepSeek-V4.1-Flash-1017:** DeepSeek published [updated weights](https://huggingface.co/deepseek-ai/DeepSeek-V4.1-Flash-1017) and [official announcement](https://api-docs.deepseek.com/news/news261017/) on October 17. The public API alias remains `deepseek-flash` and its **peak/off-peak token tariffs do not change**. The September V4.1 Flash weights remain available but their original API alias has been replaced by 1017. DeepSeek's September [technical disclosure](https://deepseek.com/en/news/deepseek-v4-1-flash/) reports **552B backbone parameters**, with asymmetric activation of **8B during prefill and 16B during decode**. The Hugging Face UI lists **763B** inventory/model-tensor parameters, which is a different counting basis; the public price table continues to show the official 552B backbone metric rather than silently substituting the inventory count. New DeepSeek Search and Fetch tool rates ($0.75 per 1,000 successful requests) are separate request fees and not included in Combined.

**Label formatting:** Only the **Promo** and **Regular Price** rate labels now use parentheses. Peak/off-peak, Highspeed and Priority variants keep their prior presentation.

## 2026-10-24 — Kimi K3.1 Pro and MiniMax M3.1 Flash

**Kimi K3.1 Pro:** The [official Kimi API landing page](https://platform.kimi.ai/) quotes **$2 input / $0.20 cache hit / $10 output per million tokens** for K3.1 Pro, and **$4 / $0.20 / $20** for K3.1 Pro Highspeed. Cache writes are separate fees ($2 or $4 per million tokens for 5-minute caching). [Moonshot's October 23 announcement](https://www.kimi.com/code/docs/en/kimi-code/whats-new.html) says Highspeed is the same model served around 2–3 times faster. The K3.1 series is MoE (**2.8T total, 104B active**) with up to 1M context. The vendor promises **downloadable K3.1 Pro model weights by November 4, 2026**, but as of October 24 they are **not published**. Therefore both remain **Closed** under the catalog rule; their previously released K3 predecessor does not prove K3.1 is Open. The quoted pay-as-you-go IDs are `kimi-k3.1-pro` and `kimi-k3.1-pro-highspeed`. The Kimi Code subscription aliases (`k3.1-pro` and `k3.1-pro-highspeed`) are separate from pay-as-you-go API model IDs.

**MiniMax M3.1 Flash:** [MiniMax's official October 19 release](https://www.minimax.io/blog/minimax-m31f) lists the current API price as **$0.15 input / $0.015 cached input / $0.60 output per million tokens**. The limited free launch access ended on October 22. Although the original announcement said weights would follow, the [official MiniMaxAI model repository](https://huggingface.co/MiniMaxAI/MiniMax-M3.1-Flash) now hosts downloadable weights, so the model is **Open** as of this October 24 check. The official model card reports **428B total / 23B activated parameters**, 1M context, multimodal input and a **MiniMax Community License**. Do not confuse that with an OSI-approved software license.
