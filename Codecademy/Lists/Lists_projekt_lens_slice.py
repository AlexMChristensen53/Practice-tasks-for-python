topping = ["pepperoni", "pineapple", "cheese", "sausage", "olives", "anchovies", "mushrooms"]
prices = [2, 6, 1, 3, 2, 7, 2]
num_two_dollar_slices = prices.count(2)
print(num_two_dollar_slices)
num_pizzas = len(prices)
print("We sell", num_pizzas, "different kinds of pizza!")

pizza_and_prices = [
    [prices[0], topping[0]],
    [prices[1], topping[1]],
    [prices[2], topping[2]],
    [prices[3], topping[3]],
    [prices[4], topping[4]],
    [prices[5], topping[5]],
    [prices[6], topping[6]],
]
print(pizza_and_prices)

pizza_and_prices.sort()
print(pizza_and_prices)
cheapest_pizza = pizza_and_prices[0]
priciest_pizza = pizza_and_prices[-1]

pizza_and_prices.pop(-1)
print(pizza_and_prices)
pizza_and_prices.insert(3, [2.5, "peppers"])
print(pizza_and_prices)
three_cheapest = pizza_and_prices[:3]

print(three_cheapest)
