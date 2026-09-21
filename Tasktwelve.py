
driving_dist = float(input('enter driving dist: '))
miles_gallon = float(input('enter miles per gallon: '))
price_gallon = float(input('enter price per gallon: '))

driving_cost = (driving_dist / miles_gallon) * price_gallon

print("Your total driving cost is =", driving_cost)
