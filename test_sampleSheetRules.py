import pytest

# from sampleSheetRules import checkforspaces
from sampleSheetRules import checkforspaces, disallowedchars


def test_checkforspaces():
    assert checkforspaces("Hello Me")


def test_disallowedchars():
    discharlist = ["#", "*", ".", "\\", "/", "[", "]", ":", ";", "|", "="]
    assert disallowedchars("hello#me", discharlist)
