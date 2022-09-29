# -*- coding: utf-8 -*-

# Apunte clase 15/09

#Juego de la vida 
# Creado en 1970
# Automata
# Reglas sencillas
# Comportamiento caotico

#Reglas 
# *Si viva: con menor de 2 vecinos 
#           vivos, muere(soledad)
#           con mas de 3 vecinos
#           vivos, 3 mas alrededor se muere sobrepobacion


import pygame
import numpy as np
import time

pygame.init()

width, height = 400, 400

bg = 25, 25 ,25

screen  = pygame.display.set_mode((height, width))
screen.fill(bg)

# Tamaño de nuestra matriz
nxC, nyC = 100, 100

# Estado de las celdas. Viva = 1 / Muerta = 0
gameState = np.zeros((nxC,  nyC))

#dimensiones de cada celda individual
dimCW = width / nxC
dimCH = height / nyC

# # Oscilador.
gameState[38, 20] = 1
gameState[39, 20] = 1
gameState[40, 20] = 1

# # Runner 1
gameState[10,5] = 1
gameState[12,5] = 1
gameState[11,6] = 1
gameState[12,6] = 1
gameState[11,7] = 1

# #Runner 2
gameState[5,10] = 1
gameState[5,12] = 1
gameState[6,11] = 1
gameState[6,12] = 1
gameState[7,11] = 1

# #Box 1
# gameState[18,15] = 1
# gameState[17,16] = 1
# gameState[17,15] = 1
# gameState[18,16] = 1

# #Serpent 1
# gameState[30,20] = 1
# gameState[31,20] = 1
# gameState[32,20] = 1
# gameState[32,19] = 1
# gameState[33,19] = 1
# gameState[34,19] = 1

xpos = -10
ypos = -10

#espada
gameState[xpos+13, ypos-10]
gameState[xpos+30,ypos+30] = 1
gameState[xpos+31,ypos+31] = 1
gameState[xpos+32,ypos+32] = 1
gameState[xpos+33,ypos+33] = 1
gameState[xpos+34,ypos+34] = 1
gameState[xpos+35,ypos+35] = 1
gameState[xpos+36,ypos+36] = 1
gameState[xpos+36,ypos+37] = 1
gameState[xpos+37,ypos+37] = 1
gameState[xpos+37,ypos+36] = 1
gameState[xpos+30,ypos+28] = 1
gameState[xpos+30,ypos+27] = 1
gameState[xpos+29,ypos+30] = 1
gameState[xpos+28,ypos+30] = 1
gameState[xpos+30,ypos+29] = 1
gameState[xpos+26,ypos+29] = 1
gameState[xpos+27,ypos+30] = 1
gameState[xpos+25,ypos+28] = 1
gameState[xpos+24,ypos+27] = 1
gameState[xpos+23,ypos+26] = 1
gameState[xpos+22,ypos+25] = 1
gameState[xpos+21,ypos+24] = 1
gameState[xpos+20,ypos+23] = 1
gameState[xpos+19,ypos+22] = 1
gameState[xpos+18,ypos+21] = 1
gameState[xpos+18,ypos+20] = 1
gameState[xpos+18,ypos+19] = 1
gameState[xpos+18,ypos+18] = 1
gameState[xpos+19,ypos+18] = 1
gameState[xpos+20,ypos+18] = 1
gameState[xpos+21,ypos+18] = 1
gameState[xpos+22,ypos+19] = 1
gameState[xpos+23,ypos+20] = 1
gameState[xpos+24,ypos+21] = 1
gameState[xpos+25,ypos+22] = 1
gameState[xpos+26,ypos+23] = 1
gameState[xpos+27,ypos+24] = 1
gameState[xpos+28,ypos+25] = 1
gameState[xpos+29,ypos+26] = 1

#mensaje
#H
# gameState[5,59] = 1
# gameState[5,58] = 1
# gameState[5,57] = 1
# gameState[5,56] = 1
# gameState[5,55] = 1
# gameState[6,57] = 1
# gameState[7,59] = 1
# gameState[7,58] = 1
# gameState[7,57] = 1
# gameState[7,56] = 1
# gameState[7,55] = 1

