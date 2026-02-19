import pytest
from app import calculate_area, greet_user, is_adult, get_config, add_numbers, Calculator


def test_calculate_area():
    result = calculate_area(5)
    assert abs(result - 78.539) < 0.01


def test_greet_user():
    result = greet_user("Alice")
    assert "Alice" in result
    assert "30" in result


def test_is_adult_true():
    assert is_adult(20) == True  # Will FAIL due to logic bug


def test_is_adult_false():
    assert is_adult(15) == False  # Will FAIL due to logic bug


def test_add_numbers():
    assert add_numbers(3, 4) == 7


def test_divide_normal():
    calc = Calculator()
    assert calc.divide(10, 2) == 5.0


def test_divide_by_zero():
    calc = Calculator()
    with pytest.raises(ZeroDivisionError):
        calc.divide(5, 0)


def test_square_root():
    calc = Calculator()
    assert calc.square_root(16) == 4.0
