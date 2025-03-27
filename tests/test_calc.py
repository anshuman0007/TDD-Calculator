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

def test_ignore_numbers_greater_than_1000():
    """Numbers greater than 1000 should be ignored"""
    assert Calc.add("2,1001") == 2
    assert Calc.add("1000,1") == 1001  

def test_multiple_character_delimiter():
    """Supports multi-character delimiter like //[***]\\n1***2***3"""
    assert Calc.add("//[***]\n1***2***3") == 6

def test_multiple_delimiters():
    """Supports multiple delimiters like //[*][%]\\n1*2%3"""
    assert Calc.add("//[*][%]\n1*2%3") == 6

def test_pipe_delimiters():
    assert Calc.add("3,|,4")==7