# #O
# gameState[9,59] = 1
# gameState[9,58] = 1
# gameState[9,57] = 1
# gameState[9,56] = 1
# gameState[9,55] = 1
# gameState[10,59] = 1
# gameState[10,55] = 1
# gameState[11,59] = 1
# gameState[11,58] = 1
# gameState[11,57] = 1
# gameState[11,56] = 1
# gameState[11,55] = 1
# #
# #L
# gameState[13,59] = 1
# gameState[13,58] = 1
# gameState[13,57] = 1
# gameState[13,56] = 1
# gameState[13,55] = 1
# gameState[14,59] = 1
# gameState[15,59] = 1
# #
# #A
# gameState[17,59] = 1
# gameState[17,58] = 1
# gameState[17,57] = 1
# gameState[17,56] = 1
# gameState[17,55] = 1
# gameState[18,55] = 1
# gameState[18,57] = 1
# gameState[19,59] = 1
# gameState[19,58] = 1
# gameState[19,57] = 1
# gameState[19,56] = 1
# gameState[19,55] = 1
# #
# #P
# gameState[22,59] = 1
# gameState[22,58] = 1
# gameState[22,57] = 1
# gameState[22,56] = 1
# gameState[22,55] = 1
# gameState[23,55] = 1
# gameState[24,55] = 1
# gameState[24,56] = 1
# gameState[24,57] = 1
# gameState[23,57] = 1
# #
# #R
# gameState[26,59] = 1
# gameState[26,58] = 1
# gameState[26,57] = 1
# gameState[26,56] = 1
# gameState[26,55] = 1
# gameState[27,55] = 1
# gameState[28,55] = 1
# gameState[28,56] = 1
# gameState[28,57] = 1
# gameState[27,57] = 1
# gameState[27,58] = 1
# gameState[28,59] = 1
# #
# #R
# gameState[30,59] = 1
# gameState[30,58] = 1
# gameState[30,57] = 1
# gameState[30,56] = 1
# gameState[30,55] = 1
# gameState[31,55] = 1
# gameState[32,55] = 1
# gameState[32,56] = 1
# gameState[32,57] = 1
# gameState[31,57] = 1
# gameState[31,58] = 1
# gameState[32,59] = 1
# #
# #O
# gameState[34,59] = 1
# gameState[34,58] = 1
# gameState[34,57] = 1
# gameState[34,56] = 1
# gameState[34,55] = 1
# gameState[35,59] = 1
# gameState[35,55] = 1
# gameState[36,59] = 1
# gameState[36,58] = 1
# gameState[36,57] = 1
# gameState[36,56] = 1
# gameState[36,55] = 1
# #
# #S
# gameState[38,59] = 1
# gameState[38,58] = 0
# gameState[38,57] = 1
# gameState[38,56] = 1
# gameState[38,55] = 1
# gameState[39,59] = 1
# gameState[39,57] = 1
# gameState[39,55] = 1
# gameState[40,59] = 1
# gameState[40,58] = 1
# gameState[40,57] = 1
# gameState[40,56] = 0
# gameState[40,55] = 1














pauseExect = True
stay = True

# Bucle de ejecución
while stay:

    # Copiamos la matriz del estado anterior
    # #para representar la matriz en el nuevo estado
    newGameState = np.copy(gameState)

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
                pass
            elif event.key == pygame.K_RIGHT:
                pass
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
            newGameState[celX, celY] = 1

    for y in range(0, nxC):
        for x in range (0, nyC):

            if not pauseExect:

                # Calculamos el número de vecinos cercanos.
                n_neigh =   gameState[(x - 1) % nxC, (y - 1)  % nyC] + \
                            gameState[(x)     % nxC, (y - 1)  % nyC] + \
                            gameState[(x + 1) % nxC, (y - 1)  % nyC] + \
                            gameState[(x - 1) % nxC, (y)      % nyC] + \
                            gameState[(x + 1) % nxC, (y)      % nyC] + \
                            gameState[(x - 1) % nxC, (y + 1)  % nyC] + \
                            gameState[(x)     % nxC, (y + 1)  % nyC] + \
                            gameState[(x + 1) % nxC, (y + 1)  % nyC]

                # Regla #1 : Una celda muerta con exactamente 3 vecinas vivas, "revive".

                if gameState[x, y] == 0 and n_neigh == 3:
                    newGameState[x, y] = 1

                # Regla #2 : Una celda viva con menos de 2 o más 3 vecinas vinas, "muere".

                elif gameState[x, y] == 1 and (n_neigh < 2 or n_neigh > 3):
                    newGameState[x, y] = 0

            # Calculamos el polígono que forma la celda.
            poly = [((x)   * dimCW, y * dimCH),
                    ((x+1) * dimCW, y * dimCH),
                    ((x+1) * dimCW, (y+1) * dimCH),
                    ((x)   * dimCW, (y+1) * dimCH)]

            # Si la celda está "muerta" pintamos un recuadro con borde gris
            if newGameState[x, y] == 0:
                pygame.draw.polygon(screen, (40, 40, 40), poly, 1)
           # Si la celda está "viva" pintamos un recuadro relleno de color
            else:
                pygame.draw.polygon(screen, (200, 100, 100), poly, 0)

    # Actualizamos el estado del juego.
    gameState = np.copy(newGameState)

    # Mostramos el resultado
    pygame.display.flip()

