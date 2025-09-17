"""
Mini Dataanalyse Python opgave

opgave
1. String manipulation
   - Modtag en tekststreng.
   - Returnér antal unikke ord og længste ord.

2. Lists & Tuples
   - Liste: alle ord i små bogstaver.
   - Tuple: tre mest brugte ord.

3. Dictionaries
   - Ordfrekvens med antal forekomster.

4. Sortering & Filtrering
   - Sortér ordfrekvens efter hyppighed (mest brugt først).
   - Filtrér ord længere end 4 bogstaver.

5. Arrays (standardbibliotek)
   - Array med længden af hvert ord.

6. NumPy
   - Beregn gennemsnit og standardafvigelse af ordlængder.
"""

import array
import numpy as np
from collections import Counter

tekst = "Python er fantastisk og Python er sjovt kode er sjovt"


def ord_statistik(tekst: str) -> tuple[int, str]:
    """Returnerer (antal_ord, længste_ord)"""
    tekst_split = tekst.split()
    antal_ord = len(tekst_split)
    længste_ord = max(tekst_split, key=len)

    tuple_list = (antal_ord, længste_ord)
    print(tuple_list)
    return tuple_list


##


def mest_brugte_ord(tekst: str) -> tuple[str, str, str]:
    """Returnerer tuple med de tre mest brugte ord"""
    pass


def ord_frekvens(tekst: str) -> dict[str, int]:
    """Returnerer dictionary med ordfrekvens"""
    pass


def filtrer_ord(ordliste: list[str]) -> list[str]:
    """Returnerer ny liste med ord længere end 4 bogstaver"""
    pass


def ordlaengder_array(tekst: str) -> array.array:
    """Returnerer array.array med ordlængder"""
    pass


def numpy_statistik(tekst: str) -> tuple[float, float]:
    """Returnerer (gennemsnit, std_afvigelse) af ordlængder via NumPy"""
    pass


# ---------------------------
#           TESTKODE hvis den kører igennem og i modtager et tillykke er i igennem
# ---------------------------
if __name__ == "__main__":
    tekst = "Python er fantastisk og Python er sjovt kode er sjovt"

    assert ord_statistik(tekst) == (10, "fantastisk")
    assert mest_brugte_ord(tekst) == ("er", "python", "sjovt")
    assert ord_frekvens(tekst) == {
        "python": 2,
        "er": 3,
        "fantastisk": 1,
        "og": 1,
        "sjovt": 2,
        "kode": 1,
    }
    assert filtrer_ord(["hej", "python", "kode", "fantastisk"]) == ["python", "fantastisk"]

    np.testing.assert_array_equal(
        ordlaengder_array(tekst), array.array("i", [6, 2, 10, 2, 6, 2, 5, 4, 2, 5])
    )

    gennemsnit, std = numpy_statistik(tekst)
    assert round(gennemsnit, 2) == 4.40
    assert round(std, 2) == 2.46

    print(
        "******************************************************************************************"
    )
    print(
        "************************************     Tillykke         ********************************"
    )
    print(
        "*                                    Alle tests bestået                                  *"
    )
    print(
        "******************************************************************************************"
    )
    print(
        "******************************************************************************************"
    )
