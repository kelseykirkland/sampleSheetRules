import numpy as np
import pandas as pd
from pathlib import Path

# checks for spaces in the value (the string) of the row of the dataframe
# returns False if there is no space characters
# returns True if the is a space character and prints a statement
def checkForSpaces(val):
    if " " in val:
        print(f"Detected space character in {val}")
        return True
    return False

def disallowedChars(val):
    if "#" in val:
        print(f"Detected disallowed character in {val}")
        return True
    return False

# checks for spaces in the value (the string) of row of the dataframe
# returns False if its
# returns True if the is a space character and prints a statement
def characterLimit(val):
    if len(val) > 20:
        print(f"Exceeded character length of 20 for {val}")
        return True
    return False

#  Start
# Read in sample Sheet submission
print("START")
f = Path('/home/kelsey/Documents/SS_20200122_META_WGS_16S_M01308.csv')
# ss_df = pd.read_csv(f)
ss_df = pd.read_csv(str(f), skiprows=19)

for i, row in ss_df.iterrows():
    checkForSpaces(row['Sample_ID'])

print("Doneski")