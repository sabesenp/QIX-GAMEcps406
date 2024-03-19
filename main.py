#this block of code is setting up the screen, libraries, 
import random       #importing the random library
import pygame as pg

# Initialize Pygame
pg.init()

# Set the screen to windowed mode
dev_size = (854, 650)
SD = (640, 480)
screen = pg.display.set_mode(dev_size, pg.RESIZABLE)
screenSize = pg.display.get_window_size()
screenMid = (screenSize[0] // 2, screenSize[1] // 2)
pg.display.set_caption("QIX")

# Start the main loop
while True:
    # Check for events
    
    print()
    for event in pg.event.get():
        # Check for the quit event
        if event.type == pg.QUIT:
            # Quit the game
            pg.quit()
            exit()

