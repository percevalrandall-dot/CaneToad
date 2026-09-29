#!/usr/bin/env python3
"""Sum trapped mass from the Fluent DPM sample file."""

import re

PATH = r"C:\Users\jc814609\Documents\3D-TOAD_files\dp0\FFF-1\Fluent\toad.dpm"

ROW = re.compile(r"^\(\(\s*(.*?)\)\s*\S+\)\s*$")

total = 0.0
with open(PATH, "r", errors="replace") as f:
    for line in f:
        m = ROW.match(line.strip())
        if m:
            total += float(m.group(1).split()[8])

print(f"{total:.6e} kg")