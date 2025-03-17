import math
from typing import Dict


def pythonSto() -> None:
    """
    This function prints the message "Python je fajn'" 100 times.
    """
    for _ in range(100):
        print("Python je fajn'")


polomer: int = 5
obsah: float = math.pi * polomer**2
obvod: float = 2 * math.pi * polomer
objem: float = 4 / 3 * math.pi * polomer**3

mena_prezyvky: Dict[str, str] = {
    "Jano": "Janči",
    "Peter": "Peto",
    "Lukáš": "Luky",
    "Marek": "Maro",
    "Tomáš": "Tomi",
    "Michal": "Mišo",
    "Juraj": "Ďuri",
    "Martin": "Maťo",
    "Andrej": "Andy",
    "Viktor": "Viki",
}

print(mena_prezyvky["Jano"])
print(mena_prezyvky["Lukáš"])
