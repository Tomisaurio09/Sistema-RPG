import random

class Personaje:
    def __init__(self, nombre, vida, ataque, defensa):
        self.nombre = nombre 
        self.vida = vida
        self.ataque = ataque
        self.defensa = defensa

    def mostrar_detalles(self):
        print(f"""
            LOS STATS DEL PERSONAJE SON:
            Nombre: {self.nombre}
            Vida: {self.vida}
            Ataque: {self.ataque}
            Defensa: {self.defensa}
        """)

    def atacar(self, oponente):
        defensa_porcentaje = (oponente.defensa * 30) / 100
        ataque_recibido = self.ataque - defensa_porcentaje
        probabilidad_golpe = random.random()
        if probabilidad_golpe <= 0.8:
            print(f"El luchador {self.nombre} atacó a {oponente.nombre} y golpeó")
            oponente.vida -= ataque_recibido
            if oponente.vida <= 0:
                print(f"\nEl oponente {oponente.nombre} perdió, el ganador es {self.nombre}")
            else:
                print(f"\nEl ataque infligió {ataque_recibido:.2f} de daño al oponente, la vida del oponente {oponente.nombre} es de {oponente.vida:.2f}")
        else:
            print(f"El luchador {self.nombre} atacó a {oponente.nombre} y falló")
    
    

    def defender(self, oponente):
        defensa_porcentaje = (self.defensa * 30) / 100
        ataque_recibido = oponente.ataque - defensa_porcentaje
        defensa_despues_del_ataque = (self.defensa * 2) - ataque_recibido
        if defensa_despues_del_ataque < 0:
            self.vida += defensa_despues_del_ataque
            print(f"\nEl ataque pudo romper la defensa, la vida actual es de {self.vida:.2f}")
        else:
            print(f"\nLa defensa pudo resistir el ataque, la defensa actual es de {self.defensa:.2f}")

    def esquivar(self, oponente):
        defensa_porcentaje = (self.defensa * 30) / 100
        ataque_recibido = oponente.ataque - defensa_porcentaje
        numero_aleatorio = random.randint(1, 3)
        if numero_aleatorio == 2:
            print(f"\nEsquivaste el ataque de tu oponente, tu vida actual es: {self.vida:.2f}")
        else:
            self.vida -= ataque_recibido
            print(f"\nNo pudiste esquivar el ataque de tu oponente, tu vida actual es de: {self.vida:.2f}")

class Mago(Personaje):
    def __init__(self, nombre, vida, ataque, defensa):
        super().__init__(nombre, vida, ataque, defensa)
        defensa_reducida = (defensa * 5) / 100
        vida_reducida = (vida * 10) / 100
        self.ataque = ataque * 3
        self.vida = vida - vida_reducida
        self.defensa = defensa - defensa_reducida

    def ataque_especial(self,oponente):
        #Ataque que ignora la defensa
        print("\nEL ATAQUE ESPECIAL SE ESTÁ EJECUTANDO")
        probabilidad_golpe = random.random()
        if probabilidad_golpe <= 0.6:
            print(f"El luchador {self.nombre} atacó a {oponente.nombre} con su ATAQUE ESPECIAL y golpeó")
            oponente.vida -= self.ataque
            if oponente.vida <= 0:
                print(f"\nEl oponente {oponente.nombre} perdió, el ganador es {self.nombre}")
            else:
                print(f"\nEl ATAQUE ESPECIAL infligió {self.ataque:.2f} de daño al oponente, la vida del oponente {oponente.nombre} es de {oponente.vida:.2f}")
        else:
            print(f"El luchador {self.nombre} atacó a {oponente.nombre} con su ATAQUE ESPECIAL y falló")

class Guerrero(Personaje):
    def __init__(self, nombre, vida, ataque, defensa):
        super().__init__(nombre, vida, ataque, defensa)
        self.ataque = ataque * 2

    def ataque_especial(self,oponente):
        #Ataca 3 veces
        print("\nEL ATAQUE ESPECIAL SE ESTÁ EJECUTANDO")
        defensa_porcentaje = (oponente.defensa * 30) / 100
        ataque_berserker = self.ataque * 3
        ataque_recibido = ataque_berserker - defensa_porcentaje
        probabilidad_golpe = random.random()
        if probabilidad_golpe <= 0.6:
            print(f"El luchador {self.nombre} atacó a {oponente.nombre} con su ATAQUE ESPECIAL y golpeó")
            oponente.vida -= ataque_recibido
            if oponente.vida <= 0:
                print(f"\nEl oponente {oponente.nombre} perdió, el ganador es {self.nombre}")
            else:
                print(f"\nEl ATAQUE ESPECIAL infligió {ataque_recibido:.2f} de daño al oponente, la vida del oponente {oponente.nombre} es de {oponente.vida:.2f}")
        else:
            print(f"El luchador {self.nombre} atacó a {oponente.nombre} con su ATAQUE ESPECIAL y falló")

