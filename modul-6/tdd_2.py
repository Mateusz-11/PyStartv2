import pytest


def create_list_of_numbers(n: int, m: int, z: int) -> list:
    result = []
    for i in range(n, m + 1):
        if i % z == 0:
            result.append(i)
    return result


@pytest.mark.parametrize("n_number,m_number, z_number,expected", [
    (6, 20, 2, [6, 8, 10, 12, 14, 16, 18, 20]),

])
def test_divider(n_number, m_number, z_number, expected):
    divider = create_list_of_numbers(n_number, m_number, z_number)
    assert divider == expected
