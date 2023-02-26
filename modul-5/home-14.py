def validate_pin(pin_number:str) -> bool:
    if not len(pin_number) == 4:
        return False
    for i in pin_number:
        if not i.isdigit():
            return False
    return True


print(validate_pin('1234'))
print(validate_pin('1s34'))
print(validate_pin('1!34'))
print(validate_pin('12234'))
print(validate_pin('134'))