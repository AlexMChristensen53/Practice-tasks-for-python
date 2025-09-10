# Emne 6 — Operatorer

# Eksempel 1: Aritmetik og tildeling
n = 5
n += 3   # nu 8
n *= 2   # nu 16
print("n efter += og *=:", n)

# Eksempel 2: Sammenligning
print(3 < 5, 5 <= 5, 7 >= 10, 4 == 4, 4 != 5)

# Eksempel 3: Medlemskab
print("'py' i 'python'?", "py" in "python", "| 2 i [1,2,3]?", 2 in [1,2,3])

# Eksempel 4: Identitet vs lighed
a = [1,2,3]
b = [1,2,3]
c = a
print("a==b:", a == b, "| a is b:", a is b, "| a is c:", a is c)

# Eksempel 5: Bitvise operatorer (bruges mest til lav-niveau ting)
print("5 & 3:", 5 & 3, "| 5 | 3:", 5 | 3, "| 5 ^ 3:", 5 ^ 3, "| 5<<1:", 5<<1, "| 5>>1:", 5>>1)
