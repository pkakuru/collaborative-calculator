import pytest
from calculator import get_numbers, add_numbers, multiply_numbers
from unittest.mock import patch


@patch("builtins.input", side_effect=["5", "ABC", "10", "done"])
def test_get_numbers_with_invalid_input(mock_input):
    expected_output = [5.0, 10.0]
    result = get_numbers()
    assert result == expected_output


def test_add_positive_numbers():
    numbers = [1, 2, 3, 4.5]
    expected_sum = 10.5
    assert add_numbers(numbers) == expected_sum


def test_multiply_positive_numbers():
    numbers = [1, 2, 3, 4]
    expected_product = 24
    assert multiply_numbers(numbers) == expected_product
