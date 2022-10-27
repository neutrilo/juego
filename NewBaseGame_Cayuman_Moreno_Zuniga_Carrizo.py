# -*- coding: utf-8 -*-
import pygame
import numpy as np #alias de numpy
import time

pygame.init() 

width, height = 400, 400

bg = 25, 75, 100

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

# Bucle de ejecución
while stay:

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
                xpos = xpos - 1
            elif event.key == pygame.K_RIGHT:
                xpos = xpos + 1
            elif event.key == pygame.K_UP:
                if ypos > -nyC+15:
                    ypos = ypos - 1
            elif event.key == pygame.K_DOWN:
                ypos =  ypos + 1                
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
    
    
    #Borrado y escritura
    if (xpos != bxpos) or (ypos != bypos):
        
        # #H
        # gameState[bxpos+5,59+bypos] = 0
        # gameState[bxpos+5,58+bypos] = 0
        # gameState[bxpos+5,57+bypos] = 0
        # gameState[bxpos+5,56+bypos] = 0
        # gameState[bxpos+5,55+bypos] = 0
        # gameState[bxpos+6,57+bypos] = 0
        # gameState[bxpos+7,59+bypos] = 0
        # gameState[bxpos+7,58+bypos] = 0
        # gameState[bxpos+7,57+bypos] = 0
        # gameState[bxpos+7,56+bypos] = 0
        # gameState[bxpos+7,55+bypos] = 0
        # #Alas
        # gameState[bxpos+4,57+bypos] = 0
        # gameState[bxpos+8,57+bypos] = 0
        # gameState[bxpos+4,58+bypos] = 0
        # gameState[bxpos+8,58+bypos] = 0
        # gameState[bxpos+3,58+bypos] = 0
        # gameState[bxpos+9,58+bypos] = 0
        # gameState[bxpos+3,59+bypos] = 0
        # gameState[bxpos+9,59+bypos] = 0

        
        # #H
        # gameState[xpos+5,59+ypos] = 1
        # gameState[xpos+5,58+ypos] = 1
        # gameState[xpos+5,57+ypos] = 1
        # gameState[xpos+5,56+ypos] = 1
        # gameState[xpos+5,55+ypos] = 1
        # gameState[xpos+6,57+ypos] = 1
        # gameState[xpos+7,59+ypos] = 1
        # gameState[xpos+7,58+ypos] = 1
        # gameState[xpos+7,57+ypos] = 1
        # gameState[xpos+7,56+ypos] = 1
        # gameState[xpos+7,55+ypos] = 1
        # #Alas
        # gameState[xpos+4,57+ypos] = 1
        # gameState[xpos+8,57+ypos] = 1
        # gameState[xpos+4,58+ypos] = 1
        # gameState[xpos+8,58+ypos] = 1
        # gameState[xpos+3,58+ypos] = 1
        # gameState[xpos+9,58+ypos] = 1
        # gameState[xpos+3,59+ypos] = 1
        # gameState[xpos+9,59+ypos] = 1
    
            #amongus
            gameState[bxpos+0,bypos-3]=0
            gameState[bxpos+0,bypos-4]=0
            gameState[bxpos+0,bypos-5]=0
            gameState[bxpos+0,bypos-6]=0
            gameState[bxpos+0,bypos-7]=0
            gameState[bxpos+0,bypos-8]=0
            gameState[bxpos+0,bypos-9]=0
            gameState[bxpos+0,bypos-10]=0
            gameState[bxpos+0,bypos-11]=0
            gameState[bxpos+0,bypos-12]=0
            gameState[bxpos+0,bypos-13]=0
            gameState[bxpos+0,bypos-14]=0
            #
            gameState[bxpos+1,bypos-15]=0
            gameState[bxpos+2,bypos-15]=0
            gameState[bxpos+3,bypos-15]=0
            gameState[bxpos+4,bypos-15]=0
            gameState[bxpos+5,bypos-15]=0
            gameState[bxpos+6,bypos-15]=0
            gameState[bxpos+7,bypos-15]=0
            #
            gameState[bxpos+8,bypos-14]=0
            gameState[bxpos+8,bypos-13]=0
            gameState[bxpos+9,bypos-12]=0
            gameState[bxpos+9,bypos-11]=0
            gameState[bxpos+8,bypos-10]=0
            gameState[bxpos+8,bypos-9]=0
            gameState[bxpos+8,bypos-8]=0
            gameState[bxpos+8,bypos-7]=0
            gameState[bxpos+8,bypos-6]=0
            gameState[bxpos+8,bypos-5]=0
            gameState[bxpos+8,bypos-4]=0
            gameState[bxpos+8,bypos-3]=0
            #
            gameState[bxpos+7,bypos-3]=0
            gameState[bxpos+6,bypos-3]=0
            gameState[bxpos+5,bypos-3]=0
            gameState[bxpos+5,bypos-4]=0
            gameState[bxpos+5,bypos-5]=0
            gameState[bxpos+5,bypos-6]=0
            gameState[bxpos+4,bypos-6]=0
            gameState[bxpos+3,bypos-6]=0
            gameState[bxpos+3,bypos-5]=0
            gameState[bxpos+3,bypos-4]=0
            gameState[bxpos+3,bypos-3]=0
            gameState[bxpos+2,bypos-3]=0
            gameState[bxpos+1,bypos-3]=0
            #
            gameState[bxpos-1,bypos-7]=0
            gameState[bxpos-2,bypos-7]=0
            gameState[bxpos-2,bypos-8]=0
            gameState[bxpos-2,bypos-9]=0
            gameState[bxpos-2,bypos-10]=0
            gameState[bxpos-2,bypos-11]=0
            gameState[bxpos-2,bypos-12]=0
            gameState[bxpos-1,bypos-12]=0
            #
            gameState[bxpos+7,bypos-13]=0
            gameState[bxpos+6,bypos-13]=0
            gameState[bxpos+5,bypos-13]=0
            gameState[bxpos+4,bypos-13]=0
            gameState[bxpos+3,bypos-12]=0
            gameState[bxpos+3,bypos-11]=0
            gameState[bxpos+7,bypos-10]=0
            gameState[bxpos+6,bypos-10]=0
            gameState[bxpos+5,bypos-10]=0
            gameState[bxpos+4,bypos-10]=0
    
    
    
    
            #amongus
            gameState[xpos+0,ypos-3]=1
            gameState[xpos+0,ypos-4]=1
            gameState[xpos+0,ypos-5]=1
            gameState[xpos+0,ypos-6]=1
            gameState[xpos+0,ypos-7]=1
            gameState[xpos+0,ypos-8]=1
            gameState[xpos+0,ypos-9]=1
            gameState[xpos+0,ypos-10]=1
            gameState[xpos+0,ypos-11]=1
            gameState[xpos+0,ypos-12]=1
            gameState[xpos+0,ypos-13]=1
            gameState[xpos+0,ypos-14]=1
            #
            gameState[xpos+1,ypos-15]=1
            gameState[xpos+2,ypos-15]=1
            gameState[xpos+3,ypos-15]=1
            gameState[xpos+4,ypos-15]=1
            gameState[xpos+5,ypos-15]=1
            gameState[xpos+6,ypos-15]=1
            gameState[xpos+7,ypos-15]=1
            #
            gameState[xpos+8,ypos-14]=1
            gameState[xpos+8,ypos-13]=1
            gameState[xpos+9,ypos-12]=1
            gameState[xpos+9,ypos-11]=1
            gameState[xpos+8,ypos-10]=1
            gameState[xpos+8,ypos-9]=1
            gameState[xpos+8,ypos-8]=1
            gameState[xpos+8,ypos-7]=1
            gameState[xpos+8,ypos-6]=1
            gameState[xpos+8,ypos-5]=1
            gameState[xpos+8,ypos-4]=1
            gameState[xpos+8,ypos-3]=1
            #
            gameState[xpos+7,ypos-3]=1
            gameState[xpos+6,ypos-3]=1
            gameState[xpos+5,ypos-3]=1
            gameState[xpos+5,ypos-4]=1
            gameState[xpos+5,ypos-5]=1
            gameState[xpos+5,ypos-6]=1
            gameState[xpos+4,ypos-6]=1
            gameState[xpos+3,ypos-6]=1
            gameState[xpos+3,ypos-5]=1
            gameState[xpos+3,ypos-4]=1
            gameState[xpos+3,ypos-3]=1
            gameState[xpos+2,ypos-3]=1
            gameState[xpos+1,ypos-3]=1
            #
            gameState[xpos-1,ypos-7]=1
            gameState[xpos-2,ypos-7]=1
            gameState[xpos-2,ypos-8]=1
            gameState[xpos-2,ypos-9]=1
            gameState[xpos-2,ypos-10]=1
            gameState[xpos-2,ypos-11]=1
            gameState[xpos-2,ypos-12]=1
            gameState[xpos-1,ypos-12]=1
            #
            gameState[xpos+7,ypos-13]=1
            gameState[xpos+6,ypos-13]=1
            gameState[xpos+5,ypos-13]=1
            gameState[xpos+4,ypos-13]=1
            gameState[xpos+3,ypos-12]=1
            gameState[xpos+3,ypos-11]=1
            gameState[xpos+7,ypos-10]=1
            gameState[xpos+6,ypos-10]=1
            gameState[xpos+5,ypos-10]=1
            gameState[xpos+4,ypos-10]=1
    
    
    
    
    
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