import pygame 

#--------------------------------------------
pygame.init()

# Define some colors
BLACK = ( 0, 0, 0)
WHITE = ( 255, 255, 255)
GREEN = ( 0, 255, 0)
RED = ( 255, 0, 0)
BLUE = (0, 0, 255)
PURPLE = (255, 0, 255)
GREY = (210, 210 ,210)

FONT = pygame.font.SysFont('Arial', 30, bold=True, italic=False)


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

cImgPosition = (35,125)
pImgPosition = (385,125)

cBGPosition = (20,100)
pBGPosition = (370,100)

carryOn = True
 
clock = pygame.time.Clock()


#--------------------------------------------

 

while carryOn:

    for event in pygame.event.get():
        if event.type == pygame.QUIT: 
              carryOn = False 
 
    # --- Game logic 

    
    
    # --- Drawing background code 
    screen.fill(WHITE)

    pygame.draw.rect(screen, BLACK, [10, 0, sWIDTH/2 - 20, sHEIGHT - 10],1)
    pygame.draw.rect(screen, BLACK, [sWIDTH/2 + 10, 0, sWIDTH/2 - 20, sHEIGHT - 10],1)

    cTitle = FONT.render('COMPUTER',True, BLACK)
    screen.blit(cTitle,(100, 5))

    pTitle = FONT.render('PLAYER',True, BLACK)
    screen.blit(pTitle,(sWIDTH - 230, 5))

    # --- Drawing chaging code

    if winner == 'player':
        cBG.fill(RED)
        pBG.fill(GREEN)
    elif winner == 'computer':
        cBG.fill(GREEN)
        pBG.fill(RED)
    elif winner == 'tie':
        cBG.fill(PURPLE)
        pBG.fill(PURPLE)      
    else:
        cBG.fill(GREY)
        pBG.fill(GREY)

    screen.blit(cBG,cBGPosition)
    screen.blit(pBG,pBGPosition)
    screen.blit(cImg,cImgPosition)
    screen.blit(pImg,pImgPosition)

    cScoreText = FONT.render(str(cScore),True,BLACK)
    screen.blit(cScoreText,(165, 50))
    pScoreText = FONT.render(str(pScore),True,BLACK)
    screen.blit(pScoreText,(515, 50))


    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()
    
    # --- Limit to 60 frames per second
    clock.tick(60)

#Once we have exited the main program loop we can stop the game engine:
pygame.quit()