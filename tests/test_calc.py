import pytest
from src.calc import Calc

def test_empty_string():
    assert Calc.add("") == 0

def test_single_number():
    assert Calc.add("1") == 1

def test_two_numbers():
    assert Calc.add("1,5") == 6

def test_multiple_numbers():
    assert Calc.add("1,2,3,4") == 10

