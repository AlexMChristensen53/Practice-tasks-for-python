import csv
import random
import time
import msvcrt
from collections import defaultdict
from datetime import datetime
from pathlib import Path

""" CSV layout, per batch header, per flaske række, per batch total. Live keys bruger msvcrt (Virker kun på windows) 
    Generer tilfældige pepsi elementer, der bliver sorteret i forskellige kasser"""

# Konstanter jeg bruger til at håndtere min log.
BASE_DIR = Path(__file__).resolve().parent
CSV_PATH = BASE_DIR / "sorting_log.csv"
FIELDNAMES = ["timestamp", "brand", "taste", "volume", "material", "container", "bin"]

# Egenskaber flasken kan genereres fra.
TASTE = ["Cola", "Lime", "twist"]

SMALL_VOLUMES = {"330ml", "500ml"}
LARGE_VOLUMES = {"1L", "1.5L", "2L"}

SMALL_BOTTLE_MATERIAL = {"Glass", "Plastic"}
LARGE_BOTTLE_MATERIAL = {"Plastic"}


current_batch = 0

bin_counter: defaultdict[str, int] = defaultdict(int)


def init_csv(path: Path = CSV_PATH) -> None:
    """Sikre at filen "sorting_log.csv" eksisterer ellers laver den en ny tom .csv fil"""
    path.parent.mkdir(parents=True, exist_ok=True)
    path.touch(exist_ok=True)


