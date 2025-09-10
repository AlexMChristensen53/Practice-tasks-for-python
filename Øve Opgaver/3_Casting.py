# Emne 3 — Casting (ændre datatype)

# Eksempel 1: str -> int/float
s_num = "42"
print(int(s_num), float(s_num))

# Eksempel 2: float -> int (den skærer decimalerne væk)
print("int(3.99):", int(3.99), "| int(-3.99):", int(-3.99))

# Eksempel 3: alt -> str (tekst)
pi = 3.14159
print("til streng:", str(pi))

# Eksempel 4: streng -> liste/tuple
word = "python"
print(list(word), tuple(word))

# Eksempel 5: til bool (sand/falsk)
print(bool(0), bool(1), bool(""), bool("ok"), bool([]), bool([0]))
