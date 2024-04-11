#all game related logic happens here. calls are made to externals

#this block of code is setting up the screen, libraries, 
import random       #importing the random library
from MainActor import *
from Field import *
import pygame as pg

# Initialize Pygame
pg.init()

# Set the screen to windowed mode
HD = (1280, 720)
SD = (640, 480)


screen = pg.display.set_mode(SD, 0)
pg.display.set_caption("QIX")
screen_size = pg.display.get_window_size()
screen_mid = (screen_size[0] // 2, screen_size[1] // 2)
GAME_FONT = pg.freetype.Font("PressStart2P.ttf", screen_size[0]//25)
PASTEL_CORAL = (248, 132, 121)
# list of player objects
trailRects = []


def drawScene():
    #placeholders, will be switched for updateable entities
    # screen.fill((0,0,0))

    # health bar
    GAME_FONT.render_to(screen, (0, 0), "HEALTH", (255, 0, 0))

    pg.draw.rect(screen, (255, 255, 255), field.edge, 10) 
    
    pg.draw.rect(screen, (255, 0, 0), player.this)

    pg.draw.rect(screen, (255, 0, 0),(150, 10, 3 * screen_size[0] // 4 + 5, 10))




def inBounds() -> bool:
    # and player.this.left >= field.edge.left and player.this.right <= field.edge.right
    return player.this.bottom <= field.edge.bottom + 10 and player.this.top + 10 >= field.edge.top and player.this.left + 10 >= field.edge.left and player.this.right <= field.edge.right + 10

def inEdge() -> bool:
    if not inBounds():
        return False
    # add checks for which edge player is on
    # perform check based on that
    if player.this.centerx <= 40 or player.this.centerx >= 450 or \
        player.this.centery <= 35 or player.this.centery >= 445:
        return True

def whichEdge() -> str:
    if inEdge():
        if player.this.centerx <= 40:
            return "left"
        if player.this.centerx >= 450:
            return "right"
        if player.this.centery <= 35:
            return "top"
        if player.this.centery >= 445:
            return "bottom"
    return "no"

def whichEdgeTuple(coords) -> str:
    if inEdge():
        if coords[0] <= 40:
            return "left"
        if coords[0] >= 450:
            return "right"
        if coords[1] <= 35:
            return "top"
        if coords[1] >= 445:
            return "bottom"
    return "no"

def update(dx, dy) -> None:
    player.this.move_ip(dx, dy)
    # if player.edge and not inEdge():
    #    player.this.move_ip(-dx, -dy)
    if not inBounds():
        player.this.move_ip(-dx, -dy)

def addTrail(p) -> None:
    # coords are stored in tuples (x, y)
    # ignores duplicate coords
    if len(trailRects) <= 0 or not (trailRects[-1][0] == p.this.centerx and trailRects[-1][1] == p.this.centery):
        trailRects.append((p.this.centerx, p.this.centery))


def inEdgeTuple(coords) -> bool:
    return coords[0] <= 40 or coords[0] >= 450 \
        or coords[1] <= 35 or coords[1] >= 445
        

def fillRect() -> None:
    if len(trailRects) < 2:
        return
    if inEdgeTuple(trailRects[-1]) and inEdgeTuple(trailRects[-2]):
        return
    # store current coords
    # go through previous coords stored in trailRects
    # find last coord it was touching corner
    # using current and last corner touch, fill area with rect
    # 445 bottom 35 top y    # 40 left 450 right x
    if inEdge():
        i = 2 

        currPos = trailRects[-1]
        while not inEdgeTuple(trailRects[-i]):
            i = i + 1

        lastEdgeTouch = trailRects[-i]
        # fail safe if f doesn't fall in any cases below
        f = Rect(1000, 1000, 100, 100)

        # reminder: y larger going down
        # x larger going right

        if whichEdgeTuple(lastEdgeTouch) == "bottom":
            if whichEdge() == "right":
                f = Rect(currPos[0] - (currPos[0] - lastEdgeTouch[0]), currPos[1], currPos[0] - lastEdgeTouch[0], lastEdgeTouch[1] - currPos[1])
            elif whichEdge() == "left":
                f = Rect(currPos[0], currPos[1], lastEdgeTouch[0] - currPos[0], lastEdgeTouch[1] - currPos[1])

        elif whichEdgeTuple(lastEdgeTouch) == "left":
            if whichEdge() == "bottom":
                f = Rect(currPos[0] + (lastEdgeTouch[0] - currPos[0]), lastEdgeTouch[1], currPos[0] - lastEdgeTouch[0], currPos[1] - lastEdgeTouch[1])
            elif whichEdge() == "top":
                f = Rect(currPos[0] + (lastEdgeTouch[0] - currPos[0]), currPos[1], currPos[0] - lastEdgeTouch[0], lastEdgeTouch[1] - currPos[1])

        elif whichEdgeTuple(lastEdgeTouch) == "top":
            if whichEdge() == "right":
                f = Rect(lastEdgeTouch[0], lastEdgeTouch[1], currPos[0] - lastEdgeTouch[0], currPos[1] - lastEdgeTouch[1])
            elif whichEdge() == "left":
                f = Rect(currPos[0], lastEdgeTouch[1], lastEdgeTouch[0] - currPos[0], currPos[1] - lastEdgeTouch[1])

        elif whichEdgeTuple(lastEdgeTouch) == "right":
            if whichEdge() == "top":
                f = Rect(currPos[0], currPos[1], lastEdgeTouch[0] - currPos[0], lastEdgeTouch[1] - currPos[1])
            elif whichEdge() == "bottom":
                f = Rect(currPos[0], lastEdgeTouch[1], lastEdgeTouch[0] - currPos[0], currPos[1] - lastEdgeTouch[1])


        pg.draw.rect(screen, (0, 100, 0), f)

        
#some game states
KEY_RIGHT = False
KEY_LEFT = False
KEY_UP = False
KEY_DOWN = False
PUSH = False
dx = 0
dy = 0
player = MainActor()
board_w = 5 * screen_size[1] // 6
field = Field(Rect(screen_mid[0] - board_w // 2 - 75, screen_mid[1] - board_w // 2, board_w, board_w) , Rect(screen_mid[0] - board_w // 2 - 4 - 75, screen_mid[1] - board_w // 2 - 4, board_w + 8, board_w + 8))

pg.draw.rect(screen, PASTEL_CORAL, field.center) 

# Start the main loop
while True:
    
    addTrail(player)
    fillRect()

    # Check for events
    for event in pg.event.get():
        # Check for the quit event
        if event.type == QUIT:
            # Quit the game
            pg.quit()
            exit()
        
        #key listener, will flip the according key bits
        if event.type == KEYDOWN:
            if event.key == K_LEFT:
                KEY_LEFT = True     #if left key is down, the corresponding state is true
            elif event.key == K_RIGHT:
                KEY_RIGHT = True     #if right key is down, the corresponding state is true
            elif event.key == K_UP:
                KEY_UP = True     #if up key is down, the corresponding state is true
            elif event.key == K_DOWN:
                KEY_DOWN = True     #if down key is down, the corresponding state is true
            if event.key == K_SPACE:
                PUSH = True     #if down key is down, the corresponding state is true
        if event.type == KEYUP:
            if event.key == K_LEFT:
                KEY_LEFT = False     #if left key is up, the corresponding state is false
            elif event.key == K_RIGHT:
                KEY_RIGHT = False     #if right key is up, the corresponding state is false
            elif event.key == K_UP:
                KEY_UP = False     #if up key is up, the corresponding state is false
            elif event.key == K_DOWN:
                KEY_DOWN = False     #if down key is up, the corresponding state is false
            if event.key == K_SPACE:
                PUSH = False     #if down key is down, the corresponding state is true

    #key state handler.
    dx = 0
    dy = 0
    if KEY_UP: 
        dy = -10
    elif KEY_DOWN:
        dy = 10
    elif KEY_LEFT:
        dx = -10
    elif KEY_RIGHT:
        dx = 10


    update(dx, dy)
    drawScene()
    pg.display.flip()      #ok so do you know what a flipbook is? Yeah, this "flips" to the next frame
    pg.time.Clock().tick(15)                     #waits long enough to have 60 fps

