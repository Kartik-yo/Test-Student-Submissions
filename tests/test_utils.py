import pytest
from app.utils import add_numbers

def test_add_numbers():
    # Test case 1: Positive numbers
    assert add_numbers(2, 3) == 5

    # Test case 2: Negative numbers
    assert add_numbers(-1, -1) == -2

    # Test case 3: Mixed numbers
    assert add_numbers(-1, 1) == 0

    # Test case 4: Zero
    assert add_numbers(0, 0) == 0
