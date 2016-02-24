from .entrance import *

#Format: name - unlocked

lDoor = Entrance("Door", False)
uDoor = Entrance("Door", True)
lWindow = Entrance("Window", False)
uWindow = Entrance("Window", True)

#Array of entrance objects for open command
entrances = [lDoor, uDoor, lWindow, uWindow]