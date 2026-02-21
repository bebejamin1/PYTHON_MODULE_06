#  Advanced potion recipes

from alchemy import elements


# Returns "Healing potion brewed with [fire_result] and [water_result]"
def healing_potion() -> str:
    return (f"Healing potion brewed with {elements.create_fire()} and "
            f"{elements.create_water()}")


#  Returns "Strength potion brewed with [earth_result] and [fire_result]"
def strength_potion() -> str:
    return (f"Strength potion brewed with {elements.create_earth()} and "
            f"{elements.create_fire()}")


#  Returns "Invisibility potion brewed with [air_result] and [water_result]"
def invisibility_potion() -> str:
    return (f"Invisibility potion brewed with {elements.create_air()} and "
            f"{elements.create_water()}")


#  Returns "Wisdom potion brewed with all elements: [all_four_results]"
def wisdom_potion() -> str:
    return ("Wisdom potion brewed with all elements: "
            f"{elements.create_fire()}, {elements.create_water()}, "
            f"{elements.create_air()}, {elements.create_earth()}")
