from pygame import *
from Enemy import *

class Sparc(Enemy):
        def __init__(self, this, dmg, goal):
                super().__init__(this, dmg, True, goal)
        
        def pickNewPos():
                return (0, 0)