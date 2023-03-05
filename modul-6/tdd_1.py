import pytest


def get_dividors(a: int) -> set:
    dividors = set()
    for i in range(1, a + 1):
        if a % i == 0:
            dividors.add(i)
    return dividors


def great_common_divider(x: int, y: int) -> int:
    dividors1 = get_dividors(x)
    dividors2 = get_dividors(y)
    common_divisors = dividors1 & dividors2
    return max(common_divisors) if max(common_divisors) > 1 else None


@pytest.mark.parametrize("x_number,y_number,expected", [
    (10, 6, 2),
    (15, 5, 5),
    (24, 18, 6),
    (100, 75, 25),
    (20, 30, 10),
    (15, 30, 15),
])
def test_gcd_exists(x_number, y_number, expected):
    divider = great_common_divider(x_number, y_number)
    assert divider == expected


@pytest.mark.parametrize("x_number,y_number,expected", [
    (7, 30, None),
    (100, 9, None),
    (15, 4, None),
])
def test_gcd_doesnt_exists(x_number, y_number, expected):
    divider = great_common_divider(x_number, y_number)
    assert divider == expected


@pytest.mark.parametrize("a_number,expected", [
    (10, {1, 2, 5, 10}),
    (25, {1, 5, 25}),
])
def test_get_dividors(a_number, expected):
    divider = get_dividors(a_number, )
    assert divider == expected
