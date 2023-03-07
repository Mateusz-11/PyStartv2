def calculate_bmi(height: float, weight: float) -> float:
    bmi = height / weight ** 2
    return round(bmi, 2)


def decription_bmi(bmi_score: float) -> str:
    # bmi_score = calculate_bmi(height, weight)
    if bmi_score < 16:
        return 'wygłodzenie'
    elif 16 <= bmi_score < 17:
        return 'wychudzenie'
    elif 17 <= bmi_score < 18.5:
        return 'niedowaga'
    elif 18.5 <= bmi_score < 25:
        return 'wartość prawidłowa'
    elif 25 <= bmi_score < 30:
        return 'nadwaga'
    elif 30 <= bmi_score < 35:
        return 'otyłość I stopnia'
    elif 35 <= bmi_score < 40:
        return 'oytłość II stopnia'
    elif 40 <= bmi_score:
        return 'skrajna otyłość'


def test_calculate_bmi():
    assert calculate_bmi(100, 2) == 25
    assert calculate_bmi(75, 1.7) == 25.95
    assert calculate_bmi(60, 2) == 15
    assert calculate_bmi(50, 2) == 12.5


def test_decription_bmi():
    assert decription_bmi(25) == 'nadwaga'
    assert decription_bmi(25.95) == 'nadwaga'
    assert decription_bmi(15) == 'wygłodzenie'
    assert decription_bmi(12.5) == 'wygłodzenie'


if __name__ == '__main__':
    weight = float(input('Text your weight: '))
    height = float(input('Text your height: '))
    bmi = calculate_bmi(weight, height)
    bmi_msg = decription_bmi(bmi)

    print(bmi)
    print(bmi_msg)