class Arquero(Personaje):
    def __init__(self, nombre, vida, ataque, defensa):
        super().__init__(nombre, vida, ataque, defensa)
        defensa_reducida = (defensa * 15) / 100
        vida_reducida = (vida * 15) / 100
        self.ataque = ataque * 3
        self.vida = vida - vida_reducida
        self.defensa = defensa - defensa_reducida

    def ataque_especial(self,oponente):
        #Hace un 60% mas de daño
        print("\nEL ATAQUE ESPECIAL SE ESTÁ EJECUTANDO")
        daño_porcentaje = (self.ataque * 60) / 100
        ataque_mejorado = self.ataque + daño_porcentaje
        defensa_porcentaje = (oponente.defensa * 30) / 100
        ataque_recibido = ataque_mejorado - defensa_porcentaje
        probabilidad_golpe = random.random()
        if probabilidad_golpe <= 0.6:
            print(f"El luchador {self.nombre} atacó a {oponente.nombre} con su ATAQUE ESPECIAL y golpeó")
            oponente.vida -= ataque_recibido
            if oponente.vida <= 0:
                print(f"\nEl oponente {oponente.nombre} perdió, el ganador es {self.nombre}")
            else:
                print(f"\nEl ATAQUE ESPECIAL infligió {ataque_recibido:.2f} de daño al oponente, la vida del oponente {oponente.nombre} es de {oponente.vida:.2f}")
        else:
            print(f"El luchador {self.nombre} atacó a {oponente.nombre} con su ATAQUE ESPECIAL y falló")

mago = Mago("Gandalf", 200, 10, 30)
guerrero = Guerrero("Aragorn", 200, 10, 30)
arquero = Arquero("Legolas", 200, 10, 30)



class Juego:
    def iniciar_combate(self, p1, p2):
        juego_en_progreso = True

        while juego_en_progreso:
            iniciar = input("\n¿Querés iniciar el juego? (S/N): ").lower()
            if iniciar == "s":
                while p1.vida > 0 and p2.vida > 0:
                    # Turno de p1
                    print(f"\n# Turno de {p1.nombre}")
                    print("\nPuedes ATACAR, DEFENDER, ESQUIVAR o ATAQUE ESPECIAL")
                    decision_p1 = input("\n¿Qué opción prefieres? (A/D/E/S): ").lower()
                    if decision_p1 == "a":
                        p1.atacar(p2)
                        if p2.vida <= 0:
                            print(f"\n{p2.nombre} ha sido derrotado. ¡{p1.nombre} es el ganador!")
                            juego_en_progreso = False
                            break
                    elif decision_p1 == "d":
                        p1.defender(p2)
                        if p1.vida <= 0:
                            print(f"\n{p1.nombre} ha sido derrotado. ¡{p2.nombre} es el ganador!")
                            juego_en_progreso = False
                            break
                    elif decision_p1 == "e":
                        p1.esquivar(p2)
                        if p1.vida <= 0:
                            print(f"\n{p1.nombre} ha sido derrotado. ¡{p2.nombre} es el ganador!")
                            juego_en_progreso = False
                            break
                    elif decision_p1 == "s":
                        p1.ataque_especial(p2)
                        if p1.vida <= 0:
                            print(f"\n{p1.nombre} ha sido derrotado. ¡{p2.nombre} es el ganador!")
                            juego_en_progreso = False
                            break

                    # Turno de p2
                    print(f"\n# Turno de {p2.nombre}")
                    print("\nPuedes ATACAR, DEFENDER, ESQUIVAR o ATAQUE ESPECIAL")
                    decision_p2 = input("\n¿Qué opción prefieres? (A/D/E/S): ").lower()
                    if decision_p2 == "a":
                        p2.atacar(p1)
                        if p1.vida <= 0:
                            print(f"\n{p1.nombre} ha sido derrotado. ¡{p2.nombre} es el ganador!")
                            juego_en_progreso = False
                            break
                    elif decision_p2 == "d":
                        p2.defender(p1)
                        if p2.vida <= 0:
                            print(f"\n{p2.nombre} ha sido derrotado. ¡{p1.nombre} es el ganador!")
                            juego_en_progreso = False
                            break
                    elif decision_p2 == "e":
                        p2.esquivar(p1)
                        if p2.vida <= 0:
                            print(f"\n{p2.nombre} ha sido derrotado. ¡{p1.nombre} es el ganador!")
                            juego_en_progreso = False
                            break
                    elif decision_p2 == "s":
                        p2.ataque_especial(p1)
                        if p2.vida <= 0:
                            print(f"\n{p2.nombre} ha sido derrotado. ¡{p1.nombre} es el ganador!")
                            juego_en_progreso = False
                            break
            elif iniciar == "n":
                print("\nGracias por participar")
                juego_en_progreso = False
            else:
                print("\nEsa no es una opción válida")

juego = Juego()
juego.iniciar_combate(mago, arquero)
