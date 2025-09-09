# Emne 7 — Matematik i Python

import math

# Eksempel 1: kvadratrod og potens
print("sqrt(81):", math.sqrt(81), "| 2^10:", math.pow(2, 10))

# Eksempel 2: Gulv og loft (afrunding ned/op)
print("floor(3.9):", math.floor(5.2), "| ceil(3.1):", math.ceil(3.1))

# Eksempel 3: Trigonometriske funktioner (i grader)
vinkel = 30
rad = math.radians(vinkel)
print("sin(30°):", math.sin(rad), "| cos(30°):", math.cos(rad))

# Eksempel 4: Pythagoras/hypot
dx, dy = 3, 4
print("hypot(3,4):", math.hypot(dx, dy))

# Eksempel 5: Konstanter
print("pi:", math.pi, "| e:", math.e)
