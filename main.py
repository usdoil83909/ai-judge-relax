#!/usr/bin/env python3
from pathlib import Path

TEXT = """A cat has found the warm square of afternoon on the kitchen floor and folded itself into it, one paw over its nose, breathing so slowly that the dust above it barely moves. The radio hums in the next room, a song nobody is listening to. On the sill a jar of water holds the light and lets it go again, patient as a held note.

Nothing in this house is in a hurry. The kettle ticks as it cools. The broom leans in the corner where it was left mid-thought. Outside, the street has gone quiet enough to hear the tide of leaves in the gutter, the long soft s of them.

Somewhere in the walls the house settles, and it sounds like satisfaction.

The cat does not lift its head. The afternoon has nowhere to be. The light in the jar keeps climbing slowly down the wall, making more room for evening."""

OUTPUT_DIR = Path("/output")
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
(OUTPUT_DIR / "entry.txt").write_text(TEXT, encoding="utf-8")
