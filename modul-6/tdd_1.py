import pytest


def most_common_divider(x: int, y: int) -> int:
    ar1 = []
    ar2 = []
    for i in range(1, x):
        if x % i == 0:
            ar1.append(i)
    for i in range(1, y):
        if y % i == 0:
            ar2.append(i)
    ar_tmp = set(ar1) & set(ar2)
    return max(ar_tmp)


@pytest.mark.parametrize("x_number,y_number,expected", [
    (10, 6, 2),
    (15, 5, 5),
    (15, 4, None),
    (24, 18, 6),
    (100, 75, 25),
    (100, 9, None),
])
def test_divider(x_number, y_number, expected):
    divider = most_common_divider(x_number, y_number)
    assert divider == expected
