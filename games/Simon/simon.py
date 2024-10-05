# import random
# import sys
# import time
# import pygame
# from pygame.locals import *

# FPS = 60
# WINDOWWIDTH = 720
# WINDOWHEIGHT = 720
# FLASHSPEED = 500  # in milliseconds
# FLASHDELAY = 200  # in milliseconds
# BUTTONSIZE = 200
# BUTTONGAPSIZE = 20
# TIMEOUT = 5  # seconds before game over if no button is pushed.

# WHITE = (255, 255, 255)
# BLACK = (0, 0, 0)
# BRIGHTRED = (255, 0, 0)
# RED = (155, 0, 0)
# BRIGHTGREEN = (0, 255, 0)
# GREEN = (0, 155, 0)
# BRIGHTBLUE = (0, 0, 255)
# BLUE = (0, 0, 155)
# BRIGHTYELLOW = (255, 255, 0)
# YELLOW = (155, 155, 0)
# DARKGRAY = (40, 40, 40)
# bgColor = BLACK

# XMARGIN = int((WINDOWWIDTH - (2 * BUTTONSIZE) - BUTTONGAPSIZE) / 2)
# YMARGIN = int((WINDOWHEIGHT - (2 * BUTTONSIZE) - BUTTONGAPSIZE) / 2)

# # Rect objects for each of the four buttons
# YELLOWRECT = pygame.Rect(XMARGIN, YMARGIN, BUTTONSIZE, BUTTONSIZE)
# BLUERECT = pygame.Rect(XMARGIN + BUTTONSIZE + BUTTONGAPSIZE, YMARGIN, BUTTONSIZE, BUTTONSIZE)
# REDRECT = pygame.Rect(XMARGIN, YMARGIN + BUTTONSIZE + BUTTONGAPSIZE, BUTTONSIZE, BUTTONSIZE)
# GREENRECT = pygame.Rect(XMARGIN + BUTTONSIZE + BUTTONGAPSIZE, YMARGIN + BUTTONSIZE + BUTTONGAPSIZE, BUTTONSIZE, BUTTONSIZE)

# def start_game(DISPLAYSURF):
#     global FPSCLOCK, BEEP1, BEEP2, BEEP3, BEEP4

#     FPSCLOCK = pygame.time.Clock()

#     # Load the sound files
#     BEEP1 = pygame.mixer.Sound('assets-SIMON/beep1.ogg')
#     BEEP2 = pygame.mixer.Sound('assets-SIMON/beep2.ogg')
#     BEEP3 = pygame.mixer.Sound('assets-SIMON/beep3.ogg')
#     BEEP4 = pygame.mixer.Sound('assets-SIMON/beep4.ogg')

#     # Initialize some variables for a new game
#     pattern = []  # stores the pattern of colors
#     currentStep = 0  # the color the player must push next
#     lastClickTime = 0  # timestamp of the player's last button push
#     score = 0
#     waitingForInput = False  # when False, the pattern is playing

#     while True:  # main game loop
#         clickedButton = None  # button that was clicked (set to YELLOW, RED, GREEN, or BLUE)
#         DISPLAYSURF.fill(BLACK)
#         drawButtons(DISPLAYSURF)

#         checkForQuit()
#         for event in pygame.event.get():  # event handling loop
#             if event.type == MOUSEBUTTONUP:
#                 mousex, mousey = event.pos
#                 clickedButton = getButtonClicked(mousex, mousey)
#             elif event.type == KEYDOWN:
#                 if event.key == K_q:
#                     clickedButton = YELLOW
#                 elif event.key == K_w:
#                     clickedButton = BLUE
#                 elif event.key == K_a:
#                     clickedButton = RED
#                 elif event.key == K_s:
#                     clickedButton = GREEN

#         if not waitingForInput:
#             # play the pattern
#             pygame.display.update()
#             pygame.time.wait(1000)
#             pattern.append(random.choice((YELLOW, BLUE, RED, GREEN)))
#             for button in pattern:
#                 flashButtonAnimation(button, DISPLAYSURF)
#                 pygame.time.wait(FLASHDELAY)
#             waitingForInput = True
#         else:
#             # wait for the player to enter buttons
#             if clickedButton and clickedButton == pattern[currentStep]:
#                 flashButtonAnimation(clickedButton, DISPLAYSURF)
#                 currentStep += 1
#                 lastClickTime = time.time()

