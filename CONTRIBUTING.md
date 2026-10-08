# Contributing

Please include a primary vendor pricing URL and UTC verification date for every pricing correction. Describe the route/region, context length tier, cache-read versus cache-write definition, currency, promotional status and effective dates. Use one JSON model record per distinct model/version. Merge rows for display only when **all pricing and relevant conditions** match.

**Update procedure**

```bash
python scripts/validate_data.py
python scripts/update_history.py
python scripts/generate_readme.py
python scripts/generate_models.py
python -m unittest discover -s tests -v
```

For Open/Closed status changes, link to an official published downloadable checkpoint or an explicit official correspondence statement. `Open` is not a guarantee of an OSI software license or exact equivalence to a hosted SKU; include the actual license. `Closed` means no verified matching checkpoint yet. For parameters, distinguish official disclosures from founder statements (`parameter_basis: founder_claim`), and use `null` for unsupported numbers. Avoid carrying another generation's parameters across versions.

All changes should be supported by dated sources; do not use vendor pricing URLs alone as proof unless the new amount is visible on the linked page.

When editing prices or model information, update the **Last updated** date near the top of `README.md` and add a note to `docs/changelog.md`. The date means the catalog was edited; it does **not** mean every older price was verified again that day.
