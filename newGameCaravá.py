# -*- coding: utf-8 -*-
import pygame
import numpy as np #alias de numpy
import time

pygame.init() 

width, height = 500, 500

bg = 25, 25, 25

screen  = pygame.display.set_mode((height, width))
screen.fill(bg)

# Tamaño de nuestra matriz
nxC, nyC = 80, 80

# Estado de las celdas. Viva = 1 / Muerta = 0
gameState = np.zeros((nxC,  nyC))

#dimensiones de cada celda individual
dimCW = width / nxC
dimCH = height / nyC

xpos = 0 
ypos = 0
bxpos = xpos
bypos = ypos



pauseExect = True
stay = True
tiempox = 0
tiempoy = 0
xvel = 0
yvel = 0

# Bucle de ejecución
while stay:

    tiempox = tiempox + 1
    tiempoy = tiempoy + 1
    # Copiamos la matriz del estado anterior
    # #para representar la matriz en el nuevo estado
    gameState = np.copy(gameState)

    # Ralentizamos la ejecución a 0.1 segundos
    time.sleep(0.1)

    # Limpiamos la pantalla
    screen.fill(bg)

    # Registramos eventos de teclado y ratón.
    ev = pygame.event.get()

    # Cada vez que identificamos un evento lo procesamos
    for event in ev:
        # Detectamos si se presiona una tecla.
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                xvel = xvel - 1
            elif event.key == pygame.K_RIGHT:
                xvel = xvel + 1
            elif event.key == pygame.K_UP:
                yvel = yvel - 1
            elif event.key == pygame.K_DOWN:
                yvel =  yvel + 1                
            else:
                pauseExect = not pauseExect
                
       
        if event.type == pygame.QUIT:
        
            stay = False
            pygame.quit()

        # Detectamos si se presiona el ratón.
        mouseClick = pygame.mouse.get_pressed()

        if sum(mouseClick) > 0:
            posX, posY = pygame.mouse.get_pos()
            celX, celY = int(np.floor(posX / dimCW)), int(np.floor(posY / dimCH))
            gameState[celX, celY] = 1
    
    periodox=6 - abs(xvel)        
    if periodox == 6:
        periodox = 99999999999999999999999999999999999999999999999999999999
    periodoy=6 - abs(yvel)        
    if periodoy == 6:
        periodoy = 99999999999999999999999999999999999999999999999999999999
    
    if tiempox >= periodox: 
        tiempox = 0
        xpos = int(xpos + xvel / abs(xvel))
    if tiempoy >= periodoy: 
        tiempoy = 0
        ypos = ypos + yvel / abs(yvel)
    #Borrado y escritura
    if (xpos != bxpos) or (ypos != bypos):
        
        #AVION
        #cuerpo
        
        gameState[bxpos+50,bypos+50] = 0
        gameState[bxpos+50,bypos+51] = 0
        gameState[bxpos+50,bypos+52] = 0
        gameState[bxpos+50,bypos+53] = 0
        gameState[bxpos+50,bypos+54] = 0
        gameState[bxpos+50,bypos+55] = 0
        gameState[bxpos+50,bypos+56] = 0
        gameState[bxpos+50,bypos+57] = 0
        gameState[bxpos+50,bypos+58] = 0
        gameState[bxpos+50,bypos+59] = 0
        
          #alas
        gameState[bxpos+51,bypos+53] = 0
        gameState[bxpos+49,bypos+53] = 0
        gameState[bxpos+52,bypos+54] = 0
        gameState[bxpos+48,bypos+54] = 0
        gameState[bxpos+53,bypos+55] = 0
        gameState[bxpos+47,bypos+55] = 0
        
        gameState[bxpos+51,bypos+59] = 0
        gameState[bxpos+49,bypos+59] = 0
        
             
        gameState[xpos+50,ypos+50] = 1
        gameState[xpos+50,ypos+51] = 1
        gameState[xpos+50,ypos+52] = 1
        gameState[xpos+50,ypos+53] = 1
        gameState[xpos+50,ypos+54] = 1
        gameState[xpos+50,ypos+55] = 1
        gameState[xpos+50,ypos+56] = 1
        gameState[xpos+50,ypos+57] = 1
        gameState[xpos+50,ypos+58] = 1
        gameState[xpos+50,ypos+59] = 1
        
          #alas
        gameState[xpos+51,ypos+53] = 1
        gameState[xpos+49,ypos+53] = 1
        gameState[xpos+52,ypos+54] = 1
        gameState[xpos+48,ypos+54] = 1
        gameState[xpos+53,ypos+55] = 1
        gameState[xpos+47,ypos+55] = 1
        
        gameState[xpos+51,ypos+59] = 1
        gameState[xpos+49,ypos+59] = 1
        
    
    #Actualizamos la posicion de borrado
    bxpos = xpos
    bypos = ypos
    

    for y in range(0, nxC):
        for x in range (0, nyC):

            # Calculamos el polígono que forma la celda.
            poly = [((x)   * dimCW, y * dimCH),
                    ((x+1) * dimCW, y * dimCH),
                    ((x+1) * dimCW, (y+1) * dimCH),
                    ((x)   * dimCW, (y+1) * dimCH)]

            # Si la celda está "muerta" pintamos un recuadro con borde gris
            if gameState[x, y] == 0:
                pygame.draw.polygon(screen, (40, 40, 40), poly, 1)
           # Si la celda está "viva" pintamos un recuadro relleno de color
            else:
                pygame.draw.polygon(screen, (200, 100, 100), poly, 0)


    # Mostramos el resultado
    pygame.display.flip()
