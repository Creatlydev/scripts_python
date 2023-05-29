import pygame
from copy import deepcopy
import time
import sys



SIZE = (1000, 800)

pygame.init()




def show_Generation(pantalla, fuente, texto, color, dimensiones) :
    type_letter = pygame.font.Font(fuente, dimensiones)
    superfic = type_letter.render(texto, True, color)
    rect = superfic.get_rect()
    rect.x = 800
    rect.y = 715
    pantalla.blit(superfic, rect)



SCREEN = pygame.display.set_mode(SIZE)
bg = 25, 25, 25
SCREEN.fill(bg)

consolas = pygame.font.match_font('consolas')
times = pygame.font.match_font('times')
arial = pygame.font.match_font('arial')
courier = pygame.font.match_font('courier')

nxC, nyC = 60, 60
width_cell = SIZE[0] / nxC
height_cell = (SIZE[1] - 100) / nyC

gameState = [[0] * nyC for i in range(nxC)]


gameState[5][3] = 1
gameState[5][4] = 1
gameState[5][5] = 1
gameState[5][6] = 1
gameState[5][7] = 1

gameState[8][3] = 1
gameState[8][4] = 1
gameState[8][5] = 1
gameState[8][6] = 1
gameState[8][7] = 1

puntuaction = 0
pauseExcept = False


while True :

    newGameState = deepcopy(gameState) 

    SCREEN.fill(bg)
    time.sleep(.2)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.KEYDOWN :
            if event.key == pygame.K_SPACE :
                pauseExcept = not pauseExcept

        
        mouseClick = pygame.mouse.get_pressed()

        if sum(mouseClick) > 0 :
            posX, posY = pygame.mouse.get_pos()
            cellX, cellY= int(posX // width_cell), int(posY // height_cell)
            newGameState[cellX][cellY] = not mouseClick[2]
    
    if not pauseExcept :
            puntuaction += 1


    for x in range(nxC) :
        for y in range(nyC) :
            
            if not pauseExcept :
                n_height = (gameState[(x-1) % nxC][(y-1) % nyC]) + \
                    (gameState[x % nxC][(y-1) % nyC]) + \
                    (gameState[(x+1) % nxC][(y-1) % nyC]) + \
                    (gameState[(x-1) % nxC][y % nyC]) + \
                    (gameState[(x+1) % nxC][y % nyC]) + \
                    (gameState[(x-1) % nxC][(y+1) % nyC]) + \
                    (gameState[x % nxC][(y+1) % nyC]) + \
                    (gameState[(x+1) % nxC][(y+1) % nyC])
            

                #Rule 01
                if newGameState[x][y] == 0 and (n_height == 3) :
                    newGameState[x][y] = 1

                #Rule 02
                if newGameState[x][y] == 1 and (n_height < 2 or n_height > 3) :
                    newGameState[x][y] = 0

            poly = [(x * width_cell, y * height_cell),
                    ((x+1) * width_cell, y * height_cell),
                    ((x+1) * width_cell, (y+1) * height_cell),
                    (x * width_cell, (y+1) * height_cell)
                ]

            
            if newGameState[x][y] == 0 :
                pygame.draw.polygon(SCREEN, (128, 128, 128), poly, 1)
            else :
                pygame.draw.polygon(SCREEN, (255, 255, 255), poly, 0) 
            
            square = pygame.draw.rect(SCREEN, (100, 100, 100), (0, 700, 1000, 100))


    gameState = newGameState

    show_Generation(SCREEN, consolas, str(puntuaction), (255, 0, 0), 80)
    
    pygame.display.flip()





12 / 2 = 6 / 2 = 3 = 9+1 = 10 = 1

