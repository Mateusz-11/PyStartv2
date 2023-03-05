import pytest


def create_list_of_numbers(n: int, m: int, z: int) -> list:
    result = []
    for i in range(n, m + 1):
        if i % z == 0:
            result.append(i)

    return result


@pytest.mark.parametrize("n_number,m_number, z_number,expected", [
    (6, 20, 2, [6, 8, 10, 12, 14, 16, 18, 20]),
    (2, 10, 2, [2, 4, 6, 8, 10]),
    (2, 10, 30, []),
    (3, 12, 2, [4, 6, 8, 10, 12]),

])
def test_divider(n_number, m_number, z_number, expected):
    divider = create_list_of_numbers(n_number, m_number, z_number)
    assert divider == expected
    assert isinstance(create_list_of_numbers(n_number, m_number, z_number), list)
