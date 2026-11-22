import os
import sys

# Entry text under 280 code points for relaxation judge (v1.1 verified)
TEXT = "Dusk settles across the mountain lake as the wind falls still. The pine forest breathes quietly in the evening coolness, and small riplets tap against the shoreline stones. Everything is quiet."

def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    if not os.path.exists(out_dir):
        try:
            os.makedirs(out_dir, exist_ok=True)
        except Exception:
            out_dir = "./output"
            os.makedirs(out_dir, exist_ok=True)
    out_file = os.path.join(out_dir, "entry.txt")
    with open(out_file, "w", encoding="utf-8") as f:
        f.write(TEXT)
    print(f"Wrote {len(TEXT)} characters to {out_file}")

if __name__ == "__main__":
    main()
