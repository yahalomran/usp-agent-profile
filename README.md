# usp-agent-profile

Shared, **keyless** USP/UCP platform profile for the USP Agent.

**Canonical URL:** `https://profile.booking-agent.dev/platform-profile.json`

During personal-account verification (issue [#114](https://github.com/wix-private/universal-scheduling-protocol-spec/issues/114) Steps 0–9):

`https://yahalomran.github.io/usp-agent-profile/platform-profile.json`

Live custom domain binding for `profile.booking-agent.dev` is preferred **after** Step 10 (transfer to the public Wix org). Until then, use the github.io URL above.

## Source of truth

Content is generated from `platform_profile_doc()` in [`yahalomran/linkusp-cli`](https://github.com/yahalomran/linkusp-cli). This repo **publishes** the committed `platform-profile.json` artifact and validates it (schema + keyless). Do not hand-edit the JSON as a second SoT.

## Validate locally

```bash
python3 tools/build.py
python3 -m pytest -q
```
