#! /bin/python3.10

# The main sacred scroll
# Le principal rouleau sacré

# Importez et exposez UNIQUEMENT create_fire et create_water
# à partir de elements.py.
# N'exposez PAS create_earth et create_air (ils restent cachés)
# Utilisation : depuis .elements, importez create_fire, create_water

__version__ = "1.0.0"

__author__ = "Master Pythonicus"

from .elements import create_fire, create_water

__all__ = [
    "create_fire",
    "create_water"
]
