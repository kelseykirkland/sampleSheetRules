import numpy as np
import pandas as pd
from pathlib import Path
import datetime

# Rules for Sample Submission Sheet
# All return True is the rule is violated and should be flagged, otherwise False

def checkforspaces(val: str) -> bool:
    """
    this method checks for space characters
    :param val: string value of the row
    :return: False if there is no spaces, True if there is a space
    """
    if " " in val:
        print(f"Detected space character in {val}")
        return True
    return False

def disallowedchars(val: str, discharlist) -> bool:
    """
    this method check for any of the characters in the provided list
    :param val: string value of the row
    :param discharlist: list of characters to check for
    :return: False if none of the listed characters are there, True if there is character listed
    """
    for x in discharlist:
        if x in val:
            print(f"Detected disallowed character {x} in {val}")
            return True
    return False

def characterlimit(val: str) -> bool:
    """
    this method checks that val is under 20 characters
    :param val: string value of the row
    :return: False if val is 20 characters or under, True if it is over 20 characters
    """
    if len(val) > 20:
        print(f"Exceeded character length of 20 for {val}")
        return True
    return False

def picklist(val: str, picklistvalues) -> bool:
    """
    this method checks is the val is in the provided list of strings
    :param val: string value of the row
    :param picklistvalues: list of strings
    :return: False if val is in picklistvalues, True is val is not in the picklistvalues
    """
    if val not in picklistvalues:
        print(f"{val} is not one of the accepted values")
        return True
    return False

def checknumbertype(val: str, numtype: str) -> bool:
    """
    this method checks if a number is the right type, int or float
    :param val: string value of the row
    :param numtype: the expected type, int or float
    :return: True is the val is not the type given, False if it is the matching type
    """
    if isinstance(val, numtype):
        return False
    else:
        print(f"{val} should be a {numtype}")
        return True

def alluppercase(val: str) -> bool:
    """
    this method checks if every value in val is uppercase
    :param val: string value of the row
    :return: True if there is a non uppercase character, False if val is all uppercase
    """
    if val.isupper():
        return False
    else:
        print(f"{val} should be all uppercase letters")
        return True

def isDate(val: str) -> bool:
    """
    this method checks if val is a valid date in the proper format
    :param val: string value of the row
    :return: True if it is not in date format, False if val is a proper date
    """
    try:
        datetime.datetime.strptime(val, '%Y-%m-%d')
    except ValueError:
        #raise ValueError("Incorrect data format, should be YYYY-MM-DD")
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
    checkforspaces(row['Sample_ID'])
    disallowedchars(row['Sample_ID'], disCharList)
    characterlimit(row['Sample_ID'])

print("Doneski")