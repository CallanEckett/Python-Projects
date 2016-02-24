from .weapon import *
from .armor import *
from .player import *
from .game import *

#weapons: name - min damage - max damage

sword = Weapon("Sword", 19, 20)
dagger = Weapon("Dagger", 9, 10)

weapons = [sword, dagger]

#Armor: name - min defense - max defense

leather = Armor("Leather Armor", 10, 14)
chainmail = Armor("Chainmail Armor", 19, 22)

armors = [leather, chainmail]

#Players: name - health - weapon - armor

p1 = Player("p1", 100, dagger, leather)
p2 = Player("p2", 100, dagger, leather)

players = [p1, p2]

#Games: name - current

game = Game("game", p1)