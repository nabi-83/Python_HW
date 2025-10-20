import pytest
from string_utils import StringUtils


string_utils = StringUtils()


@pytest.mark.positive
@pytest.mark.parametrize("input_str, expected", [
    ("skypro", "Skypro"),
    ("hello world", "Hello world"),
    ("python", "Python"),
])
def test_capitalize_positive(input_str, expected):
    assert string_utils.capitalize(input_str) == expected


@pytest.mark.negative
@pytest.mark.parametrize("input_str, expected", [
    ("123abc", "123abc"),
    ("", ""),
    ("   ", "   "),
])
def test_capitalize_negative(input_str, expected):
    assert string_utils.capitalize(input_str) == expected


#Позитивный тест - символ
@pytest.mark.parametrize("input_str, symbol1", [
    ("Skypro", "y"),
    ("Тест", "т"),
    ("04 апреля 2023", "2"),
])
def test_contains_positive(input_str, symbol1):
    assert string_utils.contains(input_str, symbol1) == True

#Негативный тест - символ
@pytest.mark.parametrize("input_str, symbol1", [
    ("123abc", "Y"),
    ("Тест", " "),
    ("04 апреля 2023", "1")
])
def test_contains_negative(input_str, symbol1):
    assert string_utils.contains(input_str, symbol1) == False
