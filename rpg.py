
#1. Sistema de Batalla RPG

class Personaje:
    def __init__(self,nombre,vida,ataque,defensa, velocidad):
        #stats del personaje
        self.nombre = nombre 
        self.vida = vida
        self.ataque = ataque
        self.defensa = defensa
        self.velocidad = velocidad

    def atacar(self): #el oponente es una instancia?
        pass

    def defenderse(self):
        pass

    def mostrar_estado(self):
        pass

class Mago(Personaje):
    def __init__(self, nombre, vida, ataque, defensa,velocidad):
        super().__init__(nombre, vida, ataque, defensa,velocidad)
        #El mago tiene mucho ataque magico y velocidad, pero poca defensa y vida
        ataque_reducido = (ataque * 10) / 100
        defensa_reducida = (defensa * 5) / 100
        vida_reducida = (vida * 10) / 100

        self.velocidad = velocidad * 1.5
        self.ataque_magico = ataque * 2
        self.ataque = ataque - ataque_reducido
        self.vida = vida - vida_reducida
        self.defensa = defensa - defensa_reducida

    def atacar(self,oponente):
        print(f"El mago {self.nombre} le lanzó un hechizo a {oponente.nombre}")
        oponente.vida -= self.ataque_magico
        print(f"El ataque infligió {self.ataque_magico} de daño al oponente, la vida del oponente {oponente.nombre} es de {oponente.vida}")

class Guerrero(Personaje):
    def __init__(self, nombre, vida, ataque, defensa,velocidad):
        super().__init__(nombre, vida, ataque, defensa,velocidad)
        #El guerrero es un personaje equilibrado que tiene un boost en ataque fisico
        self.berserker = ataque * 2

    def atacar(self,oponente):
        print(f"El guerrero {self.nombre} atacó con su espada a {oponente.nombre}")
        oponente.vida -= self.berserker
        print(f"El ataque infligió {self.berserker} de daño al oponente, la vida del oponente {oponente.nombre} es de {oponente.vida}")

class Arquero(Personaje):
    def __init__(self, nombre, vida, ataque, defensa,velocidad):
        super().__init__(nombre, vida, ataque, defensa,velocidad)
        #El arquero es muy rápido y sus ataques son muy fuertes. Pero es débil en cuanto defensa y vida
        defensa_reducida = (defensa * 15) / 100
        vida_reducida = (vida * 15) / 100

        self.velocidad = velocidad * 2
        self.ataque = ataque * 3
        self.vida = vida - vida_reducida
        self.defensa = defensa - defensa_reducida
    
    def atacar(self,oponente):
        print(f"El arquero {self.nombre} le disparó una flecha a {oponente.nombre}")
        oponente.vida -= self.ataque
        print(f"El ataque infligió {self.ataque} de daño al oponente, la vida del oponente {oponente.nombre} es de {oponente.vida}")


mago = Mago("Gandalf",100,20,30,50)
guerrero = Guerrero("Aragorn",100,20,30,50)
arquero = Arquero("Legolas",100,20,30,100)

guerrero.atacar(mago)