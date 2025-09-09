# Emne 1 — Python Datatyper

# Eksempel 1: Helt simple typer
a_int = 42
a_float = 3.14
a_str = "hej"
a_bool = True
print(type(a_int), type(a_float), type(a_str), type(a_bool))

# Eksempel 2: Lister, tuples, sets og dicts
a_list = [1, 2, 3]
a_tuple = (4, 5, 6)
a_set = {1, 1, 2, 3}     # et set fjerner dubletter -> {1,2,3}
a_dict = {"navn": "Alex", "alder": 23}
print(a_list, a_tuple, a_set, a_dict)

# Eksempel 3: Lister kan ændres, tuples kan ikke
a_list.append(4)
print("Liste efter append:", a_list)

# Eksempel 4: None er "ingenting"
nothing = None
print("Er nothing None?", nothing is None)

# Eksempel 5: Tjekke om et objekt har længde
def safe_len(obj):
    return len(obj) if hasattr(obj, "__len__") else 0
print("safe_len på liste:", safe_len([1,2,3]), "| safe_len på 10:", safe_len(10))
