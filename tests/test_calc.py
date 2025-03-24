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

def test_new_line_delimiter():
    assert Calc.add("1\n2,3") == 6

def test_custom_delimiter():
    assert Calc.add("//;\n1;2") == 3

def test_negative_number():
    with pytest.raises(ValueError, match="negative numbers not allowed: -3"):
        Calc.add("1,-3")

def test_multiple_negative_numbers():
    with pytest.raises(ValueError, match="negative numbers not allowed: -3,-5"):
        Calc.add("1,-3,2,-5")