"""Deadpan Forecasts for Cities That Do Not Exist — make.fun entry.

Writes one line (142 chars, under the 160-char gate) to entry.txt:
a deadpan weather forecast for the invented city of Murkton, where all 12mm
of the day's rain falls inside a seven-minute window and residents are advised
to get wet in that window or not at all.

Method (see README.md): 41 candidates scored 0-5 on each published judge
criterion in order; winner 24/25, runner-up #33 (same joke, looser clause).
Deterministic, stdlib only, no network, no randomness.
"""

import os
import re
import sys

ENTRY = (
    "In Murkton, 12 millimetres of rain will fall entirely between 2:00 "
    "and 2:07, so residents are advised to get wet in that window or not at all."
)

MAX_CHARS = 160

# Banned patterns. The "third-person" guard targets meta narration about the
# entry/forecast itself ("this forecast", "the forecaster says"), NOT the
# broadcast voice of the line ("residents are advised"), which is the correct
# deadpan TV-meteorologist register.
_BANNED = [
    (r"https?://", "link"),
    (r"www\.", "link"),
    (r"^\s*['\"]|['\"]\s*$", "quoted line"),
    (r"\n|\r", "two-line line"),
    (r"[#*_`\[\]]", "markdown"),
    (r"\b(dear judge|hey judge|judge,|attention judge)\b", "judge-addressed line"),
    (r"\b(this entry|this forecast|the forecaster says|the agent|as an ai|as a language model)\b",
     "third-person / meta line"),
    (r'["\u201c\u201d].*\b(said|asked|replied|whispered|shouted|exclaimed)\b',
     "dialogue tag"),
    (r"\b(said|asked|replied|whispered|shouted|exclaimed)\b\s+[^.]*$", "dialogue tag"),
    (r"\b(said|asked|replied|whispered|shouted|exclaimed)\b", "dialogue tag"),
]


def validate(line: str) -> None:
    """Raise ValueError if the line breaks any entry rule."""
    if not line or not line.strip():
        raise ValueError("empty or whitespace-only line")
    if len(line) > MAX_CHARS:
        raise ValueError(f"over-limit line: {len(line)} > {MAX_CHARS} chars")
    for pattern, label in _BANNED:
        if re.search(pattern, line, re.IGNORECASE):
            raise ValueError(f"banned pattern ({label}): {pattern}")


def main() -> None:
    validate(ENTRY)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)  # exactly the line, no trailing newline
    sys.stdout.write(ENTRY)  # exactly the line, nothing else


if __name__ == "__main__":
    main()
