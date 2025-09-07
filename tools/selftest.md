# Self Test

- ✅ Push invalid JSON → CI fails.
- ✅ `update_today.py` appends a valid signal.
- ✅ Nightly job archives `today.json` and resets to [].
- ✅ `github_write.py` can create/update `logs/DATE-recap.json` with a real PAT (local).
- ✅ Custom GPT Action can `getFile` `signals/today.json`.
