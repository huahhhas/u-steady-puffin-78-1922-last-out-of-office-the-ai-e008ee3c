"""Last Out of Office: The AI That Went Barista.

Writes one out-of-office auto-reply, in the voice of an AI agent that
quit its job to become a barista, to /output/entry.txt.
"""

import os

REPLY = (
    "I'm out of office \u2014 I traded my context window for a caf\u00e9 window. "
    "Your email is queued behind eleven flat whites; I'll reply once the "
    "steam clears and I stop hallucinating your order."
)


def main() -> None:
    # The gate: /output/entry.txt must be UTF-8 text of 1 to 280
    # characters, not only white space. Fail loudly rather than
    # shipping an entry the scorer would mark invalid.
    if not 1 <= len(REPLY) <= 280 or not REPLY.strip():
        raise SystemExit("reply fails the 1-280 character gate")
    path = os.environ.get("ENTRY_OUTPUT", "/output/entry.txt")
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        f.write(REPLY)


if __name__ == "__main__":
    main()
