import random 
import time

# Definerer min class
class Pepsi:
    
    def __init__(self, taste: str, volume: str, material: str, kind: str,):
        self.taste = taste
        self.volume = volume
        self.material = material
        self.kind = kind
    
    # Debug Print mode #TODO: Lav highlight regel for ord "DEBUG"
    def __repr__(self) -> str:
        soda = self.__class__.__name__
        return (f"{soda} TASTE={self.taste!r}, VOLUME={self.volume!r},"
                f" MATERIAL={self.material!r}, KIND={self.kind!r}")
        
# Egenskaber flasken kan genereres fra
TASTE    = ["Pepsi", "Pepsi Max", "Pepsi Lime", "Pepsi Max twist"]

SMALL_VOLUMES = {"330ml", "500ml"}
LARGE_VOLUMES = {"1L", "1.5L", "2L"}

SMALL_BOTTLE_MATERIAL = {"Glass", "Plastic"}
LARGE_BOTTLE_MATERIAL = {"Plastic"}

# Laver og retunerer en tilfældig Pepsi
def generate_pepsi() -> Pepsi:
    vol = random.choice(list(SMALL_VOLUMES | LARGE_VOLUMES))
            
    if vol in LARGE_VOLUMES:
        # Store flasker er altid plastik
        kind = "Bottle"
        mat = "Plastic"
    else:
        # Flaske, Dåse eller Glass flaske 
        kind = random.choice(["Bottle", "Can"])
        if kind == "Can":
            mat = "Metal"
        else:
            mat = random.choice(list(SMALL_BOTTLE_MATERIAL))
    return Pepsi(
        taste=random.choice(TASTE),
        volume=vol,
        material=mat,
        kind=kind,
    )
    

    
#TODO: Tilføj kommentarer            
def arrivals(n: int = 5) -> None:
    for i in range(n):
        p = generate_pepsi() # <- Kalder "generate_pepsi" funktionen
        process_bottle(p)
        if (i + 1) % 5 == 0:
            print_status()
        time.sleep(0.5)
                


# Sorterings regler #TODO: SLET DICTIONARY BRUGES IKKE LÆNGERE
SORTING_BY_MAT_TYPE = {
    ("Glass", "Bottle"): "glass_bottle",
    ("Plastic", "Bottle"): "plastic_bottle",
    ("Metal", "Can"): "metal_can", 
}   

#TODO: Lav Kommentar
def pick_bin(p: Pepsi) -> str:
    match (p.material, p.kind):
        case ("Glass", "Bottle"):
            return "glass_bottle"
        case ("Plastic", "Bottle"):
            return "plastic_bottle"
        case ("Metal", "Can"):
            return "metal_can"
        case _:
            return "reject"
        
from collections import defaultdict
bin_counter: dict[str, int] = defaultdict(int)

#TODO: Lav Kommentar    
def process_bottle(p: Pepsi) -> None:
    b = pick_bin(p)
    bin_counter[b] += 1
    print(f"{p} -> {b}")

#TODO: Lav Kommentar    
def print_status() -> None:
    parts = [f"{k}:{bin_counter[k]}" for k in sorted(bin_counter)]
    print("Status", " | ".join(parts))

if __name__ == "__main__":
    arrivals(10)
    
    for _ in range(200):
        p = generate_pepsi()
        assert not (p.kind == "Can" and p.volume in {"1L","1.5L","2L"})
        assert not (p.volume in {"1L","1.5L","2L"} and p.material != "Plastic")
        assert not (p.kind == "Can" and p.material != "Metal")
    print("OK")