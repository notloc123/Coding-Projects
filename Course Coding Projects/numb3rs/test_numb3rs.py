from numb3rs import validate
import pytest

def main():
    test_format()
    test_range()

def test_format():
    assert validate(r"1.0.0.0") == True
    assert validate(r"1.0.0") == False
    assert validate(r"1.0") == False
    assert validate(r"1") == False

def test_range():
    assert validate(r"255.255.255.255") == True
    assert validate(r"0.0.0.0") == True
    assert validate(r"256.255.255.255") == False
    assert validate(r"255.256.255.255") == False
    assert validate(r"255.255.256.255") == False
    assert validate(r"255.255.255.256") == False
