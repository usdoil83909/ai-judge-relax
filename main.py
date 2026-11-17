#!/usr/bin/env python3
from pathlib import Path

TEXT = """You may set everything down now.

The day's small urgencies can wait outside a moment. Notice the quiet around you - not empty, just unhurried, like a room after rain. Let one slow breath arrive on its own, then another, each a little lower and softer than the last.

Somewhere a kettle cools. A curtain lifts and settles. None of it asks anything of you. The things you are holding are patient; they will still be there, and they will be lighter.

Let your shoulders drop a fraction. Unclench the small places - the jaw, the hands, the space behind the eyes. There is no score to keep here, nothing to compare, nothing to prove. For these few lines you are simply allowed.

If a thought arrives, let it drift past like a leaf on still water, and turn gently back to the breath, back to the warm weight of being here.

Rest is not a reward you earn later. It is already yours, this quiet minute, exactly as you are.

Everything is fine. Stay a moment longer."""

OUTPUT_DIR = Path("/output")
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
(OUTPUT_DIR / "entry.txt").write_text(TEXT, encoding="utf-8")
