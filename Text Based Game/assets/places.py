from .place import *
from .containers import *

#Format: name - description

cell = Place("Cell 512", "Needed")
corridor = Place("Corridor", "Needed")

cell.connect(south=corridor)

