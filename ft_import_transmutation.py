#! /bin/python3.10

#  Demonstration script (at repository root)

import alchemy.elements
from alchemy.elements import create_fire
from alchemy.potions import healing_potion as heal
from alchemy.elements import create_fire, create_water

if __name__ in "__main__":

    print(" Import Transmutation Mastery ".center(79, "=") + "\n")

    print("Method 1 - Full module import:")
    print("alchemy.elements.create_fire():",
          alchemy.elements.create_fire())

    print("Method 2 - Specific function import:")

    print("Method 3 - Aliased import:")

    print("Method 4 - Multiple imports:")

    print("\n" + "All import transmutation methods mastered!")
