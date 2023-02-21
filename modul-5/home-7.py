miles = 1.609344


def conversion_miles_km(m: float) -> float:
    return m * miles


def conversion_km_miles(km: float) -> float:
    return km / miles


print(conversion_miles_km(10))
print(conversion_km_miles(16))
