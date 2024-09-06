import pygame
import pygame.display
pygame.init()
    #ancho,alto
size=(500,800)

#aqui para ir creando la vista de la ventana
screen=pygame.display.set_mode(size)

#los juegos se mantienen vivos en constante por los whiles(bucles infinitos)
while True:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            SystemExit(exit())