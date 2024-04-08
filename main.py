#all game related logic happens here. calls are made to externals

#this block of code is setting up the screen, libraries, 
import random       #importing the random library
from MainActor import *
import pygame as pg

# Initialize Pygame
pg.init()

# Set the screen to windowed mode
HD = (1280, 720)
SD = (640, 480)
screen = pg.display.set_mode(SD, 0)
pg.display.set_caption("QIX")
screenSize = pg.display.get_window_size()
screenMid = (screenSize[0] // 2, screenSize[1] // 2)
GAME_FONT = pg.freetype.Font("PressStart2P.ttf", 25)

PASTEL_CORAL = (248, 132, 121)



def drawScene():
    #placeholders, will be switched for updateable entities
    screen.fill((0,0,0))
    boardW = 400

    # health bar
    GAME_FONT.render_to(screen, (0, 0), "HEALTH", (255, 0, 0))
    pg.draw.rect(screen, (255, 0, 0),(150, 10, 3 * screenSize[0] // 4, 10))
    
    pg.draw.rect(screen, (255, 255, 255), (screenMid[0] - boardW // 2 - 115, screenMid[1] - boardW // 2 + 15, boardW + 20, boardW + 20), 1) 
    pg.draw.rect(screen, PASTEL_CORAL, (screenMid[0] - boardW // 2 - 105, screenMid[1] - boardW // 2 + 25, boardW, boardW) ) 
    
    pg.draw.rect(screen, (255, 0, 0), player.this)

# add a check for the player moving off the board
def update(dx, dy):
    player.this.move_ip(dx, dy)

#some game states
KEY_RIGHT = False
KEY_LEFT = False
KEY_UP = False
KEY_DOWN = False
PUSH = False
dx = 0
dy = 0
player = MainActor()

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
            if event.key == K_RIGHT:
                KEY_RIGHT = True     #if right key is down, the corresponding state is true
            if event.key == K_UP:
                KEY_UP = True     #if up key is down, the corresponding state is true
            if event.key == K_DOWN:
                KEY_DOWN = True     #if down key is down, the corresponding state is true
            if event.key == K_SPACE:
                PUSH = True     #if down key is down, the corresponding state is true
        if event.type == KEYUP:
            if event.key == K_LEFT:
                KEY_LEFT = False     #if left key is up, the corresponding state is false
            if event.key == K_RIGHT:
                KEY_RIGHT = False     #if right key is up, the corresponding state is false
            if event.key == K_UP:
                KEY_UP = False     #if up key is up, the corresponding state is false
            if event.key == K_DOWN:
                KEY_DOWN = False     #if down key is up, the corresponding state is false
            if event.key == K_SPACE:
                PUSH = False     #if down key is down, the corresponding state is true

    #key state handler.
    if KEY_UP:
        dy = -10
    elif KEY_DOWN:
        dy = 10
    else:
        dy = 0

    if KEY_LEFT:
        dx = -10
    elif KEY_RIGHT:
        dx = 10
    else:
        dx = 0


    update(dx, dy)
    drawScene()
    pg.display.flip()      #ok so do you know what a flipbook is? Yeah, this "flips" to the next frame
    pg.time.Clock().tick(60)                     #waits long enough to have 60 fps

