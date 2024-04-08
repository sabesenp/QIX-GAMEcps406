#all game related logic happens here. calls are made to externals

#this block of code is setting up the screen, libraries, 
import random       #importing the random library
from MainActor import *
from pygame import *

# Initialize Pygame
init()

# Set the screen to windowed mode
HD = (1280, 720)
SD = (640, 480)
screen = display.set_mode(SD, RESIZABLE)
display.set_caption("QIX")

PASTEL_CORAL = (248, 132, 121)

#some game states
KEY_RIGHT = False
KEY_LEFT = False
KEY_UP = False
KEY_DOWN = False
PUSH = False
dx = 10
dy = 10
player = MainActor(Rect(0,0,10,10),100, True)

def drawScene():
    #placeholders, will be switched for updateable entities
    screen.fill((0,0,0))
    screenSize = display.get_window_size()
    screenMid = (screenSize[0] // 2, screenSize[1] // 2)
    boardW = 200

    
    draw.rect(screen, PASTEL_CORAL, (screenMid[0] - boardW // 2, screenMid[1] - boardW // 2, boardW, boardW) ) 
    draw.rect(player.this)


# Start the main loop
while True:

    # Check for events
    for event in event.get():
        # Check for the quit event
        if event.type == QUIT:
            # Quit the game
            quit()
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
                PUSH = False     #if down key is up, the corresponding state is false

    #key state handler.
    if KEY_UP:
        dy = -abs(dy)
    elif KEY_DOWN:
        dy = abs(dy)
    else:
        dy = 0

    if KEY_LEFT:
        dx = -abs(dx)
    elif KEY_DOWN:
        dx = abs(dx)
    else:
        dx = 0


    #add an update function here???




    #call drawScene() after all logic calculations
    display.flip()      #ok so do you know what a flipbook is? Yeah, this "flips" to the next frame
    time.Clock().tick(60)                     #waits long enough to have 60 fps

