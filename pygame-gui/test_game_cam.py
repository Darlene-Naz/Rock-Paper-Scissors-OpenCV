import pygame
import cv2
import numpy as np
import keras as k
import tensorflow as tf
from tensorflow.keras.models import load_model

# --- In utils
ROCK = 0
PAPER = 1
SCISSORS = 2

# text labels corresponding to gestures
gestureTxt = {ROCK: 'rock', PAPER: 'paper', SCISSORS: 'scissors'}

# --- Init
print("Initializing Camera...")
cap = cv2.VideoCapture(0)
print("Camera Window Loaded!")

pygame.init()

model= load_model(filepath="C:/Users/Darlene/Desktop/GitHub/Rock-Paper-Scissors-OpenCV-Game/models/final_custom_model7.h5")


# Define some default colors, fonts and msgs
font = cv2.FONT_HERSHEY_SIMPLEX
default_msg = 0

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
PURPLE = (255, 0, 255)
GREY = (210, 210, 210)

FONT = pygame.font.SysFont("Arial", 30, bold=True, italic=False)


# Open a new window
sWIDTH = 700
sHEIGHT = 500
sWINDOW = (sWIDTH, sHEIGHT)

screen = pygame.display.set_mode(sWINDOW)
pygame.display.set_caption("Rock Paper Scissor")

pScore = 0
cScore = 0
winner = None

pImg = pygame.Surface((280, 335))
cImg = pygame.Surface((280, 335))

pBG = pygame.Surface((310, 380))
cBG = pygame.Surface((310, 380))

cImgPosition = (35, 125)
pImgPosition = (385, 125)

cBGPosition = (20, 100)
pBGPosition = (370, 100)

carryOn = True

clock = pygame.time.Clock()


# --------------------------------------------


while carryOn:
    
    # --- opencv pImg

    ret, frame = cap.read()
    frame = np.rot90(frame)

    # define region of interest
    roi = frame[0:280, 0:335]
    rgb_roi = cv2.cvtColor(roi, cv2.COLOR_BGR2RGB)
    
    # pred
    x=cv2.resize(rgb_roi,(100,100))
    x = x / 255
    img_arr=np.array(x)
    img = np.array([img_arr])
    print(img.shape)
    y=model.predict(img)
    print(np.max(y))
    print(np.argmax(y,axis=1))
    print(gestureTxt[int(np.argmax(y,axis=1))])
    

    pImg = pygame.surfarray.make_surface(rgb_roi)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            carryOn = False

    # --- Game logic

    # --- Drawing background code
    screen.fill(WHITE)

    pygame.draw.rect(screen, BLACK, [10, 0, sWIDTH / 2 - 20, sHEIGHT - 10], 1)
    pygame.draw.rect(
        screen, BLACK, [sWIDTH / 2 + 10, 0, sWIDTH / 2 - 20, sHEIGHT - 10], 1
    )

    cTitle = FONT.render("COMPUTER", True, BLACK)
    screen.blit(cTitle, (100, 5))

    pTitle = FONT.render("PLAYER", True, BLACK)
    screen.blit(pTitle, (sWIDTH - 230, 5))

    # --- Drawing chaging code

    if winner == "player":
        cBG.fill(RED)
        pBG.fill(GREEN)
    elif winner == "computer":
        cBG.fill(GREEN)
        pBG.fill(RED)
    elif winner == "tie":
        cBG.fill(PURPLE)
        pBG.fill(PURPLE)
    else:
        cBG.fill(GREY)
        pBG.fill(GREY)

    screen.blit(cBG, cBGPosition)
    screen.blit(pBG, pBGPosition)
    screen.blit(cImg, cImgPosition)
    screen.blit(pImg, pImgPosition)

    cScoreText = FONT.render(str(cScore), True, BLACK)
    screen.blit(cScoreText, (165, 50))
    pScoreText = FONT.render(str(pScore), True, BLACK)
    screen.blit(pScoreText, (515, 50))

    # --- Update the screen
    pygame.display.flip()

    # --- Limit to 60 frames per second
    clock.tick(60)

# --- Exit code
pygame.quit()
cap.release()
cv2.destroyAllWindows()
