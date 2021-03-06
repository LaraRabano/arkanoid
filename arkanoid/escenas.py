"""Esto me permite que la ruta de llamada de los archivos coloque las barras automáticamente en función del sistema 
operativo en el que esté. Así mi juego funciona en cualquier sistema operativo"""

from curses.ascii import alt
import os 

import pygame as pg

from . import ANCHO, ALTO #He puesto el punto porque Escenas está en arkanoid. Esto es una "importación relativa"

class Escena:
   
    def __init__(self,pantalla):
        self.pantalla = pantalla
    
    def bucle_principal(sefl):
      """
      Este método debe ser implementado por cada una de las escenas,
      en función de lo que estén esperando hasta la condición de salida
      """

class Portada(Escena):

    def __init__(self, pantalla: pg.Surface): #Le digo que pantalla es de tipo surface
        super().__init__(pantalla)
        self.logo = pg.image.load(os.path.join("Resources", "Images", "arkanoid_name.png"))
     
    def bucle_principal(self):
        salir = False
        while not salir:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    salir = True

            self.pantalla.fill((0,99,0))
            self.pintar_logo()
            pg.display.flip()

    def pintar_logo(self):
        ancho_logo = self.logo.get_width()
        pos_x = (ANCHO - ancho_logo)/2
        pos_y = ALTO/3
        self.pantalla.blit(self.logo,(pos_x, pos_y))

class Partida(Escena):
    
     def bucle_principal(self):
        salir = False
        while not salir:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    salir = True
            self.pantalla.fill((0,0,99))
            pg.display.flip()

            

class HallofFame(Escena):
    
     def bucle_principal(self):
        salir = False
        while not salir:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    salir = True
            self.pantalla.fill((99,0,0))
            pg.display.flip()