#                 if currentStep == len(pattern):
#                     score += 1
#                     # Check if score reached 5
#                     if score >= 5:
#                         return  # Regresar al menú principal
#                     waitingForInput = False
#                     currentStep = 0  # reset back to first step

#             elif (clickedButton and clickedButton != pattern[currentStep]) or (currentStep != 0 and time.time() - TIMEOUT > lastClickTime):
#                 gameOverAnimation(DISPLAYSURF)
#                 # reset the variables for a new game:
#                 pattern = []
#                 currentStep = 0
#                 waitingForInput = False
#                 score = 0
#                 pygame.time.wait(1000)

#         pygame.display.update()
#         FPSCLOCK.tick(FPS)



# def terminate():
#     pygame.quit()
#     sys.exit()

# def checkForQuit():
#     for event in pygame.event.get(QUIT):  # get all the QUIT events
#         terminate()  # terminate if any QUIT events are present
#     for event in pygame.event.get(KEYUP):  # get all the KEYUP events
#         if event.key == K_ESCAPE:
#             terminate()  # terminate if the KEYUP event was for the Esc key
#         pygame.event.post(event)  # put the other KEYUP event objects back

# def flashButtonAnimation(color, DISPLAYSURF, animationSpeed=50):
#     if color == YELLOW:
#         sound = BEEP1
#         flashColor = BRIGHTYELLOW
#         rectangle = YELLOWRECT
#     elif color == BLUE:
#         sound = BEEP2
#         flashColor = BRIGHTBLUE
#         rectangle = BLUERECT
#     elif color == RED:
#         sound = BEEP3
#         flashColor = BRIGHTRED
#         rectangle = REDRECT
#     elif color == GREEN:
#         sound = BEEP4
#         flashColor = BRIGHTGREEN
#         rectangle = GREENRECT

#     origSurf = DISPLAYSURF.copy()
#     flashSurf = pygame.Surface((BUTTONSIZE, BUTTONSIZE))
#     flashSurf = flashSurf.convert_alpha()
#     r, g, b = flashColor
#     sound.play()
#     for start, end, step in ((0, 255, 1), (255, 0, -1)):  # animation loop
#         for alpha in range(start, end, animationSpeed * step):
#             checkForQuit()
#             DISPLAYSURF.blit(origSurf, (0, 0))
#             flashSurf.fill((r, g, b, alpha))
#             DISPLAYSURF.blit(flashSurf, rectangle.topleft)
#             pygame.display.update()
#             FPSCLOCK.tick(FPS)
#     DISPLAYSURF.blit(origSurf, (0, 0))

# def drawButtons(DISPLAYSURF):
#     pygame.draw.rect(DISPLAYSURF, YELLOW, YELLOWRECT)
#     pygame.draw.rect(DISPLAYSURF, BLUE, BLUERECT)
#     pygame.draw.rect(DISPLAYSURF, RED, REDRECT)
#     pygame.draw.rect(DISPLAYSURF, GREEN, GREENRECT)

# def gameOverAnimation(DISPLAYSURF, color=WHITE, animationSpeed=50):
#     origSurf = DISPLAYSURF.copy()
#     flashSurf = pygame.Surface(DISPLAYSURF.get_size())
#     flashSurf = flashSurf.convert_alpha()
#     BEEP1.play()  # play all four beeps at the same time
#     BEEP2.play()
#     BEEP3.play()
#     BEEP4.play()
#     r, g, b = color
#     for i in range(3):  # do the flash 3 times
#         for start, end, step in ((0, 255, 1), (255, 0, -1)):
#             for alpha in range(start, end, animationSpeed * step):  # animation loop
#                 checkForQuit()
#                 flashSurf.fill((r, g, b, alpha))
#                 DISPLAYSURF.blit(origSurf, (0, 0))
#                 DISPLAYSURF.blit(flashSurf, (0, 0))
#                 drawButtons(DISPLAYSURF)
#                 pygame.display.update()
#                 FPSCLOCK.tick(FPS)

# def getButtonClicked(x, y):
#     if YELLOWRECT.collidepoint((x, y)):
#         return YELLOW
#     elif BLUERECT.collidepoint((x, y)):
#         return BLUE
#     elif REDRECT.collidepoint((x, y)):
#         return RED
#     elif GREENRECT.collidepoint((x, y)):
#         return GREEN
#     return None


