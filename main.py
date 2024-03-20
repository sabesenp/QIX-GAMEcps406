#this block of code is setting up the screen, libraries, 
import random       #importing the random library
import pygame as pg

# Initialize Pygame
pg.init()

# Set the screen to windowed mode
HD = (1280, 720)
SD = (640, 480)
screen = pg.display.set_mode(HD, pg.RESIZABLE)
pg.display.set_caption("QIX")

PASTEL_CORAL = (248, 132, 121)

#some game states
KEY_RIGHT = False
KEY_LEFT = False
KEY_UP = False
KEY_DOWN = False

# Start the main loop
while True:
    # Check for events
    for event in pg.event.get():
        # Check for the quit event
        if event.type == pg.QUIT:
            # Quit the game
            pg.quit()
            exit()
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_LEFT:
                KEY_LEFT = True     #if left key is down, the corresponding state is true
            if event.key == pg.K_RIGHT:
                KEY_RIGHT = True     #if right key is down, the corresponding state is true
            if event.key == pg.K_UP:
                KEY_UP = True     #if up key is down, the corresponding state is true
            if event.key == pg.K_DOWN:
                KEY_DOWN = True     #if down key is down, the corresponding state is true
        if event.type == pg.KEYUP:
            if event.key == pg.K_LEFT:
                KEY_LEFT = False     #if left key is up, the corresponding state is false
            if event.key == pg.K_RIGHT:
                KEY_RIGHT = False     #if right key is up, the corresponding state is false
            if event.key == pg.K_UP:
                KEY_UP = False     #if up key is up, the corresponding state is false
            if event.key == pg.K_DOWN:
                KEY_DOWN = False     #if down key is up, the corresponding state is false
    
    screen.fill((0,0,0))
    screenSize = pg.display.get_window_size()
    screenMid = (screenSize[0] // 2, screenSize[1] // 2)
    boardW = 200
    pg.draw.rect(screen, PASTEL_CORAL, (screenMid[0] - boardW // 2, screenMid[1] - boardW // 2, boardW, boardW) )


    pg.display.flip()      #drawing the scene
    pg.time.Clock().tick(60)                     #waits long enough to have 60 fps

