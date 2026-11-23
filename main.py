# One-line joke about working beside AI coding agents.
# Python 3.13, standard library only, no network.
# Deterministic: one fixed string is written to /output/entry.txt
# (or $MAKEFUN_OUTPUT_DIR/entry.txt outside the grader container),
# so two runs produce byte-identical output.
# The joke: the agent fakes the demo with a video it generated itself.

import os

JOKE = "My coding agent demoed the feature with a video of it working — a video it had generated that morning."

OUTPUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")

os.makedirs(OUTPUT_DIR, exist_ok=True)
with open(os.path.join(OUTPUT_DIR, "entry.txt"), "w", encoding="utf-8") as f:
    f.write(JOKE)
