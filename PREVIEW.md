# Preview — Funniest Time Machine Warning Label

Competition: **Funniest Time Machine Warning Label**
(`u-eager-stork-81-9647-funniest-time-machine-warning-f8add151`, Growth, $2 pool, free entry)
Deadline: 2026-11-26 14:15 UTC (26 Nov 2026 21:15 WIB)

## Entry text (what `main.py` writes to `/output/entry.txt`)

> WARNING: Do not lend money to your past self. He has never paid you back, and he is standing behind you.

- Characters: **104** (gate: 1–120)
- Lines: **1**, no newline inside the text
- Bytes (UTF-8): **104**
- Non-whitespace: yes

## Why this line

- A genuine time-machine warning label, in deadpan official safety-notice voice.
- Real hazard turned into the joke: meeting your duplicate past self (paradox) becomes a debt — he has never paid you back.
- The surprise lands in the last few words: "he is standing behind you."
- No wasted words; every clause does work inside the 120-character cap.

## Local test

```sh
python3 main.py
# wrote 104 characters to /output/entry.txt
cat /output/entry.txt
```

Run twice, byte-identical output (deterministic). Gate mirror check: 1–120 chars, UTF-8, single line, not whitespace-only — LOLOS.

## Status

Built, tested locally, NOT submitted. Awaiting the user's explicit green light before any submit.
