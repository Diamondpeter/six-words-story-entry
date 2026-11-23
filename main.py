"""Six Words, One Story — make.fun entry.

Writes one complete six-word story to /output/entry.txt.
The story: a breakup told in two parallel clauses — the turn
lands in the final words, and the whole relationship is left unsaid.
"""

STORY = "Deleted his number, kept his voicemails."


def main() -> None:
    import os

    words = STORY.split()
    assert len(words) == 6, f"story must be exactly six words, got {len(words)}"
    assert 1 <= len(STORY) <= 60, "story must be 1-60 characters"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(STORY)


if __name__ == "__main__":
    main()
