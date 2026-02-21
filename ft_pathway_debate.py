#! /bin/python3.10
import alchemy
from alchemy.transmutation.basic import lead_to_gold, stone_to_gem
from alchemy.transmutation.advanced import philosophers_stone, elixir_of_life


if __name__ == "__main__":

    print(" Pathway Debate Mastery ".center(79, "="))

    print("\n" + "Testing Absolute Imports (from basic.py):")
    print("lead_to_gold(): ", lead_to_gold())
    print("stone_to_gem(): ", stone_to_gem())

    print("\n" + "Testing Relative Imports (from advanced.py):")
    print("philosophers_stone(): ", philosophers_stone())
    print("elixir_of_life(): ", elixir_of_life())

    print("\n" + "Testing Package Access:")

    try:
        alchemy.transmutation.lead_to_gold()
        print("alchemy.transmutation.lead_to_gold(): "
              "Lead transmuted to gold using Fire element created")
    except AttributeError:
        print("alchemy.transmutation.lead_to_gold(): "
              "AttributeError - not exposed")

    try:
        alchemy.transmutation.philosophers_stone()
        print("alchemy.transmutation.philosophers_stone(): [same as above]")
    except AttributeError:
        print("alchemy.transmutation.philosophers_stone(): "
              "AttributeError - not exposed")

    print("\n" + "Both pathways work! Absolute: clear, Relative: concise")
