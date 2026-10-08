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

For open weights and parameter count contributions, link to an official model card, released checkpoint or technical report. Include the actual license; do not assume an open-weight release is OSI open source. If a number is unverified, set it to `null` and provide a note instead of guessing.

All changes should be supported by dated sources; do not use vendor pricing URLs alone as proof unless the new amount is visible on the linked page.
