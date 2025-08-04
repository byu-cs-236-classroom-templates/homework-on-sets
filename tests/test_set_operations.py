# tests/test_set_operations.py
from homework1.set_operations import union, intersection, cartesian_product

def test_union_positive():
    assert union({1, 2}, {2, 3}) == {1, 2, 3}

def test_union_negative():
    assert union({1}, {2}) != {1}

def test_intersection_positive():
    assert intersection({1, 2}, {2, 3}) == {2}

def test_intersection_negative():
    assert intersection({1, 2}, {3, 4}) == set()

def test_cartesian_product_positive():
    a = {1, 2}
    b = {'a', 'b'}
    expected = {(1, 'a'), (1, 'b'), (2, 'a'), (2, 'b')}
    assert cartesian_product(a, b) == expected

def test_cartesian_product_negative():
    assert cartesian_product({1}, {2}) != {(1, 1)}
