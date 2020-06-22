import pygame
import random
import numpy as np
import keras as k
import keras.backend as K
import tensorflow as tf
import cv2
from tensorflow.keras.models import load_model

# --- In utils
ROCK = 1
PAPER = 0
SCISSORS = 2

# text labels corresponding to gestures
gestureTxt = {PAPER: "paper", ROCK: "rock", SCISSORS: "scissors"}

# --- Init
print("Initializing Camera...")
cap = cv2.VideoCapture(0)
print("Camera Window Loaded!")

pygame.init()

model = load_model(
    filepath="C:/Users/Darlene/Desktop/GitHub/Rock-Paper-Scissors-OpenCV-Game/models/final_custom_model6.h5"
)


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
SPRING_GREEN = pygame.Color("springgreen")

FONT = pygame.font.SysFont("Arial", 30, bold=True, italic=False)
FONT_TIMER = pygame.font.Font(None, 54)


# Open a new window
sWIDTH = 700
sHEIGHT = 500
sWINDOW = (sWIDTH, sHEIGHT)

screen = pygame.display.set_mode(sWINDOW)
pygame.display.set_caption("Rock Paper Scissor")
icon = pygame.image.load("utils/images/gaming.png")
pygame.display.set_icon(icon)

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
duration = 0
timer_started = False


# --------------------------------------------


while carryOn:

    # --- opencv pImg

    ret, frame = cap.read()
    frame = np.rot90(frame)

    # define region of interest
    roi = frame[0:280, 0:335]
    rgb_roi = cv2.cvtColor(roi, cv2.COLOR_BGR2RGB)

    # pred
    if timer_started:
        pygame.time.wait(1000)
        if duration > 0:
            duration = duration - 1

    if duration == 0 and timer_started:

        no = str(random.randint(0, 2))
        img = cv2.imread("utils/images/" + no + ".png", cv2.IMREAD_COLOR)
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        img = cv2.resize(img, (280, 335))
        img = np.rot90(img)
        cImg = pygame.surfarray.make_surface(img[:, ::-1, :])

        bgr = cv2.cvtColor(rgb_roi, cv2.COLOR_RGB2BGR)
        x = cv2.resize(bgr, (100, 100))
        cv2.imwrite("pygame-gui/img.jpg", x)
        x = x / 255
        img_arr = np.array(x)
        img = np.array([img_arr])
        print(img.shape)
        y = model.predict(img)
        print(np.max(y))
        print(np.argmax(y, axis=1))
        print(gestureTxt[int(np.argmax(y, axis=1))])
        timer_started = not timer_started

    pImg = pygame.surfarray.make_surface(rgb_roi)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            carryOn = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                timer_started = not timer_started
                if timer_started:
                    duration = 3

    # --- Game logic

    # --- Drawing background code
    screen.fill(WHITE)

    pygame.draw.rect(screen, GREY, [10, 0, sWIDTH / 2 - 20, sHEIGHT - 10], 0)
    pygame.draw.rect(
        screen, GREY, [sWIDTH / 2 + 10, 0, sWIDTH / 2 - 20, sHEIGHT - 10], 0
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

    clockImg = pygame.image.load(
        "C:\\Users\\Darlene\\Desktop\\GitHub\\Rock-Paper-Scissors-OpenCV-Game\\pygame-gui\\time.png"
    )
    clockImg.convert()  # will place at (0,0)
    rect = clockImg.get_rect()  # get dimensions of its rect shape
    rect.center = sWIDTH // 2, 80
    screen.blit(clockImg, rect)

    timer_text = FONT_TIMER.render(str(duration), True, SPRING_GREEN)
    screen.blit(timer_text, (sWIDTH // 2 - 10, 75))

    # textBubble = pygame.image.load(
    #     "C:\\Users\\Darlene\\Desktop\\GitHub\\Rock-Paper-Scissors-OpenCV-Game\\pygame-gui\\comment2.png"
    # )
    # textBubble.convert()  # will place at (0,0)
    # rect = textBubble.get_rect()  # get dimensions of its rect shape
    # rect.center = 64, sHEIGHT - 60
    # screen.blit(textBubble, rect)

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
