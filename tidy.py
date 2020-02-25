#!/usr/bin/env python3

import os
import sys

if len(sys.argv) != 2:
    print("Usage: python tidy.py \"C:\\...your extraction folder...\"")
    exit(1)

root_dir = sys.argv[1]

if not os.path.exists(root_dir):
    print("Cant find the extraction folder, are you sure you're using this correctly? Read the README.")
    exit(2)

main_path = os.path.join(root_dir, "Main")
second_impact_path = os.path.join(root_dir, "StreetFighterIII_2ndImpact")
third_strike_path = os.path.join(root_dir, "StreetFighterIII_3rdStrike")

main_files = os.listdir(main_path)
third_strike_files = os.listdir(third_strike_path)

# Move Second Impact music from Third Strike dir to Second Impact dir.
for filename in third_strike_files:
    if filename.startswith("SF3SI") and filename.endswith(".ogg"):
        print(filename)
        old = os.path.join(third_strike_path, filename)
        new = os.path.join(second_impact_path, filename)
        os.rename(old, new)

# Move Third Strike music from Main dir to Third Strike dir.
for filename in main_files:
    if filename.startswith("SF3TS") and filename.endswith(".ogg"):
        print(filename)
        old = os.path.join(main_path, filename)
        new = os.path.join(third_strike_path, filename)
        os.rename(old, new)
