import pygame
import numpy as np
import cv2
import sys


class RockPaperScissor:
    def __init__(self, totalScore=3):
        pygame.init()

        self.carryOn = True

        self.clock = pygame.time.Clock()

        # Define some default colors and fonts
        self.BLACK = (0, 0, 0)
        self.WHITE = (255, 255, 255)
        self.GREEN = (0, 255, 0)
        self.RED = (255, 0, 0)
        self.BLUE = (0, 0, 255)
        self.PURPLE = (255, 0, 255)
        self.GREY = (210, 210, 210)
        self.SPRING_GREEN = pygame.Color("springgreen")

        self.FONT = pygame.font.SysFont("Arial", 30, bold=True, italic=False)
        self.FONT_TIMER = pygame.font.Font(None, 54)

        self.DISPLAY_ICON = "utils/images/gaming.png"
        self.CLOCK = "utils/images/time.png"
        self.MSG_BUBBLE = "utils/images/comment.png"

        # scores
        self.pScore = 0
        self.cScore = 0
        self.totalScore = totalScore
        self.winner = None

        # timer
        self.duration = 0
        self.timer_started = False

        # Open a new window
        self.sWIDTH = 700
        self.sHEIGHT = 500
        self.sWINDOW = (self.sWIDTH, self.sHEIGHT)

        self.screen = pygame.display.set_mode(self.sWINDOW)
        pygame.display.set_caption("Rock Paper Scissor")
        self.icon = pygame.image.load(self.DISPLAY_ICON)
        pygame.display.set_icon(self.icon)

        # main components
        self.pImg = pygame.Surface((280, 335))
        self.cImg = pygame.Surface((280, 335))

        self.pBG = pygame.Surface((310, 380))
        self.cBG = pygame.Surface((310, 380))

        self.cImgPosition = (35, 125)
        self.pImgPosition = (385, 125)

        self.cBGPosition = (20, 100)
        self.pBGPosition = (370, 100)

    def draw_ui(self):

        # --- Drawing background code
        self.screen.fill(self.WHITE)

        pygame.draw.rect(
            self.screen, self.GREY, [10, 0, self.sWIDTH / 2 - 20, self.sHEIGHT - 10], 0
        )
        pygame.draw.rect(
            self.screen,
            self.GREY,
            [self.sWIDTH / 2 + 10, 0, self.sWIDTH / 2 - 20, self.sHEIGHT - 10],
            0,
        )

        cTitle = self.FONT.render("COMPUTER", True, self.BLACK)
        self.screen.blit(cTitle, (100, 5))

        pTitle = self.FONT.render("PLAYER", True, self.BLACK)
        self.screen.blit(pTitle, (self.sWIDTH - 230, 5))

        # --- Drawing chaging code

        # c, p BG, IMG
        if self.winner == "player":
            self.cBG.fill(self.RED)
            self.pBG.fill(self.GREEN)
        elif self.winner == "computer":
            self.cBG.fill(self.GREEN)
            self.pBG.fill(self.RED)
        elif self.winner == "tie":
            self.cBG.fill(self.PURPLE)
            self.pBG.fill(self.PURPLE)
        else:
            self.cBG.fill(self.GREY)
            self.pBG.fill(self.GREY)

        self.screen.blit(self.cBG, self.cBGPosition)
        self.screen.blit(self.pBG, self.pBGPosition)

        self.screen.blit(self.cImg, self.cImgPosition)
        self.screen.blit(self.pImg, self.pImgPosition)

        clockImg = pygame.image.load(self.CLOCK)
        clockImg.convert()  # will place at (0,0)
        rect = clockImg.get_rect()  # get dimensions of its rect shape
        rect.center = self.sWIDTH // 2, 80
        self.screen.blit(clockImg, rect)

        timerText = self.FONT_TIMER.render(str(self.duration), True, self.SPRING_GREEN)
        self.screen.blit(timerText, (self.sWIDTH // 2 - 10, 75))

        # textBubble = pygame.image.load(
        #     "C:\\Users\\Darlene\\Desktop\\GitHub\\Rock-Paper-Scissors-OpenCV-Game\\pygame-gui\\comment2.png"
        # )
        # textBubble.convert()  # will place at (0,0)
        # rect = textBubble.get_rect()  # get dimensions of its rect shape
        # rect.center = 64, sHEIGHT - 60
        # screen.blit(textBubble, rect)

        cScoreText = self.FONT.render(str(self.cScore), True, self.BLACK)
        self.screen.blit(cScoreText, (165, 50))
        pScoreText = self.FONT.render(str(self.pScore), True, self.BLACK)
        self.screen.blit(pScoreText, (515, 50))

        # --- Update the screen
        pygame.display.flip()

        # --- Limit to 60 frames per second
        self.clock.tick(60)

        if self.cScore == self.totalScore or self.pScore == self.totalScore:
            self.gameOver()

    def gameOver(self, delay=3500):
        # Create surface for Game Over message
        gameOverPopUp = pygame.Surface((400, 200))

        gameOverPopUp.fill(self.WHITE)

        vertices = [(3, 3), (396, 3), (396, 196), (3, 196), (3, 3)]
        pygame.draw.polygon(gameOverPopUp, self.GREY, vertices, 0)

        gameOverText = self.FONT.render("GAME OVER", True, self.BLACK)
        gameOverPopUp.blit(gameOverText, (120, 45))

        if self.pScore > self.cScore:
            self.winner = "PLAYER"
            color = self.GREEN
        else:
            self.winner = "COMPUTER"
            color = self.RED

        winnerText = self.FONT.render("{} WINS!".format(self.winner), True, color)
        gameOverPopUp.blit(winnerText, (110, 110))

        pos = (self.sWIDTH / 2 - 200, 175)
        self.screen.blit(gameOverPopUp, pos)

        pygame.display.flip()
        pygame.time.wait(delay)

        if self.carryOn:
            self.reset()
        else:
            self.quit()

    def startTimer(self, duration):
        self.timer_started = True
        self.duration = duration

    def stopTimer(self):
        self.timer_started = False
        self.duration = 0

    def updateTimer(self):
        if self.timer_started:
            pygame.time.wait(1000)
            if self.duration > 0:
                self.duration = self.duration - 1

    def decideWinner(self, c_num, p_num):
        if p_num == c_num:
            self.updateScores("tie")
            print("[GAME] Results: Tie!")
        elif (
            (p_num == 2 and c_num == 0)
            or (p_num == 1 and c_num == 2)
            or (p_num == 0 and c_num == 1)
        ):
            self.updateScores("player")
            print("[GAME] Results: Player wins this round!")
        else:
            self.updateScores("computer")
            print("[GAME] Results: Computer wins this round!")

    def updateScores(self, winner=None):
        self.winner = winner
        if self.winner == "computer":
            self.cScore += 1
        elif winner == "player":
            self.pScore += 1
        print("[GAME] Score: Computer {} & Player {}".format(self.cScore, self.pScore))

    def setCImg(self, num):
        img = cv2.imread("utils/images/" + str(num) + ".png", cv2.IMREAD_COLOR)
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        img = cv2.resize(img, (280, 335))
        img = np.rot90(img)
        self.cImg = pygame.surfarray.make_surface(img[:, ::-1, :])

    def setPImg(self, rgb_roi):
        self.pImg = pygame.surfarray.make_surface(rgb_roi)

    def quit(self):
        self.carryOn = False
        pygame.quit()
        sys.exit()

    def reset(self):
        self.winner = None
        self.pScore = 0
        self.cScore = 0
