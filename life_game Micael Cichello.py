# -*- coding: utf-8 -*-
import pygame
import numpy as np #alias de numpy
import time

pygame.init() 

width, height = 800, 800

bg = 25, 25, 30

screen  = pygame.display.set_mode((height, width))
screen.fill(bg)

# Tamaño de nuestra matriz
nxC, nyC = 150, 150

# Estado de las celdas. Viva = 1 / Muerta = 0
gameState = np.zeros((nxC,  nyC))

#dimensiones de cada celda individual
dimCW = width / nxC
dimCH = height / nyC

# # Oscilador.
# gameState[38, 20] = 1
# gameState[39, 20] = 1
# gameState[40, 20] = 1

# # Runner 1
# gameState[10,5] = 1
# gameState[12,5] = 1
# gameState[11,6] = 1
# gameState[12,6] = 1
# gameState[11,7] = 1

# #Runner 2
# gameState[5,10] = 1
# gameState[5,12] = 1
# gameState[6,11] = 1
# gameState[6,12] = 1
# gameState[7,11] = 1

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

#mensaje
#H
gameState[5,59] = 1
gameState[5,58] = 1
gameState[5,57] = 1
gameState[5,56] = 1
gameState[5,55] = 1
gameState[6,57] = 1
gameState[7,59] = 1
gameState[7,58] = 1
gameState[7,57] = 1
gameState[7,56] = 1
gameState[7,55] = 1
#
#O
gameState[9,59] = 1
gameState[9,58] = 1
gameState[9,57] = 1
gameState[9,56] = 1
gameState[9,55] = 1
gameState[10,59] = 1
gameState[10,55] = 1
gameState[11,59] = 1
gameState[11,58] = 1
gameState[11,57] = 1
gameState[11,56] = 1
gameState[11,55] = 1
#
#L
gameState[13,59] = 1
gameState[13,58] = 1
gameState[13,57] = 1
gameState[13,56] = 1
gameState[13,55] = 1
gameState[14,59] = 1
gameState[15,59] = 1
#
#A
gameState[17,59] = 1
gameState[17,58] = 1
gameState[17,57] = 1
gameState[17,56] = 1
gameState[17,55] = 1
gameState[18,55] = 1
gameState[18,57] = 1
gameState[19,59] = 1
gameState[19,58] = 1
gameState[19,57] = 1
gameState[19,56] = 1
gameState[19,55] = 1
#
#P
gameState[22,59] = 1
gameState[22,58] = 1
gameState[22,57] = 1
gameState[22,56] = 1
gameState[22,55] = 1
gameState[23,55] = 1
gameState[24,55] = 1
gameState[24,56] = 1
gameState[24,57] = 1
gameState[23,57] = 1
#
#R
gameState[26,59] = 1
gameState[26,58] = 1
gameState[26,57] = 1
gameState[26,56] = 1
gameState[26,55] = 1
gameState[27,55] = 1
gameState[28,55] = 1
gameState[28,56] = 1
gameState[28,57] = 1
gameState[27,57] = 1
gameState[27,58] = 1
gameState[28,59] = 1
#
#R
gameState[30,59] = 1
gameState[30,58] = 1
gameState[30,57] = 1
gameState[30,56] = 1
gameState[30,55] = 1
gameState[31,55] = 1
gameState[32,55] = 1
gameState[32,56] = 1
gameState[32,57] = 1
gameState[31,57] = 1
gameState[31,58] = 1
gameState[32,59] = 1
#
#O
gameState[34,59] = 1
gameState[34,58] = 1
gameState[34,57] = 1
gameState[34,56] = 1
gameState[34,55] = 1
gameState[35,59] = 1
gameState[35,55] = 1
gameState[36,59] = 1
gameState[36,58] = 1
gameState[36,57] = 1
gameState[36,56] = 1
gameState[36,55] = 1
#
#S
gameState[38,59] = 1
gameState[38,58] = 0
gameState[38,57] = 1
gameState[38,56] = 1
gameState[38,55] = 1
gameState[39,59] = 1
gameState[39,57] = 1
gameState[39,55] = 1
gameState[40,59] = 1
gameState[40,58] = 1
gameState[40,57] = 1
gameState[40,56] = 0
gameState[40,55] = 1













pauseExect = True
stay = True

pos=[20,20]


