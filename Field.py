from pygame import *
#this is a change!!!!!!!
class Field:
        def __init__(self, center = Rect(0, 0, 0, 0), edge = Rect(0, 0, 0, 0)):
                self.center = center
                self.edge = edge
                self.junctions = [(33, 438), (33, 28), (443, 438),(443,28)]