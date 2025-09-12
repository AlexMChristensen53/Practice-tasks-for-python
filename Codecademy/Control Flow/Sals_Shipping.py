weight = float(input("Enter the weight of the package: "))
drone_flat_charge = 0
ground_flat_charge = 20
price_per_pound = 0

# Ground Shipping
if weight <= 2:
    price_per_pound = 1.5
    ground_cost = ground_flat_charge + weight * price_per_pound
    print(f"The price is {ground_cost:.2f}$ for ground shipping")
elif weight > 2 and weight <= 6:
    price_per_pound = 3.0
    ground_cost = ground_flat_charge + weight * price_per_pound
    print(f"The price is {ground_cost:.2f}$ for ground shipping")
elif weight > 6 and weight <= 10:
    price_per_pound = 4.0
    ground_cost = ground_flat_charge + weight * price_per_pound
    print(f"The price is {ground_cost:.2f}$ for ground shipping")
elif weight > 10:
    price_per_pound = 4.75
    ground_cost = ground_flat_charge + weight * price_per_pound
    print(f"The price is {ground_cost:.2f}$ for ground shipping")

# Ground Shipping PREMIUM!
ground_shipping_premium = 125
print(f"The price is {ground_shipping_premium}$ for premium shipping")

# Drone Shipping
if weight <= 2:
    price_per_pound = 4.50
    drone_cost = drone_flat_charge + weight * price_per_pound
    print(f"The price is {drone_cost:.2f}$ for drone shipping")
elif weight > 2 and weight <= 6:
    price_per_pound = 9.00
    drone_cost = drone_flat_charge + weight * price_per_pound
    print(f"The price is {drone_cost:.2f}$ for drone shipping")
elif weight > 6 and weight <= 10:
    price_per_pound = 12.00
    drone_cost = drone_flat_charge + weight * price_per_pound
    print(f"The price is {drone_cost:.2f}$ for drone shipping")
elif weight > 10:
    price_per_pound = 14.25
    drone_cost = drone_flat_charge + weight * price_per_pound
    print(f"The price is {drone_cost:.2f}$ for drone shipping")

cheapest_option = min(ground_cost, ground_shipping_premium, drone_cost)
if cheapest_option == ground_cost:
    print(f"Ground Shipping is cheapest: {ground_cost:.2f}$")
elif cheapest_option == ground_shipping_premium:
    print(f"Premium Shipping is cheapest: {ground_shipping_premium:.2f}$")
elif cheapest_option == drone_cost:
    print(f"Drone Shipping is cheapest: {drone_cost:.2f}$")
