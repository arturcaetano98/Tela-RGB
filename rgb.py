import pygame
R = 255.0
G = 0.0
B = 0.0
etapa = 0;
while(1):
    if(etapa == 0):
        G = G + 0.5
        if(R == 255.0 and G == 255.0 and B == 0.0):
            etapa = 1
    if(etapa == 1):
        R = R - 0.5
        if(R == 0.0 and G == 255.0 and B == 0.0):
            etapa = 2
    if(etapa == 2):
        B = B + 0.5
        if(R == 0.0 and G == 255.0 and B == 255.0):
            etapa = 3
    if(etapa == 3):
        G = G - 0.5
        if(R == 0.0 and G == 0.0 and B == 255.0):
            etapa = 4
    if(etapa == 4):
        R = R + 0.5
        if(R == 255.0 and G == 0.0 and B == 255.0):
            etapa = 5
    if(etapa == 5):
        B = B - 0.5
        if(R == 255.0 and G == 0.0 and B == 0.0):
            etapa = 0
    pygame.init()
    surface = pygame.display.set_mode((1366, 768))
    color = (R, G, B)
    surface.fill(color)  
    pygame.display.flip()
