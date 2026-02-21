#! /bin/python3.10

from alchemy.grimoire import validate_ingredients
from alchemy.grimoire import record_spell

if __name__ == "__main__":

    print(" Circular Curse Breaking ".center(79, "="))

    print("\n" + "Testing ingredient validation:")
    print("validate_ingredients(\"fire air\"):",
          validate_ingredients("fire air"))
    print("validate_ingredients(\"dragon scales\"):",
          validate_ingredients("dragon scales"))

    print("\n" + "Testing spell recording with validation:")
    print("record_spell(\"Fireball", "fire air\"):",
          record_spell("Fireball", "fire air"))
    print("record_spell(\"Dark Magic\", \"shadow\"):",
          record_spell("Dark Magic", "shadow"))

    print("\n" + "Testing late import technique:")
    print("record_spell(\"Lightning\", \"air\"):",
          record_spell("Lightning", "air"))

    print("\n" + "Circular dependency curse avoided using late imports!")
    print("All spells processed safely!")
