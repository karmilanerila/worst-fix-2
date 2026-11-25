"""Worst Fix Ever: Funniest Commit Message (angle v2).

The joke: the "fix" for users clicking the wrong button was to make
the button bigger. The misclicks did not stop — they just got bigger,
because the button users kept hitting by mistake is now the biggest
target on the screen. The repair made the exact problem it was meant
to solve easier to do.
"""

import os

COMMIT_LINE = (
    "fix: made the button bigger so users stop misclicking; "
    "now they click the big wrong one"
)


def check_line(line):
    """The gate needs 1-100 UTF-8 characters, not only whitespace."""
    if not line.strip():
        raise ValueError("commit line must not be only whitespace")
    size = len(line.encode("utf-8"))
    if not 1 <= len(line) <= 100:
        raise ValueError("commit line must be 1-100 characters")
    return size


def main():
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    target = os.path.join(output_dir, "entry.txt")
    text = COMMIT_LINE
    byte_count = check_line(text)
    encoded = text.encode("utf-8")
    assert len(encoded) == byte_count, "byte count mismatch"
    with open(target, "wb") as handle:
        handle.write(encoded)
    os.chmod(target, 0o644)
    # No trailing newline: the file holds exactly the commit line.
    print("wrote %d characters to %s" % (len(text), target))


if __name__ == "__main__":
    main()
