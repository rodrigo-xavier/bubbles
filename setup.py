import pygame
from pygame.locals import *

import random, math, sys
from bubble import BubblesGame


##################################### CONFIGURATIONS #####################################
################# Database Location #################

IMG_PATH = "../../.database/pibic/pygame/img/"

################# Workflow ##########################

SURFACE_COLOR = (0,0,0)
BUBBLES_COLOR = (255,255,255)
WIDTH, HEIGHT = 500, 500
FPS = 0
NUMBER_OF_FRAMES = 120000
BUBBLES_RADIUS = 30
CIRCLE_BUBBLES = 10
SQUARE_BUBBLES = 10

################# Select Save Option ################

SAVE = False

##################################### CONFIGURATIONS #####################################




##################################### GAMESPACE ##########################################


    
def reset_folder(self):
        try:
            shutil.rmtree(self.img_path)
        except OSError as e:
            print("Error: %s" % (e.strerror))
        try:
            os.mkdir(self.img_path)
        except OSError:
            print ("Creation of the directory failed")

def play_game():
    if SAVE:
        reset_folder()
    
    bubble = BubblesGame(
        SURFACE_COLOR=SURFACE_COLOR,
        FPS=FPS,
        CIRCLE_BUBBLES=CIRCLE_BUBBLES,
        SQUARE_BUBBLES=SQUARE_BUBBLES,
        BUBBLES_COLOR=BUBBLES_COLOR,
        BUBBLES_RADIUS=BUBBLES_RADIUS,
        WIDTH=WIDTH,
        HEIGHT=HEIGHT,
    )

    n = 0
    while True:
        n += 1
        bubble.run()
        if SAVE:
            bubble.save(IMG_PATH, n)

################# Init #################

pygame.init()
play_game()
pygame.quit(); sys.exit()