def start_new_batch(path: Path = CSV_PATH) -> None:
    """Tæller +1 til "current_batch" hver gang mit program har kørt et loop færdigt eller det er blevet stoppet"""
    global current_batch, bin_counter
    current_batch += 1
    bin_counter.clear()  # <- rydder min tæller så den kan starte fra 0, i det nye batch.
    with path.open("a", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        w.writerow([])  # Blank linje til at springe en kolonne over.
        w.writerow([f"BATCH {current_batch}", datetime.now().strftime("%Y-%m-%d %H:%M:%S")])
        w.writerow([])  # Blank linje til at springe en kolonne over.
        w.writerow(FIELDNAMES)


def end_current_batch(path: Path = CSV_PATH) -> None:
    """Tilføjer et summary til slut i sorting_log.csv og viser total for hver kasse"""
    bins = ["glass_bottle", "plastic_bottle", "metal_can", "rejected_bottle"]
    counts = [bin_counter.get(b, 0) for b in bins]
    total = sum(counts)
    with path.open("a", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        w.writerow([])
        w.writerow(bins + ["total"])
        w.writerow(counts + [total])


class Pepsi:
    """Definerer min class Pepsi"""

    def __init__(
        self,
        taste: str,
        volume: str,
        material: str,
        container: str,
    ):
        self.taste = taste
        self.volume = volume
        self.material = material
        self.container = container

    def __repr__(self) -> str:
        """Printer en tilfældigt genereret pepsi med '' rundt om ord den har taget fra lister

        Returns:
            str: Pepsi TASTE='Lime' VOLUME='330ml' MATERIAL='Metal' CONTAINER='Can'
        """
        soda = self.__class__.__name__
        return (
            f"{soda} TASTE={self.taste!r}, VOLUME={self.volume!r},"
            f" MATERIAL={self.material!r}, CONTAINER={self.container!r}"
        )

    def __str__(self) -> str:
        """Printer den tilfældigt genereret pepsi med egenskaber separeret med " | "

        Returns:
            str: Pepsi | Lime | 330ml | Metal | Can
        """
        parts = [
            self.__class__.__name__,
            self.taste,
            self.volume,
            self.material,
            self.container,
        ]
        return " | ".join(parts)


def generate_pepsi() -> Pepsi:
    """Generer én tilfældig Pepsi.

    Regler:
     Store volumener (1L, 1.5L 2L) -> er altid plastik flasker.
     "Can" -> er altid Metal og aldrig stor volumen.
     Smag vælges fra TASTE.

    Returns:
        Pepsi: Et tilfældigt Pepsi objekt.
    """
    vol = random.choice(list(SMALL_VOLUMES | LARGE_VOLUMES))

    if vol in LARGE_VOLUMES:
        # Store flasker er altid plastik.
        container = "Bottle"
        mat = "Plastic"
    else:
        # Flaske, Dåse eller Glasflaske.
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


def run_batch(count: int) -> None:
    """kører et sorterings batch med 'count' flasker.

    Under batchen kan brugeren trykke:
        f - Simulerer ét fejlprodukt i form af "Pilk"
        s - Stopper batchet og vender tilbage til menuen
        a - Afslutter programmet

    Args:
        count (int): Antal maksimale flasker der behandles i dette batch.

    Raises:
        ValueError: Hvis 'count' <=0
        SystemExit: Hvis brugeren trykker "a" under batch
    """
    if count <= 0:
        raise ValueError("Please enter a positive number")
    start_new_batch()  # <- Kalder min funktion til at starte et nyt batch, således dette vises i min csv fil som "BATCH x".
    try:
        for _ in range(count):
            injected = False  # sætter injected til "false" for hvert loop, bruges til at generer en "pilk".

            if msvcrt.kbhit():
                key = (
                    msvcrt.getwch().lower()
                )  # <- konvertere brugerens input til et lille bogstav, så det matcher logikken i "run_batch" for loop.
                while msvcrt.kbhit():
                    msvcrt.getwch()  # <- kigger efter brugerens input.
                if key == "f":
                    injected = True
                elif key == "s":
                    print("Stopping batch and returning to menu…")
                    break
                elif key == "a":
                    print("Exiting program…")
                    raise SystemExit

            p = Pepsi("Pilk", "330ml", "Paper", "Carton") if injected else generate_pepsi()
            process_bottle(p)
            print_status()
            time.sleep(0.5)
        pass
    finally:
        end_current_batch()


def menu() -> None:
    """Menu med bruger inputs"""
    while True:
        choice = input("\n[Enter]=Generate Pepsi's | 'q'=Quit program > ").strip().lower()

        if choice == "q":
            print("Goodbye!")
            break

        try:
            count = int(input("How many Pepsis do you want? "))
            if count <= 0:
                print("Please enter a positive number")
                continue
            run_batch(count)  # Kalder min funktion "run_batch" det antal gange brugeren ønsker.
        except ValueError as e:
            print(f"Not a number: {e}")
            continue


def pick_bin(p: Pepsi) -> str:
    """Funktion til at bestemme hvilke produkter der hører til hvad"""
    match (p.material, p.container):
        case ("Glass", "Bottle"):
            return "glass_bottle"
        case ("Plastic", "Bottle"):
            return "plastic_bottle"
        case ("Metal", "Can"):
            return "metal_can"
        case _:
            return "rejected_bottle"


def process_bottle(p: Pepsi) -> None:
    """Vælger en kasse for mit "p" element, opdaterer tælleren, udskriver og tilføjer en række til min CSV fil"""
    bin_name = pick_bin(p)
    bin_counter[bin_name] += 1
    print(f"{p} -> {bin_name}")
    log_to_csv(p, bin_name)  # <- sørger for jeg kan tilføje denne info til min csv fil.


def print_status() -> None:
    """Udskriver status efter hver genereret flaske så vi kan se de bliver sorteret korrekt"""
    parts = [f"{k}:{bin_counter[k]}" for k in sorted(bin_counter)]
    print("Status", " | ".join(parts))


def log_to_csv(p: Pepsi, bin_name: str, path: Path = CSV_PATH) -> None:
    """Laver overskrifter til de forskellige kolonner i "sorting_log.csv"""
    with path.open("a", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=FIELDNAMES)
        writer.writerow(
            {
                "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                "brand": p.__class__.__name__,
                "taste": p.taste,
                "volume": p.volume,
                "material": p.material,
                "container": p.container,
                "bin": bin_name,
            }
        )


if __name__ == "__main__":
    init_csv()
    menu()
