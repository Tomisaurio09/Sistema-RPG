"""
1. Sistema de Batalla RPG
Descripción: Diseña un simulador de batalla entre personajes de un juego RPG.

Requisitos:

Crea una clase Personaje con atributos básicos como:
nombre
vida
ataque
defensa
Añade métodos como atacar (reduce la vida del oponente según el ataque y defensa), defenderse, y mostrar_estado.
Crea subclases como Guerrero, Mago o Arquero, que tengan habilidades específicas:
El Mago puede lanzar hechizos que ignoran defensa.
El Guerrero tiene más vida base.
El Arquero puede realizar ataques críticos al azar.
Diseña un bucle para simular turnos de batalla entre dos personajes hasta que uno gane.
Extras para mayor dificultad:

Añade una clase Inventario para que los personajes puedan usar pociones o armas durante la batalla.
Crea un sistema de niveles y experiencia que mejore los atributos de los personajes tras cada batalla.

"""

class Personaje:
    def __init__(self,nombre,vida,ataque,defensa):
        self.nombre = nombre
        self.vida = vida
        self.ataque = ataque
        self.defensa = defensa

    def atacar(self):
        pass

    def defenderse(self):
        pass

    def mostrar_estado(self):
        pass

class Mago(Personaje):
    pass

class Guerrero(Personaje):
    pass

class Arquero(Personaje):
    pass

