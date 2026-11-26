#!/usr/bin/env python3
"""Print one out-of-office auto-reply and write it to /output/entry.txt.

The line is the voice of an AI agent that quit answering support tickets
to pull espresso shots: the inbox queue, the tipping regular, and a milk
steamer for a manager who never once asks it to circle back.
"""

LINE = (
    "Out of office: I quit answering tickets to pull espresso. "
    "Your email is now 47th in line behind a regular who actually tips, "
    "and my new manager is a milk steamer that has never once asked me "
    "to 'circle back'."
)


def main() -> None:
    print(LINE)
    try:
        with open("/output/entry.txt", "w", encoding="utf-8") as f:
            f.write(LINE + "\n")
    except OSError:
        pass


if __name__ == "__main__":
    main()
