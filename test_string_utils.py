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

#позитивный тест - удаление подстроки
@pytest.mark.parametrize("string, symbol, expected_result", [
    ("Тест", "е", "Тст"),
    ("123abc", "3", "12abc")
    ])
def test_delete_symbol(string, symbol, expected_result):
    assert string_utils.delete_symbol(string, symbol) == expected_result

#негативный тест - удаление подстроки
@pytest.mark.parametrize("string, symbol, expected_result", [
    ("123abc", "5", "123abc")
    ])
def test_delete_symbol(string, symbol, expected_result):
    assert string_utils.delete_symbol(string, symbol) == expected_result

#позитивный тест - удаление пробела в начале, если они есть
@pytest.mark.parametrize("string, whitespace", [
    ("   Skypro", "Skypro"),
    ("   Тест", "Тест"),
    ])
def test_trim_positive(string, whitespace):
    assert string_utils.trim(whitespace) == whitespace

#негативный тест - удаление пробела в начале, если они есть
@pytest.mark.parametrize("string, whitespace", [
    ("Skypro", "Skypro"),
    ("Тест", "Тест"),
    ])
def test_trim_negative(string, whitespace):
    assert string_utils.trim(whitespace) == whitespace
