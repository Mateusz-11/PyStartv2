def calculate_cost_of_electricity(time: float, cost: float = 0.617) -> float:
    """
    This function calculates the cost of electricity for working machine.
    :param time: Time of working machine in hours
    :param cost: price of electricity for 1 kWh. Default price = 0.617
    :return: Total spent on electricity
    """
    return round((time * cost), 2)


print(calculate_cost_of_electricity(1))
print(calculate_cost_of_electricity(10))
print(calculate_cost_of_electricity(1000))

calculate_cost_of_electricity(1)
