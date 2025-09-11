# Emne 5 — Booleans (sand/falsk)

# Eksempel 1: Sammenligninger
print(7 > 3, 7 == 3, 7 != 3)

# Eksempel 2: Logiske operatorer
print(True and False, True or False, not False)

# Eksempel 3: Tjekke om liste er tom
ting = []
if not ting:
    print("listen er tom -> False")

# Eksempel 4: all/any
checks = [3 < 5, 10 == 10, "x" in "tekst"]
print("all:", all(checks), "| any:", any([False, 0, "", "hej"]))

# Eksempel 5: Kortslutning (short-circuit)
def side_effect():
    print("side_effect() blev kørt")
    return True
print("OR:", True or side_effect())
print("AND:", False and side_effect())


print("Daniel is super gay")