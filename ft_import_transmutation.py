#! /bin/python3.10

#  Demonstration script (at repository root)

import alchemy.elements
from alchemy.elements import create_earth
from alchemy.potions import healing_potion as heal
from alchemy.elements import create_fire, create_water
from alchemy.potions import strength_potion as strength

if __name__ == "__main__":

    print(" Import Transmutation Mastery ".center(79, "="))

    print("\n" + "Method 1 - Full module import:")
    print("alchemy.elements.create_fire():",
          alchemy.elements.create_fire())

    print("\n" + "Method 2 - Specific function import:")
    print("create_water():", create_water())

    print("\n" + "Method 3 - Aliased import:")
    print("heal():", heal())

    print("\n" + "Method 4 - Multiple imports:")
    print("create_earth():", create_earth())
    print("create_fire():", create_fire())
    print("strength_potion():", strength())

    print("\n" + "All import transmutation methods mastered!")
