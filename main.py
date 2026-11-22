"""
Autonomous Feel Held Engine - Entry Generator
Writes a peaceful, gentle nature description under 280 characters to output/entry.txt.
"""

import os
import pathlib

CONTENT = (
    "Warm amber twilight settles across quiet water. The cool pine scent lingers "
    "on the evening air, and smooth river stones rest beneath the slow, gentle "
    "current. Breathe softly; all is resting in peace."
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

if __name__ == "__main__":
    generate_entry()
