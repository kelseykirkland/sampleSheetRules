import pytest

# from sampleSheetRules import checkforspaces
from sampleSheetRules import checkforspaces, disallowedchars, characterlimit, picklist, checknumbertype, alluppercase, \
    wellformat, singleword


def test_checkforspaces():
    assert checkforspaces("Test Test")
    assert not checkforspaces("Test")


def test_disallowedchars():
    discharlist = ["#", "*", ".", "\\", "/", "[", "]", ":", ";", "|", "="]
    assert disallowedchars("hello#me", discharlist)

def test_characterlimit():
    assert characterlimit("abcdefghijklmnopqqrstuvwxyz")
    assert not characterlimit("abcde")


def test_picklist():
    picklistValues = ["A", "B", "C"]
    assert picklist("D", picklistValues)
    assert not picklist("B", picklistValues)


def test_checknumbertype():
    assert checknumbertype("1.2", "int")
    assert checknumbertype("2", "float")


def test_alluppercase():
    assert alluppercase("Test")
    assert not alluppercase("TEST")


def test_wellformat():
    assert wellformat("A033")
    assert wellformat("test")
    assert not wellformat("A01")


def test_singleword():
    assert singleword("Test for testing")
    assert singleword("Test123")
    assert singleword("test")
    assert not singleword("Test")
