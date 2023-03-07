def check_pesel(pesel: str):
    CONTROL = '13791379131'

    if len(pesel) != 11:
        return False

    control_sum = 0
    for pesel_char, control_char in zip(pesel, CONTROL):
        control_sum += int(pesel_char) * int(control_char)

    if control_sum % 10 != 0:
        return False

    return True


def test_check_pesel_right():
    assert check_pesel('82012974188')
    assert check_pesel('06281074994')


def test_check_pesel_wrong():
    assert not check_pesel('123')
    assert not check_pesel('06283074994')
    assert not check_pesel('123789789456')
