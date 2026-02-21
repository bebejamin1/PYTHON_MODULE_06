# Validates spell ingredients

def validate_ingredients(ingredients: str) -> str:
    ingredients_valid = ["fire", "water", "earth", "air"]
    for ingredient in ingredients_valid:
        if (ingredient in ingredients):
            return (f"{ingredients} - VALID")
    return (f"{ingredients} - INVALID")
