#! /bin/python3.10

# Demonstration script (at repository root)
# Script de démonstration (à la racine du référentiel)

# from alchemy import elements
import alchemy

if __name__ == "__main__":
    print("\n" + " Sacred Scroll Mastery ".center(79, "=") + "\n")

    spells = ["create_fire", "create_water", "create_earth", "create_air"]

    print("Testing direct module access:")

    for spell in spells:
        func = getattr(alchemy.elements, spell)
        print(f"alchemy.elements.{spell}():", func())

    print("\n" + "Testing package-level access (controlled by __init__.py):")

    for spell in spells:
        try:
            func = getattr(alchemy, spell)
            print(f"alchemy.{spell}():", func())
        except AttributeError:
            print(f"alchemy.{spell}(): AttributeError - not exposed")

    print("\n" + "Package metadata:")
    print("Version: ", alchemy.__version__)
    print("Author", alchemy.__author__)
