from pygame import *
class MainActor:
    def __init__(self, this = Rect(215,465,10,10), health = 100, edge = True):
        self.this = this
        self.health = health
        self.edge = edge
        self.pos = this.topleft

    