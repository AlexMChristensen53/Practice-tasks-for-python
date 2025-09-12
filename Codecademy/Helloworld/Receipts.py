lovely_loveseat_description = (
    "Lovely Loveseat."
    "\n"
    "Tufted polyester blend on wood."
    "\n"
    "32 inches high x 40 inches wide x 30 inches deep."
    "\n"
    "Red or white."
    "\n"
)
lovely_loveseat_price = 254.00
stylish_settee_description = (
    "Stylish Settee."
    "\n"
    "Faux leather on birch."
    "\n"
    "29.50 inches high x 54.75 inches wide x 28 inches deep."
    "\n"
    "Black."
    "\n"
)
stylish_settee_price = 180.5
luxurious_lamp_description = (
    "Luxurious Lamp."
    "\n"
    "Glass and iron."
    "\n"
    "36 inches tall."
    "\n"
    "Brown with cream shade."
    "\n"
)
luxurious_lamp_price = 52.15
sales_tax = 0.088

customer_one_total = 0
customer_one_itemization = ""


customer_one_itemization += lovely_loveseat_description + "\n" + luxurious_lamp_description
customer_one_total += lovely_loveseat_price + luxurious_lamp_price
customer_one_tax = customer_one_total * sales_tax
customer_one_total += customer_one_tax
print("Customer One Items:" "\n")
print(customer_one_itemization)
print("Customer One Total:")
print(f"{customer_one_total:.2f}")
