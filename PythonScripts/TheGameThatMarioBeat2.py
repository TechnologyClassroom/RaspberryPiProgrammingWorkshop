# The Game That Mario Beat 2
# By Michael McMahon

# This game was modified from:
# Wormy (a Nibbles clone)
# By Al Sweigart al@inventwithpython.com
# http://inventwithpython.com/pygame
# Released under a "Simplified BSD" license

#KRT 14/06/2012 modified Start Screen and Game Over screen to cope with mouse events
#KRT 14/06/2012 Added a non-busy wait to Game Over screen to reduce processor loading from near 100%
import random, pygame, sys
from pygame.locals import *


# Game Variables
FPS = 15
WINDOWWIDTH = 1000 # 1900 # 640
WINDOWHEIGHT = 700 # 1780 # 480
CELLSIZE = 20
assert WINDOWWIDTH % CELLSIZE == 0, "Window width must be a multiple of cell size."
assert WINDOWHEIGHT % CELLSIZE == 0, "Window height must be a multiple of cell size."
CELLWIDTH = int(WINDOWWIDTH / CELLSIZE)
CELLHEIGHT = int(WINDOWHEIGHT / CELLSIZE)

#             R    G    B
WHITE     = (255, 255, 255)
BLACK     = (  0,   0,   0)
RED       = (255,   0,   0)
GREEN     = (  0, 255,   0)
DARKGREEN = (  0, 155,   0)
DARKGRAY  = ( 40,  40,  40)
BGCOLOR = BLACK

UP = 'up'
DOWN = 'down'
LEFT = 'left'
RIGHT = 'right'

HEAD = 0 # syntactic sugar: index of the worm's head


# This function uses the variable above and creates an infinite loop
# main() is the first function called.
def main():
    global FPSCLOCK, DISPLAYSURF, BASICFONT

    pygame.init()
    FPSCLOCK = pygame.time.Clock()
    DISPLAYSURF = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))
    BASICFONT = pygame.font.Font('freesansbold.ttf', 18)
    pygame.display.set_caption('The Game That Mario Beat')
    # This sets the title of the window.

    # This runs the title screen and then loops the game and the Game Over screen.
    showStartScreen()
    while True:
        runGame()
        showGameOverScreen()


# Game content
def runGame():
# Ways to lose, a key other than enter is pressed.
# Future idea time limit
    DISPLAYSURF.fill(BGCOLOR)
    pygame.display.update() # Debug
    gameOverFont = pygame.font.Font('freesansbold.ttf', 35)
    gameSurf = gameOverFont.render('Press the enter or return key to win.', True, WHITE)
    overSurf = gameOverFont.render('All you have to do is press that key.', True, WHITE)
    gameRect = gameSurf.get_rect()
    overRect = overSurf.get_rect()
    gameRect.midtop = (WINDOWWIDTH / 2, 10)
    overRect.midtop = (WINDOWWIDTH / 2, gameRect.height + 10 + 25)

    DISPLAYSURF.blit(gameSurf, gameRect)
    DISPLAYSURF.blit(overSurf, overRect)
    pygame.display.update()
    pygame.time.wait(500)
    pygame.event.get()  #clear out event queue 

    while True: # main game loop
        for event in pygame.event.get(): # event handling loop
            if event.type == QUIT:
                terminate()
            # elif time out lose
            elif event.type == KEYDOWN:
                if event.key == K_RETURN:
                    showGameWinScreen()
                elif event.key == K_ESCAPE:
                    terminate()
                else:
                    showGameOverScreen()

#        DISPLAYSURF.fill(BGCOLOR)
        pygame.display.update()
        FPSCLOCK.tick(FPS)


# "Press any key to play" message
def drawPressKeyMsg():
    pressKeySurf = BASICFONT.render('Press any key to play.', True, DARKGRAY)
    pressKeyRect = pressKeySurf.get_rect()
    pressKeyRect.topleft = (WINDOWWIDTH - 200, WINDOWHEIGHT - 30)
    DISPLAYSURF.blit(pressKeySurf, pressKeyRect)


