from .place import *
from .entrances import *
from .containers import *

#Format: name - description - container - entrance

canteen = Place("Canteen", "Needed", cCanteen, uDoor)
cell13 = Place("Cell 13", "Needed", cCell13, uDoor)
courtyard = Place("Courtyard", "Needed", cCourtyard, uDoor)
janitor = Place("Janitors Office", "Needed", cJanitor, uDoor)
security = Place("Security Office", "Needed", cSecurity, uDoor)
visitors = Place("Visitors Room", "Needed", cVisitors, uDoor)
walkway = Place("Walkway", "Needed", cWalkway, uDoor)
watch = Place("Watch Tower", "Needed", cWatch, uDoor)

#Place connections

canteen.connect(north=janitor, south=security, west=walkway)
cell13.connect(north=walkway)
courtyard.connect(north=visitors, east=walkway, south=watch)