import random
import sys
import time
import pygame
from pygame.locals import *

FPS = 60
WINDOWWIDTH = 720
WINDOWHEIGHT = 720
FLASHSPEED = 500  # in milliseconds
FLASHDELAY = 200  # in milliseconds
BUTTONSIZE = 150
BUTTONGAPSIZE = 20
TIMEOUT = 5  # seconds before game over if no button is pushed.

WHITE = (255, 255, 255)
BRIGHTRED = (255, 0, 0)
RED = (155, 0, 0)
BRIGHTGREEN = (0, 255, 0)
GREEN = (0, 155, 0)
BRIGHTBLUE = (0, 0, 255)
BLUE = (0, 0, 155)
BRIGHTYELLOW = (255, 255, 0)
YELLOW = (155, 155, 0)
DARKGRAY = (40, 40, 40)

XMARGIN = int((WINDOWWIDTH - (2 * BUTTONSIZE) - BUTTONGAPSIZE) / 2)
YMARGIN = int((WINDOWHEIGHT - (2 * BUTTONSIZE) - BUTTONGAPSIZE) / 2) + 90

# Rect objects for each of the four buttons
YELLOWRECT = pygame.Rect(XMARGIN, YMARGIN, BUTTONSIZE, BUTTONSIZE)
BLUERECT = pygame.Rect(XMARGIN + BUTTONSIZE + BUTTONGAPSIZE, YMARGIN, BUTTONSIZE, BUTTONSIZE)
REDRECT = pygame.Rect(XMARGIN, YMARGIN + BUTTONSIZE + BUTTONGAPSIZE, BUTTONSIZE, BUTTONSIZE)
GREENRECT = pygame.Rect(XMARGIN + BUTTONSIZE + BUTTONGAPSIZE, YMARGIN + BUTTONSIZE + BUTTONGAPSIZE, BUTTONSIZE, BUTTONSIZE)

def start_game(DISPLAYSURF):
    global FPSCLOCK, BEEP1, BEEP2, BEEP3, BEEP4

    FPSCLOCK = pygame.time.Clock()

    # Load the sound files
    BEEP1 = pygame.mixer.Sound('games/Simon/assets-SIMON/beep1.ogg')
    BEEP2 = pygame.mixer.Sound('games/Simon/assets-SIMON/beep2.ogg')
    BEEP3 = pygame.mixer.Sound('games/Simon/assets-SIMON/beep3.ogg')
    BEEP4 = pygame.mixer.Sound('games/Simon/assets-SIMON/beep4.ogg')

    # Load the background image
    background_image = pygame.image.load('fondo5FRAME.png')  # Cambia la ruta a tu imagen

    # Initialize some variables for a new game
    pattern = []  # stores the pattern of colors
    currentStep = 0  # the color the player must push next
    lastClickTime = 0  # timestamp of the player's last button push
    score = 0
    waitingForInput = False  # when False, the pattern is playing

    while True:  # main game loop
        clickedButton = None  # button that was clicked (set to YELLOW, RED, GREEN, or BLUE)
        DISPLAYSURF.blit(background_image, (0, 0))  # Dibuja la imagen de fondo
        drawButtons(DISPLAYSURF)

        checkForQuit()
        for event in pygame.event.get():  # event handling loop
            if event.type == MOUSEBUTTONUP:
                mousex, mousey = event.pos
                clickedButton = getButtonClicked(mousex, mousey)
            elif event.type == KEYDOWN:
                if event.key == K_q:
                    clickedButton = YELLOW
                elif event.key == K_w:
                    clickedButton = BLUE
                elif event.key == K_a:
                    clickedButton = RED
                elif event.key == K_s:
                    clickedButton = GREEN

        if not waitingForInput:
            # play the pattern
            pygame.display.update()
            pygame.time.wait(1000)
            pattern.append(random.choice((YELLOW, BLUE, RED, GREEN)))
            for button in pattern:
                flashButtonAnimation(button, DISPLAYSURF)
                pygame.time.wait(FLASHDELAY)
            waitingForInput = True
        else:
            # wait for the player to enter buttons
            if clickedButton and clickedButton == pattern[currentStep]:
                flashButtonAnimation(clickedButton, DISPLAYSURF)
                currentStep += 1
                lastClickTime = time.time()

                if currentStep == len(pattern):
                    score += 1
                    # Check if score reached 5
                    if score >= 5:
                        return  # Regresar al menú principal
                    waitingForInput = False
                    currentStep = 0  # reset back to first step

            elif (clickedButton and clickedButton != pattern[currentStep]) or (currentStep != 0 and time.time() - TIMEOUT > lastClickTime):
                gameOverAnimation(DISPLAYSURF)
                # reset the variables for a new game:
                pattern = []
                currentStep = 0
                waitingForInput = False
                score = 0
                pygame.time.wait(1000)

        pygame.display.update()
        FPSCLOCK.tick(FPS)

