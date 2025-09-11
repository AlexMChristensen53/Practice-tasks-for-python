import random 
import time

# Definerer min class
class Pepsi:
    
    def __init__(self, taste: str, volume: str, material: str, kind: str,):
        self.taste = taste
        self.volume = volume
        self.material = material
        self.kind = kind
    
    # Debug Print mode
    def __repr__(self) -> str:
        soda = self.__class__.__name__
        return (f"{soda}TASTES={self.taste!r}, VOLUMES={self.volume!r},"
                f"MATERIALS={self.material!r}, kinds={self.kind!r}")
        
# Egenskaber flasken kan genereres fra
TASTES    = ["Pepsi", "Pepsi Max", "Pepsi Lime", "Pepsi Max twist"]

SMALL_VOLUMES = {"330ml", "500ml"}
LARGE_VOLUMES = {"1L", "1.5L", "2L"}

CAN_MATERIAL = {"Metal"}
SMALL_BOTTLE_MATERIAL = {"Glass", "Plastic"}
LARGE_BOTTLE_MATERIAL = {"Plastic"}

# Laver og retunerer en tilfældig Pepsi
def generate_Pepsi() -> Pepsi:
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
        taste=random.choice(TASTES),
        volume=vol,
        material=mat,
        kind=kind,
    )
        
def arrivals(n: int = 5) -> None:
    for _ in range(n):
        p = generate_Pepsi() # <- Kalder "generate_Pepsi" funktionen
        print(p)
        time.sleep(0.5)
        
if __name__ == "__main__":
    arrivals(3)
    
for _ in range(200):
    p = generate_Pepsi()
    assert not (p.kind == "Can" and p.volume in {"1L","1.5L","2L"})
    assert not (p.volume in {"1L","1.5L","2L"} and p.material != "Plastic")
    assert not (p.kind == "Can" and p.material != "Metal")
print("OK")

# Sorterings regler
SORTING_BY_MAT_TYPE = {
    ("Glass", "Bottle"): "glass_bottle",
    ("Plastic", "Bottle"): "plastic_bottle",
    ("Metal", "Can"): "metal_can", 
}   

def pick_bin(p: Pepsi) -> str:
    match (p.material, p.kind):
        case ("Glass", "Bottle"):
            return "glass_bottle"
        case ("Plastic", "Bottle"):
            return "plastic_bottle"
        case ("Metal", "Can"):
            return "metal_can"
        case _:
            return "Weirdo"