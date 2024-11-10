# test_calculator.py

import pytest
from calculator import add, subtract, multiply, divide


def test_add_basic():
    assert add(1, 2) == 3
    assert add(-1, 1) == 0

def test_add_zero():
    assert add(0, 0) == 0
    assert add(-1, -1) == -2

def test_add_floats():
    assert add(1.5, 2.5) == 4.0

def test_add_large_numbers():
    assert add(1000, 2000) == 3000


def test_subtract_basic():
    assert subtract(5, 2) == 3
    assert subtract(-1, -1) == 0

def test_subtract_zero():
    assert subtract(0, 1) == -1
    assert subtract(1, 0) == 1

def test_subtract_floats():
    assert subtract(3.5, 1.5) == 2.0

def test_subtract_large_numbers():
    assert subtract(100, 50) == 50

def test_multiply_basic():
    assert multiply(3, 4) == 12
    assert multiply(-1, 5) == -5

def test_multiply_zero():
    assert multiply(0, 10) == 0
    assert multiply(-2, -2) == 4

def test_multiply_floats():
    assert multiply(2.5, 4) == 10.0

def test_multiply_large_numbers():
    assert multiply(100, 0) == 0


def test_divide_basic():
    assert divide(6, 3) == 2
    assert divide(-6, 3) == -2

def test_divide_zero():
    assert divide(0, 1) == 0
    assert divide(5, 2) == 2.5
    with pytest.raises(ValueError, match="Cannot divide by zero."):
        divide(1, 0)

def test_divide_floats():
    assert divide(5.0, 2.0) == 2.5

def test_divide_large_numbers():
    assert divide(100, 25) == 4
    assert divide(-100, -25) == 4


def test_divide_invalid_inputs():
    with pytest.raises(ValueError, match="Inputs must be numbers."):
        divide("a", 1)
    with pytest.raises(ValueError, match="Inputs must be numbers."):
        divide(1, "b")
    with pytest.raises(ValueError, match="Inputs must be numbers."):
        divide("a", "b")
