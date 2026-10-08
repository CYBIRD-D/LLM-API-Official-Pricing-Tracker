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
