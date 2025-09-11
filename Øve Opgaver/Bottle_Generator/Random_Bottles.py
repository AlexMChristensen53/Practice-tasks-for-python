import random 
import time
import csv, os
from datetime import datetime

#TODO: Tilføj kommentar
CSV_PATH = "sorting_log.csv"
FIELDNAMES = ["timestamp", "taste", "volume", "material", "container", "bin"]

# Egenskaber flasken kan genereres fra
TASTE    = ["Cola", "Lime", "twist"]

SMALL_VOLUMES = {"330ml", "500ml"}
LARGE_VOLUMES = {"1L", "1.5L", "2L"}

SMALL_BOTTLE_MATERIAL = {"Glass", "Plastic"}
LARGE_BOTTLE_MATERIAL = {"Plastic"}


# Definerer min class
class Pepsi:
    
    def __init__(self, taste: str, volume: str, material: str, container: str,):
        self.taste = taste
        self.volume = volume
        self.material = material
        self.container = container
    
    # Debug Print mode #TODO: Lav highlight regel for ord "DEBUG"
    def __repr__(self) -> str:
        soda = self.__class__.__name__
        return (f"{soda} TASTE={self.taste!r}, VOLUME={self.volume!r},"
                f" MATERIAL={self.material!r}, KIND={self.container!r}")
        


# Laver og retunerer en tilfældig Pepsi
def generate_pepsi() -> Pepsi:
    vol = random.choice(list(SMALL_VOLUMES | LARGE_VOLUMES))
            
    if vol in LARGE_VOLUMES:
        # Store flasker er altid plastik
        container = "Bottle"
        mat = "Plastic"
    else:
        # Flaske, Dåse eller Glass flaske 
        container = random.choice(["Bottle", "Can"])
        if container == "Can":
            mat = "Metal"
        else:
            mat = random.choice(list(SMALL_BOTTLE_MATERIAL))
    return Pepsi(
        taste=random.choice(TASTE),
        volume=vol,
        material=mat,
        container=container,
    )
    

    
#TODO: Tilføj kommentarer            
def arrivals(n: int = 5) -> None:
    for _ in range(n):
        p = generate_pepsi() # <- Kalder "generate_pepsi" funktionen
        process_bottle(p)
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
    match (p.material, p.container):
        case ("Glass", "Bottle"):
            return "glass_bottle"
        case ("Plastic", "Bottle"):
            return "plastic_bottle"
        case ("Metal", "Can"):
            return "metal_can"
        case _:
            return "reject"

from collections import defaultdict
bin_counter: defaultdict[str, int] = defaultdict(int)

#TODO: Lav Kommentar    
def process_bottle(p: Pepsi) -> None:
    b = pick_bin(p)
    bin_counter[b] += 1
    print(f"{p} -> {b}")
    log_to_csv(p, b)

#TODO: Lav Kommentar    
def print_status() -> None:
    parts = [f"{k}:{bin_counter[k]}" for k in sorted(bin_counter)]
    print("Status", " | ".join(parts))
    
def init_csv(path: str = CSV_PATH) -> None:
    #TODO: lav kommentar
    needs_header = not os.path.exists(path)
    with open(path, "a", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=FIELDNAMES)
        if needs_header:
            w.writeheader()
            
def log_to_csv(p: Pepsi, bin_name: str, path: str = CSV_PATH) -> None:
    with open(path, "a", newline="", encoding="utf-8") as f:
         w = csv.DictWriter(f, fieldnames=FIELDNAMES)
         w.writerow({
            "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "taste": p.taste,
            "volume": p.volume,
            "material": p.material,
            "container": p.container,
            "bin": bin_name,
        })

if __name__ == "__main__":
    init_csv()
    arrivals(10)
    
    for _ in range(200):
        p = generate_pepsi()
        assert not (p.container == "Can" and p.volume in {"1L","1.5L","2L"})
        assert not (p.volume in {"1L","1.5L","2L"} and p.material != "Plastic")
        assert not (p.container == "Can" and p.material != "Metal")
    print("OK")