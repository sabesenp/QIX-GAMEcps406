#all game related logic happens here. calls are made to externals
#this is a change
#this block of code is setting up the screen, libraries, 
from random import randint as rand       #importing the random library
from MainActor import *
from Field import *
from Sparc import *
import pygame as pg
from math import copysign

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



def drawScene():
    #placeholders, will be switched for updateable entities

    screen.fill((0,0,0))
    
    # health bar
    GAME_FONT.render_to(screen, (0, 0), "HEALTH", (255, 0, 0))
    pg.draw.rect(screen, (255, 0, 0),(150, 10, 3 * screen_size[0] // 4 + 5, 10))


    pg.draw.rect(screen, (255, 255, 255), field.edge, 10) 
    pg.draw.rect(screen, PASTEL_CORAL, field.center) 
    
    pg.draw.rect(screen, (255, 0, 0), player.this)
    
    pg.draw.rect(screen, (0, 0, 255), sparc.this)


def inBounds():
    return player.this.bottom <= field.edge.bottom + 10 and player.this.top + 10 >= field.edge.top and player.this.left + 10 >= field.edge.left and player.this.right <= field.edge.right + 10

def inEdge():
    if not inBounds():
        return False
    
    if player.this.centerx <= 40 or player.this.centerx >= 450 or player.this.centery <= 35 or player.this.centery >= 445:
        return True


def update(dx, dy):
    if PUSH and player.edge:
        player.edge = False
    
    if PUSH and inEdge():
        player.this.move_ip(dx, dy) 
    elif PUSH:
        player.this.move_ip(0.5*dx, 0.5*dy) 
    else:
        player.this.move_ip(dx, dy)

    if player.edge and not inEdge():
       if PUSH:
        player.this.move_ip(-0.5*dx, -0.5*dy)
       else:
        player.this.move_ip(-dx, -dy)
    elif not player.edge and inEdge():
        player.edge = True
    if not inBounds():
        player.this.move_ip(-dx, -dy)

def pickOriginal(pos: tuple) -> tuple:
    new = field.junctions[rand(0, len(field.junctions) - 1)]
    if pos == new:
        return pickOriginal(pos)
    else:
        return new


def updateEnemy():

    pos = sparc.this.topleft    #defining position as top left of sparc

    if pos == sparc.goal or sparc.dir == [0,0]:     #if sparc has reached it's random goal, or has a default val
        sparc.goal = pickOriginal(pos)              #pickOriginal is a recursive function guaranteeing a new goal, not equal to current position
        sparc.dir = [copysign(1, sparc.goal[0] - pos[0]), copysign(1, sparc.goal[1] - pos[1])]  #dir is a direction vector, determining where sparc will move
    elif sparc.this.topleft in field.junctions:     #if sparc is at a junction, we must still recalculate the new direction
        sparc.dir = [copysign(1, sparc.goal[0] - pos[0]), copysign(1, sparc.goal[1] - pos[1])]
    
    #sparc is confined to edges. thus sparc is forced to pick one
    if pos[0] == sparc.goal[0]:
        sparc.dir[0] = 0
    elif pos[1] == sparc.goal[1]:
        sparc.dir[1] = 0
    else:
        sparc.dir[rand(0,1)] = 0    #if sparc is not level with the goal, it will pick a random direction

    sparc.this.move_ip(sparc.dir[0] * 5, sparc.dir[1] * 5)

    #lets hope this don't break when we integrate Ryan's code, eh?
    



#some game states
KEY_RIGHT = False
KEY_LEFT = False
KEY_UP = False
KEY_DOWN = False
PUSH = False
player = MainActor()

board_w = 5 * screen_size[1] // 6
field = Field(Rect(screen_mid[0] - board_w // 2 - 75, screen_mid[1] - board_w // 2, board_w, board_w) , Rect(screen_mid[0] - board_w // 2 - 4 - 75, screen_mid[1] - board_w // 2 - 4, board_w + 8, board_w + 8))

sparc = Sparc(Rect(field.junctions[rand(0, len(field.junctions) - 1)], (15,15)), -10, field.junctions[rand(0, len(field.junctions) - 1)])
sparc.dir = [copysign(1, sparc.goal[0] - sparc.this.topleft[0]), copysign(1, sparc.goal[1] - sparc.this.topleft[1])]
# Start the main loop
while True:

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



    updateEnemy()
    update(dx, dy)
    drawScene()
    pg.display.flip()      #ok so do you know what a flipbook is? Yeah, this "flips" to the next frame
    pg.time.Clock().tick(60)                     #waits long enough to have 60 fps

