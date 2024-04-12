from pygame import *
from math import copysign

class Qix:
        def __init__(self, this, dmg, goal):
                self.this = this        #still defined by Rect, but shape will be a spinning ellipse
                self.dmg = dmg
                self.edge = False
                self.goal=goal
                self.dir=(0,0)