# Bucle de ejecución
while stay:
    
    # gameState[pos[0]-4,pos[1]] = 1
    # gameState[pos[0]-5,pos[1]] = 1
    # gameState[pos[0]-6,pos[1]] = 1
    # gameState[pos[0]-7,pos[1]] = 1
    # gameState[pos[0],pos[1]] = 1
    # gameState[pos[0]-1,pos[1]-1] = 1
    # gameState[pos[0]-2,pos[1]-1] = 1
    # gameState[pos[0]-3,pos[1]-1] = 1
    # gameState[pos[0]-3,pos[1]-1] = 1
    # gameState[pos[0]-3,pos[1]] = 1
    # gameState[pos[0]-3,pos[1]+1] = 1
    # gameState[pos[0]-3,pos[1]+2] = 1
    # gameState[pos[0]-3,pos[1]+3] = 1
    # gameState[pos[0],pos[1]+1] = 1
    # gameState[pos[0]-1,pos[1]+2] = 1
    # gameState[pos[0]-2,pos[1]+3] = 1
    # gameState[pos[0]-3,pos[1]+3] = 1
    
    # Copiamosla matriz del estado anterior
    # #para representar la matriz en el nuevo estado
    newGameState = np.copy(gameState)

    # Ralentizamos la ejecución a 0.1 segundos
    time.sleep(0.01)

    # Limpiamos la pantalla
    screen.fill(bg)

    # Registramos eventos de teclado y ratón.
    ev = pygame.event.get()

    # Cada vez que identificamos un evento lo procesamos
    for event in ev:
        # Detectamos si se presiona una tecla.
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                pos[0]=pos[0]-1
                
            elif event.key == pygame.K_RIGHT:
                pos[0]=pos[0]+1
            elif event.key == pygame.K_DOWN:
                pos[1]=pos[1]+1
            elif event.key == pygame.K_UP:
                pos[1]=pos[1]+1
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
            
            newGameState[pos[0]+30,pos[1]+30] = 1
            newGameState[pos[0]+31,pos[1]+31] = 1
            newGameState[pos[0]+32,pos[1]+32] = 1
            newGameState[pos[0]+33,pos[1]+33] = 1
            newGameState[pos[0]+34,pos[1]+34] = 1
            newGameState[pos[0]+35,pos[1]+35] = 1
            newGameState[pos[0]+36,pos[1]+36] = 1
            newGameState[pos[0]+36,pos[1]+37] = 1
            newGameState[pos[0]+37,pos[1]+37] = 1
            newGameState[pos[0]+37,pos[1]+36] = 1
            newGameState[pos[0]+30,pos[1]+28] = 1
            newGameState[pos[0]+30,pos[1]+27] = 1
            newGameState[pos[0]+29,pos[1]+30] = 1
            newGameState[pos[0]+28,pos[1]+30] = 1
            newGameState[pos[0]+30,pos[1]+29] = 1
            newGameState[pos[0]+26,pos[1]+29] = 1
            newGameState[pos[0]+27,pos[1]+30] = 1
            newGameState[pos[0]+25,pos[1]+28] = 1
            newGameState[pos[0]+24,pos[1]+27] = 1
            newGameState[pos[0]+23,pos[1]+26] = 1
            newGameState[pos[0]+22,pos[1]+25] = 1
            newGameState[pos[0]+21,pos[1]+24] = 1
            newGameState[pos[0]+20,pos[1]+23] = 1
            newGameState[pos[0]+19,pos[1]+22] = 1
            newGameState[pos[0]+18,pos[1]+21] = 1
            newGameState[pos[0]+18,pos[1]+20] = 1
            newGameState[pos[0]+18,pos[1]+19] = 1
            newGameState[pos[0]+18,pos[1]+18] = 1
            newGameState[pos[0]+19,pos[1]+18] = 1
            newGameState[pos[0]+20,pos[1]+18] = 1
            newGameState[pos[0]+21,pos[1]+18] = 1
            newGameState[pos[0]+22,pos[1]+19] = 1
            newGameState[pos[0]+23,pos[1]+20] = 1
            newGameState[pos[0]+24,pos[1]+21] = 1
            newGameState[pos[0]+25,pos[1]+22] = 1
            newGameState[pos[0]+26,pos[1]+23] = 1
            newGameState[pos[0]+27,pos[1]+24] = 1
            newGameState[pos[0]+28,pos[1]+25] = 1
            newGameState[pos[0]+29,pos[1]+26] = 1
            # Si la celda está "muerta" pintamos un recuadro con borde gris
            if newGameState[x, y] == 0:
                pygame.draw.polygon(screen, (40, 40, 40), poly, 1)
           # Si la celda está "viva" pintamos un recuadro relleno de color
            else:
                pygame.draw.polygon(screen, (100, 100, 200), poly, 0)

    # Actualizamos el estado del juego.
    gameState = np.copy(newGameState)

    # Mostramos el resultado
    pygame.display.flip()