# Checks for any key during the game over or start screen.
def checkForKeyPress():
    for event in pygame.event.get():
        if event.type == QUIT:      #event is quit 
            terminate()
        elif event.type == KEYDOWN:
            if event.key == K_ESCAPE:   #event is escape key
                terminate()
            else:
                runGame()   #key found return with it
    # no quit or key events in queue so return None    
    return None


# Title screen function
def showStartScreen():
    DISPLAYSURF.fill(BGCOLOR)
    pygame.display.update() # Debug
    titleFont = pygame.font.Font('freesansbold.ttf', 100)
    titleSurf1 = titleFont.render('Mario Beat!', True, WHITE, DARKGREEN)
    titleSurf2 = titleFont.render('The Game That', True, GREEN)

    degrees1 = 0
    degrees2 = 0

    pygame.event.get()  #clear out event queue
    
    while True:
        DISPLAYSURF.fill(BGCOLOR)
        rotatedSurf1 = pygame.transform.rotate(titleSurf1, degrees1)
        rotatedRect1 = rotatedSurf1.get_rect()
        rotatedRect1.center = (WINDOWWIDTH / 2, WINDOWHEIGHT / 2)
        DISPLAYSURF.blit(rotatedSurf1, rotatedRect1)

        rotatedSurf2 = pygame.transform.rotate(titleSurf2, degrees2)
        rotatedRect2 = rotatedSurf2.get_rect()
        rotatedRect2.center = (WINDOWWIDTH / 2, WINDOWHEIGHT / 2)
        DISPLAYSURF.blit(rotatedSurf2, rotatedRect2)

        drawPressKeyMsg()
        if checkForKeyPress():
            return
        pygame.display.update()
        FPSCLOCK.tick(FPS)
        degrees1 += 3 # rotate by 3 degrees each frame
        degrees2 += 7 # rotate by 7 degrees each frame


# Quit function
def terminate():
    pygame.quit()
    sys.exit()


# Lose Function
def showGameOverScreen():
    DISPLAYSURF.fill(BGCOLOR)
    pygame.display.update() # Debug
    gameOverFont = pygame.font.Font('freesansbold.ttf', 150)
    gameSurf = gameOverFont.render('YOU LOSE!', True, WHITE)
    overSurf = gameOverFont.render('Try again!', True, WHITE)
    gameRect = gameSurf.get_rect()
    overRect = overSurf.get_rect()
    gameRect.midtop = (WINDOWWIDTH / 2, 10)
    overRect.midtop = (WINDOWWIDTH / 2, gameRect.height + 10 + 25)

    DISPLAYSURF.blit(gameSurf, gameRect)
    DISPLAYSURF.blit(overSurf, overRect)
    drawPressKeyMsg()
    pygame.display.update()
    pygame.time.wait(500)
    pygame.event.get()  #clear out event queue 
    while True:
        if checkForKeyPress():
            return
        pygame.time.wait(100)


# Win function
def showGameWinScreen():
    DISPLAYSURF.fill(BGCOLOR)
    pygame.display.update() # Debug
    gameOverFont = pygame.font.Font('freesansbold.ttf', 25)
    gameSurf = gameOverFont.render('You win, Mario.  Now you can say, "The only game', True, WHITE)
    overSurf = gameOverFont.render('that I have ever beaten is The Game That Mario Beat!"', True, WHITE)
    gameRect = gameSurf.get_rect()
    overRect = overSurf.get_rect()
    gameRect.midtop = (WINDOWWIDTH / 2, 10)
    overRect.midtop = (WINDOWWIDTH / 2, gameRect.height + 10 + 25)

    DISPLAYSURF.blit(gameSurf, gameRect)
    DISPLAYSURF.blit(overSurf, overRect)
    drawPressKeyMsg()
    pygame.display.update()
    pygame.time.wait(500)
    pygame.event.get()  #clear out event queue 
    while True:
        if checkForKeyPress():
            return
        pygame.time.wait(100)


# This runs the functions defined above.
if __name__ == '__main__':
    main()
