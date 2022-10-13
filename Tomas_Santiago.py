# -*- coding: utf-8 -*-
import pygame
import numpy as np #alias de numpy
import time

pygame.init() 

width, height = 400, 400

bg = 25, 25, 25

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
#
 #Serpent 1
#gameState[30,20] = 1
#gameState[31,20] = 1
#gameState[32,20] = 1
#gameState[32,19] = 1
#gameState[33,19] = 1
#ameState[34,19] = 1
#
#mensaje






#A
# gameState[20,20] = 1
# gameState[19,21] = 1
# gameState[18,22] = 1
# gameState[17,23] = 1
# gameState[16,24] = 1
# gameState[15,25] = 1
# gameState[15,26] = 1
# gameState[14,30] = 1
#

pos=[0,0]
pos2=[0,0]

pauseExect = True
stay = True

# Bucle de ejecución
while stay:
    
    # gameState[pos[0]+0,pos[1]+0]=1
    # gameState[pos[0]+1,pos[1]+1]=1
    # gameState[pos[0]+2,pos[1]-2]=1
    # gameState[pos[0]+3,pos[1]-3]=1
    # gameState[pos[0]+4,pos[1]-4]=1
    # gameState[pos[0]+2,pos[1]-2]=1
    # gameState[pos[0]+3,pos[1]-3]=1
    # gameState[pos[0]+5,pos[1]-4]=1
    # gameState[pos[0]+6,pos[1]-2]=1
    # gameState[pos[0]+7,pos[1]-3]=1
    # gameState[pos[0]+8,pos[1]-4]=1


    #AVION 2


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
                pos[0]=pos[0]-1
            elif event.key == pygame.K_RIGHT:
                pos[0]=pos[0]+1
                
            elif event.key == pygame.K_UP:
                pos[1]=pos[1]-1
            elif event.key == pygame.K_DOWN:
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
            
            newGameState[pos2[0]+50,pos2[1]+50] = 0
            newGameState[pos2[0]+50,pos2[1]+51] = 0
            newGameState[pos2[0]+50,pos2[1]+52] = 0
            newGameState[pos2[0]+50,pos2[1]+53] = 0
            newGameState[pos2[0]+50,pos2[1]+54] = 0
            newGameState[pos2[0]+50,pos2[1]+55] = 0
            newGameState[pos2[0]+50,pos2[1]+56] = 0
            newGameState[pos2[0]+50,pos2[1]+57] = 0
            newGameState[pos2[0]+50,pos2[1]+58] = 0
            newGameState[pos2[0]+50,pos2[1]+59] = 0
            newGameState[pos2[0]+60,pos2[1]+60] = 0
            
            #alas
            newGameState[pos2[0]+51,pos2[1]+56] = 0
            newGameState[pos2[0]+49,pos2[1]+56] = 0
            newGameState[pos2[0]+52,pos2[1]+55] = 0
            newGameState[pos2[0]+48,pos2[1]+55] = 0
            newGameState[pos2[0]+53,pos2[1]+54] = 0
            newGameState[pos2[0]+47,pos2[1]+54] = 0
            newGameState[pos2[0]+51,pos2[1]+50] = 0
            newGameState[pos2[0]+49,pos2[1]+50] = 0


            newGameState[pos[0]+50,pos[1]+50] = 1
            newGameState[pos[0]+50,pos[1]+51] = 1
            newGameState[pos[0]+50,pos[1]+52] = 1
            newGameState[pos[0]+50,pos[1]+53] = 1
            newGameState[pos[0]+50,pos[1]+54] = 1
            newGameState[pos[0]+50,pos[1]+55] = 1
            newGameState[pos[0]+50,pos[1]+56] = 1
            newGameState[pos[0]+50,pos[1]+57] = 1
            newGameState[pos[0]+50,pos[1]+58] = 1
            newGameState[pos[0]+50,pos[1]+59] = 1
            newGameState[pos[0]+60,pos[1]+60] = 1

        #alas
            newGameState[pos[0]+51,pos[1]+56] = 1
            newGameState[pos[0]+49,pos[1]+56] = 1
            newGameState[pos[0]+52,pos[1]+55] = 1
            newGameState[pos[0]+48,pos[1]+55] = 1
            newGameState[pos[0]+53,pos[1]+54] = 1
            newGameState[pos[0]+47,pos[1]+54] = 1
            newGameState[pos[0]+51,pos[1]+50] = 1
            newGameState[pos[0]+49,pos[1]+50] = 1
            
            # Si la celda está "muerta" pintamos un recuadro con borde gris
            #cuerpo
            
            pos2=pos;
            
            
                
            if newGameState[x, y] == 0:
                pygame.draw.polygon(screen, (40, 40, 40), poly, 1)
           # Si la celda está "viva" pintamos un recuadro relleno de color
            else:
                pygame.draw.polygon(screen, (200, 200, 100), poly, 0)

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