#Lista de teclas y como llamarlas
# pygame
# Constant      ASCII   Description
# ---------------------------------
# K_BACKSPACE   \b      backspace
# K_TAB         \t      tab
# K_CLEAR               clear
# K_RETURN      \r      return
# K_PAUSE               pause
# K_ESCAPE      ^[      escape
# K_SPACE               space
# K_EXCLAIM     !       exclaim
# K_QUOTEDBL    "       quotedbl
# K_HASH        #       hash
# K_DOLLAR      $       dollar
# K_AMPERSAND   &       ampersand
# K_QUOTE               quote
# K_LEFTPAREN   (       left parenthesis
# K_RIGHTPAREN  )       right parenthesis
# K_ASTERISK    *       asterisk
# K_PLUS        +       plus sign
# K_COMMA       ,       comma
# K_MINUS       -       minus sign
# K_PERIOD      .       period
# K_SLASH       /       forward slash
# K_0           0       0
# K_1           1       1
# K_2           2       2
# K_3           3       3
# K_4           4       4
# K_5           5       5
# K_6           6       6
# K_7           7       7
# K_8           8       8
# K_9           9       9
# K_COLON       :       colon
# K_SEMICOLON   ;       semicolon
# K_LESS        <       less-than sign
# K_EQUALS      =       equals sign
# K_GREATER     >       greater-than sign
# K_QUESTION    ?       question mark
# K_AT          @       at
# K_LEFTBRACKET [       left bracket
# K_BACKSLASH   \       backslash
# K_RIGHTBRACKET ]      right bracket
# K_CARET       ^       caret
# K_UNDERSCORE  _       underscore
# K_BACKQUOTE   `       grave
# K_a           a       a
# K_b           b       b
# K_c           c       c
# K_d           d       d
# K_e           e       e
# K_f           f       f
# K_g           g       g
# K_h           h       h
# K_i           i       i
# K_j           j       j
# K_k           k       k
# K_l           l       l
# K_m           m       m
# K_n           n       n
# K_o           o       o
# K_p           p       p
# K_q           q       q
# K_r           r       r
# K_s           s       s
# K_t           t       t
# K_u           u       u
# K_v           v       v
# K_w           w       w
# K_x           x       x
# K_y           y       y
# K_z           z       z
# K_DELETE              delete
# K_KP0                 keypad 0
# K_KP1                 keypad 1
# K_KP2                 keypad 2
# K_KP3                 keypad 3
# K_KP4                 keypad 4
# K_KP5                 keypad 5
# K_KP6                 keypad 6
# K_KP7                 keypad 7
# K_KP8                 keypad 8
# K_KP9                 keypad 9
# K_KP_PERIOD   .       keypad period
# K_KP_DIVIDE   /       keypad divide
# K_KP_MULTIPLY *       keypad multiply
# K_KP_MINUS    -       keypad minus
# K_KP_PLUS     +       keypad plus
# K_KP_ENTER    \r      keypad enter
# K_KP_EQUALS   =       keypad equals
# K_UP                  up arrow
# K_DOWN                down arrow
# K_RIGHT               right arrow
# K_LEFT                left arrow
# K_INSERT              insert
# K_HOME                home
# K_END                 end
# K_PAGEUP              page up
# K_PAGEDOWN            page down
# K_F1                  F1
# K_F2                  F2
# K_F3                  F3
# K_F4                  F4
# K_F5                  F5
# K_F6                  F6
# K_F7                  F7
# K_F8                  F8
# K_F9                  F9
# K_F10                 F10
# K_F11                 F11
# K_F12                 F12
# K_F13                 F13
# K_F14                 F14
# K_F15                 F15
# K_NUMLOCK             numlock
# K_CAPSLOCK            capslock
# K_SCROLLOCK           scrollock
# K_RSHIFT              right shift
# K_LSHIFT              left shift
# K_RCTRL               right control
# K_LCTRL               left control
# K_RALT                right alt
# K_LALT                left alt
# K_RMETA               right meta
# K_LMETA               left meta
# K_LSUPER              left Windows key
# K_RSUPER              right Windows key
# K_MODE                mode shift
# K_HELP                help
# K_PRINT               print screen
# K_SYSREQ              sysrq
# K_BREAK               break
# K_MENU                menu
# K_POWER               power
# K_EURO                Euro
# K_AC_BACK             Android back button 