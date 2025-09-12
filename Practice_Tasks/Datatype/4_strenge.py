# Emne 4 — Python Strenge

# Eksempel 1: Slicing (tage udsnit)
s = "Python er sjovt"
print("første 6 tegn:", s[0:6], "| sidste 3:", s[-3:])

# Eksempel 2: Almindelige metoder
print("upper:", s.upper(), "| replace:", s.replace("sjovt", "sejt"))

# Eksempel 3: f-strings (indsætte værdier i tekst)
navn, point = "Alex", 97.3
print(f"{navn} fik {point:.1f} point")

# Eksempel 4: split og join
ordene = s.split()                 # ["Python","er","sjovt"]
sammen = "-".join(ordene)          # "Python-er-sjovt"
print(ordene, "|", sammen)

# Eksempel 5: finde tekst
print("find 'er':", s.find("er"), "| indeholder 'sjovt'?", "sjovt" in s)
