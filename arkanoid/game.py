import pygame as pg

from arkanoid import ALTO, ANCHO

Icon = pg.image.load('/Users/lara/Documents/BOOTCAMP/Probando-uno/arkanoid/arkanoid/Resources/Images/arkanoid_name.png')
Fondo = pg.image.load('/Users/lara/Documents/BOOTCAMP/Probando-uno/arkanoid/arkanoid/Resources/Images/background.jpg')

class Arkanoid:
    def __init__(self) -> None:
        print("Arranca el juego!!")
        pg.init()
        self.display = pg.display.set_mode((ANCHO, ALTO)) 
        pg.display.set_caption("Larkanoid") 
        pg.display.set_icon(Icon)
        self.display.blit(Fondo,(0,0))

        #pygame.display.set_icon(Icon_name)
        #Icon = pygame.image.load('gfglogo.png')
        #pygame.display.set_icon(Icon)  
    
    def jugar(self):
        """""Este es el bucle principal"""
        salir = False
        while not salir:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    salir = True
            self.display.fill((99,99,99))
            pg.display.flip()

if __name__ == "__main__":
    juego = Arkanoid()
    juego.jugar()

