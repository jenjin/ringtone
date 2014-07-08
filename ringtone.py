import pygame, sys, random
from pygame.locals import *

pygame.init()
DISPLAYSURF = pygame.display.set_mode((600, 400))
pygame.display.set_caption('RINGTONE GENERATOR 3000')

# set up the colors
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
WHITE = (255, 255, 255)
PINK = (255, 105, 180)


def showHomeScreen():
    titleFont = pygame.font.Font('freesansbold.ttf', 30)
    DISPLAYSURF.fill(PINK)
    titleSurf1 = titleFont.render('Create your own ringtone wow', True, WHITE, PINK)
    titleSurf2 = titleFont.render('Press SPACE to continue!', True, BLUE, PINK)
    text1Rect = titleSurf1.get_rect()
    text1Rect.center = (300, 150)
    text2Rect = titleSurf2.get_rect()
    text2Rect.center = (300, 200)
    DISPLAYSURF.blit(titleSurf1, text1Rect)
    DISPLAYSURF.blit(titleSurf2, text2Rect)
    pygame.display.update()

while True: # main loop
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()

// Yay more pull requests
