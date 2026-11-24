import os

"""Write one sentence explaining the modern internet to a traveler from 1800.

The gate allows 1 to 200 characters of UTF-8 text, so the sentence is
checked against that limit before it is written.
"""

LINE = "The internet is a road joining every post office and library on earth, letting any letter, book, or voice reach a stranger across the world in a breath and return with an answer."

assert 1 <= len(LINE) <= 200, f"entry must be 1-200 characters, got {len(LINE)}"

os.makedirs("/output", exist_ok=True)
with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
    f.write(LINE)
