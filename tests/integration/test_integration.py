import pytest
import math
from MyLib.add import add
from MyLib.multiply import multiply


def test_add_then_multiply_basic():
    assert multiply(add(2, 3), 4) == 20


def test_multiply_then_add_basic():
    assert add(2, multiply(3, 4)) == 14


def test_nested_operations():
    assert multiply(add(1, 2), add(3, 4)) == 21


def test_distributive_property():
    a, b, c = 2, 3, 4
    left = multiply(a, add(b, c))         # a*(b + c)
    right = add(multiply(a, b), multiply(a, c))  # a*b + a*c
    assert left == right


def test_chain_operations():
    result = add(multiply(2, 3), multiply(4, 5))  # 6 + 20 = 26
    assert result == 26

    result = multiply(add(1.1, 2.2), add(3.3, 4.4))  # ~3.3 * 7.7 = 25.41
    assert result == pytest.approx(25.41)


def test_extreme_values():
    large = 1e308
    assert add(large, large) == float("inf")
    assert multiply(large, 1) == large
    assert multiply(large, 10) == float("inf")


def test_nan_and_infinity_propagation():
    assert math.isnan(multiply(add(float("nan"), 1), 2))
    assert multiply(float("inf"), add(1, 1)) == float("inf")
    assert math.isnan(add(multiply(1e308, 10), -float("inf")))


def test_invalid_combinations():
    with pytest.raises(TypeError):
        multiply(add("a", "b"), 5)

    with pytest.raises(TypeError):
        add(multiply(2, [1, 2]), 3)

    with pytest.raises(TypeError):
        multiply(add(True, {}), 5)


def test_boolean_chaining():
    assert multiply(add(True, 2), 3) == 9  # (1 + 2) * 3
    assert add(multiply(False, 10), 7) == 7  # (0 * 10) + 7
