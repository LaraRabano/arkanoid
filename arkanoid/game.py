import pygame as pg

from arkanoid import ALTO, ANCHO
from arkanoid.escenas import HallofFame, Partida, Portada



class Arkanoid:
    def __init__(self) -> None:
        print("Arranca el juego!!")
        pg.init()
        self.display = pg.display.set_mode((ANCHO, ALTO)) 
        pg.display.set_caption("Larkanoid") 

        Icon = pg.image.load('/Users/lara/Documents/BOOTCAMP/Probando-uno/arkanoid/arkanoid/Resources/Images/arkanoid_name.png')
        pg.display.set_icon(Icon)

        Fondo = pg.image.load('/Users/lara/Documents/BOOTCAMP/Probando-uno/arkanoid/arkanoid/Resources/Images/background.jpg')
        self.display.blit(Fondo,(0,0))

        #pygame.display.set_icon(Icon_name)
        #Icon = pygame.image.load('gfglogo.png')
        #pygame.display.set_icon(Icon)  
        
        self.escenas = [ 
            Portada(self.display),
            Partida(self.display),
            HallofFame(self.display),
        ]




    def jugar(self):
        """""Este es el bucle principal"""
        for escena in self.escenas:
            escena.bucle_principal()

if __name__ == "__main__":
    juego = Arkanoid()
    juego.jugar()

