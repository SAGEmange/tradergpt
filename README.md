# Trader Signals Repo

![Owner Avatar](https://github.com/SAGEmange.png?size=120)

A GitHub-hosted data backend for **TraderGPT v2.5** providing JSON/CSV signals, configs, market data, overlays and logs for Boom500 and Crash1000 scalping.

## Quick Start

```bash
pip install -r requirements.txt  # none yet, jsonschema used in tools
python tools/validate.py          # validate JSON files
```

## Repository Structure

```
signals/            Active and archived trade signals
configs/            Account and per-market settings
data/               Market statistics and notes
overlays/           Visual trading zones
logs/               Daily PNL, recaps and trade journal
schemas/            JSON Schemas + OpenAPI description
tools/              Helper scripts and automation hooks
.github/workflows/  CI validation and nightly archive
```

## Daily Ops

- `python tools/update_today.py` to append new signals
- CI validates all JSON on push
- Nightly workflow archives `signals/today.json` and resets it

## Access

### Raw (public)

Use raw URLs for read-only access:

```
https://raw.githubusercontent.com/SAGEmange/trader-signals-repo/main/signals/today.json
https://raw.githubusercontent.com/SAGEmange/trader-signals-repo/main/configs/account.json
```

### GitHub REST (private)

Read:

```bash
curl -H "Accept: application/vnd.github.raw+json" \
     -H "Authorization: Bearer $GITHUB_TOKEN" \
     https://api.github.com/repos/SAGEmange/trader-signals-repo/contents/signals/today.json
```

Write:

```bash
curl -X PUT \
  -H "Authorization: Bearer $GITHUB_TOKEN" \
  -H "Accept: application/vnd.github+json" \
  https://api.github.com/repos/SAGEmange/trader-signals-repo/contents/logs/2025-09-07-recap.json \
  -d '{
    "message": "chore: add recap 2025-09-07",
    "content": "<BASE64_CONTENTS>",
    "branch": "main",
    "sha": "<EXISTING_SHA_IF_UPDATING>"
  }'
```

## Custom GPT Action

Add `schemas/openapi.trader-signals.json` to your GPT action with **Bearer (User provides token)** auth. Use a read-only token for raw access and a write token only if uploading logs or recaps.

## CI

- `.github/workflows/validate.yml` – validates JSON using `jsonschema`
- `.github/workflows/daily-archive.yml` – archives signals nightly

MIT licensed. Contributions welcome.
