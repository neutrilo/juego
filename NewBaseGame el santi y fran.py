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

xvel = 0
yvel = 0
xtiempo = 0
ytiempo = 0


pauseExect = True
stay = True

# Bucle de ejecución
while stay:

    xtiempo = xtiempo+1
    ytiempo = ytiempo+1
    
    periodox=6-abs(xvel)
    if (periodox == 6):
        periodox = 999999999999999999999999999999999999999999999
        
    periodoy=6-abs(yvel)
    if (periodoy == 6):
        periodoy = 999999999999999999999999999999999999999999999
    
    if (xtiempo >= periodox):
        xtiempo = 0
        xpos = xpos+int(xvel/abs(xvel))
                
    if (ytiempo >= periodoy):
        ytiempo = 0
        ypos = ypos+int(yvel/abs(yvel)) 

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
                yvel = yvel + 1                
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
        
        #H
        
        #Alas
        gameState[bxpos+20,20+bypos] = 0
        gameState[bxpos+19,20+bypos] = 0
        gameState[bxpos+18,20+bypos] = 0
        gameState[bxpos+17,20+bypos] = 0
        gameState[bxpos+16,20+bypos] = 0
        gameState[bxpos+15,20+bypos] = 0
        gameState[bxpos+14,20+bypos] = 0
        gameState[bxpos+13,20+bypos] = 0
        gameState[bxpos+12,20+bypos] = 0
        gameState[bxpos+11,20+bypos] = 0
        gameState[bxpos+10,20+bypos] = 0
        gameState[bxpos+20,30+bypos] = 0
        gameState[bxpos+19,30+bypos] = 0
        gameState[bxpos+18,30+bypos] = 0
        gameState[bxpos+17,30+bypos] = 0
        gameState[bxpos+16,30+bypos] = 0
        gameState[bxpos+15,30+bypos] = 0
        gameState[bxpos+14,30+bypos] = 0
        gameState[bxpos+13,30+bypos] = 0
        gameState[bxpos+12,30+bypos] = 0
        gameState[bxpos+11,30+bypos] = 0
        gameState[bxpos+10,30+bypos] = 0
        
        gameState[bxpos+10,20+bypos] = 0
        gameState[bxpos+10,21+bypos] = 0
        gameState[bxpos+10,22+bypos] = 0
        gameState[bxpos+10,23+bypos] = 0
        gameState[bxpos+10,24+bypos] = 0
        gameState[bxpos+10,25+bypos] = 0
        gameState[bxpos+10,26+bypos] = 0
        gameState[bxpos+10,27+bypos] = 0
        gameState[bxpos+10,28+bypos] = 0
        gameState[bxpos+10,29+bypos] = 0
        gameState[bxpos+10,30+bypos] = 0
        gameState[bxpos+10,20+bypos] = 0
        gameState[bxpos+20,20+bypos] = 0
        gameState[bxpos+20,21+bypos] = 0
        gameState[bxpos+20,22+bypos] = 0
        gameState[bxpos+20,23+bypos] = 0
        gameState[bxpos+20,24+bypos] = 0
        gameState[bxpos+20,25+bypos] = 0
        gameState[bxpos+20,26+bypos] = 0
        gameState[bxpos+20,27+bypos] = 0
        gameState[bxpos+20,28+bypos] = 0
        gameState[bxpos+20,29+bypos] = 0
        gameState[bxpos+20,30+bypos] = 0
        gameState[bxpos+20,20+bypos] = 0
#-----------------------------------------------------------------------------
        
        #H
        gameState[xpos+20,20+ypos] = 1
        gameState[xpos+19,20+ypos] = 1
        gameState[xpos+18,20+ypos] = 1
        gameState[xpos+17,20+ypos] = 1
        gameState[xpos+16,20+ypos] = 1
        gameState[xpos+15,20+ypos] = 1
        gameState[xpos+14,20+ypos] = 1
        gameState[xpos+13,20+ypos] = 1
        gameState[xpos+12,20+ypos] = 1
        gameState[xpos+11,20+ypos] = 1
        gameState[xpos+10,20+ypos] = 1
        gameState[xpos+20,30+ypos] = 1
        gameState[xpos+19,30+ypos] = 1
        gameState[xpos+18,30+ypos] = 1
        gameState[xpos+17,30+ypos] = 1
        gameState[xpos+16,30+ypos] = 1
        gameState[xpos+15,30+ypos] = 1
        gameState[xpos+14,30+ypos] = 1
        gameState[xpos+13,30+ypos] = 1
        gameState[xpos+12,30+ypos] = 1
        gameState[xpos+11,30+ypos] = 1
        gameState[xpos+10,30+ypos] = 1
        
        gameState[xpos+10,20+ypos] = 1
        gameState[xpos+10,21+ypos] = 1
        gameState[xpos+10,22+ypos] = 1
        gameState[xpos+10,23+ypos] = 1
        gameState[xpos+10,24+ypos] = 1
        gameState[xpos+10,25+ypos] = 1
        gameState[xpos+10,26+ypos] = 1
        gameState[xpos+10,27+ypos] = 1
        gameState[xpos+10,28+ypos] = 1
        gameState[xpos+10,29+ypos] = 1
        gameState[xpos+10,30+ypos] = 1
        gameState[xpos+10,20+ypos] = 1
        gameState[xpos+20,20+ypos] = 1
        gameState[xpos+20,21+ypos] = 1
        gameState[xpos+20,22+ypos] = 1
        gameState[xpos+20,23+ypos] = 1
        gameState[xpos+20,24+ypos] = 1
        gameState[xpos+20,25+ypos] = 1
        gameState[xpos+20,26+ypos] = 1
        gameState[xpos+20,27+ypos] = 1
        gameState[xpos+20,28+ypos] = 1
        gameState[xpos+20,29+ypos] = 1
        gameState[xpos+20,30+ypos] = 1
        gameState[xpos+20,20+ypos] = 1
    
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