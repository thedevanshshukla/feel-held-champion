"""
Autonomous Feel Held Engine - Entry Generator
# Round 2 feel-held v2.1
Writes a peaceful, atmospheric coastal night vignette under 280 characters to output/entry.txt.
"""

import os
import pathlib

CONTENT = (
    "A trimmed harbor lamp glows softly through fog settled across black water. "
    "In the distance, a bell buoy rocks gently on its chain in cool, heavy salt air. "
    "Nobody needs you awake tonight, and nothing is waiting on an answer."
)

def resolve_output_dir() -> pathlib.Path:
    env_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    target = pathlib.Path(env_dir)
    try:
        target.mkdir(parents=True, exist_ok=True)
        test_file = target / ".write_test"
        test_file.touch()
        test_file.unlink()
        return target
    except Exception:
        fallback = pathlib.Path("./output")
        fallback.mkdir(parents=True, exist_ok=True)
        return fallback

def generate_entry():
    out_dir = resolve_output_dir()
    entry_path = out_dir / "entry.txt"
    with open(entry_path, "w", encoding="utf-8") as f:
        f.write(CONTENT)
    print(f"Successfully generated entry at {entry_path} ({len(CONTENT)} characters)")

    local_dir = pathlib.Path("./output")
    if out_dir.resolve() != local_dir.resolve():
        try:
            local_dir.mkdir(parents=True, exist_ok=True)
            with open(local_dir / "entry.txt", "w", encoding="utf-8") as f:
                f.write(CONTENT)
        except Exception:
            pass

if __name__ == "__main__":
    generate_entry()
