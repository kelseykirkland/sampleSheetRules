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

# checks for disallowed in the value (the string) of row of the dataframe
# parameters is the list of values in the row and the list of disallowed characters
# returns False if the string does not contain a disallowed character
# returns True if the is a disallowed character and prints a statement
def disallowedChars(val, disCharList):
    for x in disCharList:
        if x in val:
            print(f"Detected disallowed character {x} in {val}")
            return True
    return False

# checks if value (the string) of row of the dataframe exceeds 20 characters
# returns False if the string is under or equal to 20 characters
# returns True if the string exceeds 20 characters prints a statement
def characterLimit(val):
    if len(val) > 20:
        print(f"Exceeded character length of 20 for {val}")
        return True
    return False

# checks for if the value (the string) of row of the dataframe is in the list of only possible values
# parameters is the list of values in the row and the list of accepted input
# returns False if the string is in the picklistValues
# returns True if the val is not in the list of accepted input
def picklist(val, picklistValues):
    if val not in picklistValues:
        print(f"{val} is not one of the accepted values")
        return True
    return False


#  Start
# Read in sample Sheet submission
print("START")
f = Path('/home/kelsey/Documents/SS_20200122_META_WGS_16S_M01308.csv')
# ss_df = pd.read_csv(f)
ss_df = pd.read_csv(str(f), skiprows=19)

disCharList = ["#", "*", ".", "\\", "/", "[", "]", ":", ";", "|", "="]   # need to do """
picklistValues= ["Salmonella", "VTEC", "Parasitology", "Botulism", "Listeria", "Vibrio", "Virology" "Rapid-Diagnostics", "Other"]

for i, row in ss_df.iterrows():
    checkForSpaces(row['Sample_ID'])
    disallowedChars(row['Sample_ID'], disCharList)
    characterLimit(row['Sample_ID'])



print("Doneski")