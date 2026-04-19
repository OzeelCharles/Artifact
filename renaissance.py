import artifact as art
from random import randint


paint = art.Painting(
    "The guy who's thinking", randint(1300, 1700),
    "An Anonymous guy", "colors")

sculpture = art.Sculpture(
    "The mona Lisa but in 3D", randint(1300, 1700), "marble", 12)

building = art.Building(
    "Versaille Palace but in Romania", randint(1300, 1700),
    "An Armee of builder", "Romania", "Bucarest")
