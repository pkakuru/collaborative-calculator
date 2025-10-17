import pytest
from calculator import get_numbers
from unittest.mock import patch


@patch("builtins.input", side_effect=["5", "ABC", "10", "done"])
def test_get_numbers_with_invalid_input(mock_input):
    expected_output = [5.0, 10.0]
    result = get_numbers()
    assert result == expected_output
