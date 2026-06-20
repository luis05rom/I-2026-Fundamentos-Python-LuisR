class seleccion:
    def __init__(self, pais,confederacion,):
        self.pais = pais
        self.confederacion = confederacion
        self.jugadores = []#[] sirve para guardar a los jugadores de cada selección
    def agregar_jugador(self, jugador):
       self.jugadores.append(jugador)  #append sirve para agregar un nuevo jugador a la lista de jugadores de cada selección

    def eliminar_jugador(self, jugador):
        for jugador_en_lista in self.jugadores:
            if jugador_en_lista == jugador:
                self.jugadores.remove(jugador_en_lista) #ve si en la lista hay que eliminar a un jugador
                break
 
pais=input("Ingrese el pais de la seleccion: ")
confederacion=input("Ingrese la confederacion de la seleccion: ")
seleccion=seleccion(pais,confederacion)
argentina=seleccion("Argentina","Conmebol")
brasil=seleccion("Brasil","Conmebol")
espanna=seleccion  ("España","UEFA")


argentina.agregar_jugador("Messi")
argentina.agregar_jugador("Di Maria")
brasil.agregar_jugador("Neymar")
espanna.agregar_jugador("Pedri")
espanna.agregar_jugador("Gavi")

jugador_a_eliminar = input("Ingrese el nombre del jugador a eliminar: ")
seleccion.eliminar_jugador(jugador_a_eliminar)
