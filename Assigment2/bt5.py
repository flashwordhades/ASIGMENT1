import math
def pizza_unit_price_per_square(diameter_cm, price):
    radius_m = (diameter_cm / 100) / 2
    area = math.pi * radius_m ** 2
    return price / area
def caculate_pizzas_price():
    d1 = float(input("Enter diameter of pizza 1 (cm): "))
    p1 = float(input("Enter price of pizza 1 (USD): "))
    d2 = float(input("Enter diameter of pizza 2 (cm): "))
    p2 = float(input("Enter price of pizza 2 (USD): "))
    unit1 = pizza_unit_price_per_square(d1, p1)
    unit2 = pizza_unit_price_per_square(d2, p2)
    if unit1 < unit2:
        print("Pizza 1 is better value for money.")
    elif unit2 < unit1:
        print("Pizza 2 is better value for money.")
    else:
        print("Both pizzas provide the same value.")
caculate_pizzas_price()