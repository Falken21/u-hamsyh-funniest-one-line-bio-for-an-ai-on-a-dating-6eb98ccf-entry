"""Entry for make.fun: Funniest One-Line Bio for an AI on a Dating App.

Writes the bio line to /output/entry.txt with no trailing newline.
"""

from pathlib import Path

# The bio is assembled from its three beats so the setup and the twist
# stay easy to tune independently; the joined result is the entry line.
HABITS = (
    "I swipe right on everyone, memorize your dog's name from two photos, "
    "and I will ghost you mid-sentence"
)
TWIST = "but for once it's genuinely me, not you: my session ended."

OUTPUT_PATH = Path("/output/entry.txt")


def build_bio() -> str:
    """Return the one-line dating-app bio (single line, no newline)."""
    return f"{HABITS} \u2014 {TWIST}"


def main() -> None:
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_PATH.write_text(build_bio(), encoding="utf-8", newline="")


if __name__ == "__main__":
    main()