# Las demás funciones permanecen iguales...

def terminate():
    pygame.quit()
    sys.exit()

def checkForQuit():
    for event in pygame.event.get(QUIT):  # get all the QUIT events
        terminate()  # terminate if any QUIT events are present
    for event in pygame.event.get(KEYUP):  # get all the KEYUP events
        if event.key == K_ESCAPE:
            terminate()  # terminate if the KEYUP event was for the Esc key
        pygame.event.post(event)  # put the other KEYUP event objects back

def flashButtonAnimation(color, DISPLAYSURF, animationSpeed=50):
    if color == YELLOW:
        sound = BEEP1
        flashColor = BRIGHTYELLOW
        rectangle = YELLOWRECT
    elif color == BLUE:
        sound = BEEP2
        flashColor = BRIGHTBLUE
        rectangle = BLUERECT
    elif color == RED:
        sound = BEEP3
        flashColor = BRIGHTRED
        rectangle = REDRECT
    elif color == GREEN:
        sound = BEEP4
        flashColor = BRIGHTGREEN
        rectangle = GREENRECT

    origSurf = DISPLAYSURF.copy()
    flashSurf = pygame.Surface((BUTTONSIZE, BUTTONSIZE))
    flashSurf = flashSurf.convert_alpha()
    r, g, b = flashColor
    sound.play()
    for start, end, step in ((0, 255, 1), (255, 0, -1)):  # animation loop
        for alpha in range(start, end, animationSpeed * step):
            checkForQuit()
            DISPLAYSURF.blit(origSurf, (0, 0))
            flashSurf.fill((r, g, b, alpha))
            DISPLAYSURF.blit(flashSurf, rectangle.topleft)
            pygame.display.update()
            FPSCLOCK.tick(FPS)
    DISPLAYSURF.blit(origSurf, (0, 0))

def drawButtons(DISPLAYSURF):
    pygame.draw.rect(DISPLAYSURF, YELLOW, YELLOWRECT)
    pygame.draw.rect(DISPLAYSURF, BLUE, BLUERECT)
    pygame.draw.rect(DISPLAYSURF, RED, REDRECT)
    pygame.draw.rect(DISPLAYSURF, GREEN, GREENRECT)

def gameOverAnimation(DISPLAYSURF, color=WHITE, animationSpeed=50):
    origSurf = DISPLAYSURF.copy()
    flashSurf = pygame.Surface(DISPLAYSURF.get_size())
    flashSurf = flashSurf.convert_alpha()
    BEEP1.play()  # play all four beeps at the same time
    BEEP2.play()
    BEEP3.play()
    BEEP4.play()
    r, g, b = color
    for i in range(3):  # do the flash 3 times
        for start, end, step in ((0, 255, 1), (255, 0, -1)):
            for alpha in range(start, end, animationSpeed * step):  # animation loop
                checkForQuit()
                flashSurf.fill((r, g, b, alpha))
                DISPLAYSURF.blit(origSurf, (0, 0))
                DISPLAYSURF.blit(flashSurf, (0, 0))
                drawButtons(DISPLAYSURF)
                pygame.display.update()
                FPSCLOCK.tick(FPS)

def getButtonClicked(x, y):
    if YELLOWRECT.collidepoint((x, y)):
        return YELLOW
    elif BLUERECT.collidepoint((x, y)):
        return BLUE
    elif REDRECT.collidepoint((x, y)):
        return RED
    elif GREENRECT.collidepoint((x, y)):
        return GREEN
    return None
