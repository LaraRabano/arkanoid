import pygame as pg

class Escena:
   
    def __init__(self,pantalla):
        self.pantalla = pantalla
    
    def bucle_principal(sefl):
      """
      Este método debe ser implementado por cada una de las escenas,
      en función de lo que estén esperando hasta la condición de salida
      """

class Portada(Escena):
     
     def bucle_principal(self):
        salir = False
        while not salir:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    salir = True
            self.pantalla.fill((0,99,0))
            pg.display.flip()


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
