# Methodology

## Units, comparison and sorting

Every price is in USD per **one million tokens**. `Combined = input + output` represents 1M uncached input tokens plus 1M output tokens; this is an arithmetic index, not a real workload estimate. Cached Input is a **cache read** rate, not a cache write rate. `null` signifies unknown / not provided, not free. Rows sort by Combined, then Cached Input; missing cache prices sort after known cache rates within ties.

## Model weights, licenses and parameters

An `open_weight` classification means public downloadable weights, **not necessarily an OSI-approved open-source license**. `closed_weight` means proprietary hosted weights. `announced_open_weight` means a future publication has been announced but no public checkpoint was verified at the catalog cutoff. `unknown` means insufficient evidence. See model license fields rather than treating all open weights as Apache or MIT.

`total_parameters_b` and `active_parameters_b` are in billions. Model sizes not publicly disclosed are null; model families' public checkpoint sizes must not be projected onto differently deployed API versions.

Mistral Large 4 was announced with about 1.05T total parameters and 49B core active parameters (approximately 52B including embeddings/output layers), with open weights announced for a later release. At this snapshot the weights were not marked downloadable. Similarly Qwen's related open-weight Flash-Next checkpoint must not be silently equated to Qwen3.8 Flash's production API parameters.

## Pricing types and provenance

Rate records can be standard, promo, regular, peak, off_peak, contributor, or highspeed. Context-tiered models show base-tier prices in the leaderboard, while notes provide the larger-context prices where known. DeepSeek peak/off-peak are time-based tariffs. Contributor tiers can have different data sharing policies. Expired promo prices must not remain labeled current.

Each row links to its pricing source. `pricing_review` marks the degree of checking. `pricing_verified_at` is a verification date, never inferred from release date. This repository includes historical rates only when actually recorded; the history program does not invent historical vendor announcement dates.

## Updating data

Edit `data/models.json` and `data/pricing.json`, then run:

```sh
python scripts/validate_data.py
python scripts/generate_readme.py
python scripts/generate_models.py
python scripts/update_history.py
python -m unittest discover -s tests -v
```

The GitHub Actions checks verify data constraints and that README and the catalog can be generated deterministically. The source watcher performs best-effort reachability/term checking only; missing terms do **not** prove a price change. No prices are auto-rewritten.
