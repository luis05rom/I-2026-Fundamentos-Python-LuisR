from seleccion import seleccion

seleccion.pais=input("Ingrese el pais de la seleccion: ")
confederacion=input("Ingrese la confederacion de la seleccion: ")
seleccion=seleccion(pais,confederacion)
argentina=seleccion("Argentina","Conmebol")
brasil=seleccion("Brasil","Conmebol")
espanna=seleccion("España","UEFA")


argentina.agregar_jugador("Messi")
argentina.agregar_jugador("Di Maria")
brasil.agregar_jugador("Neymar")
espanna.agregar_jugador("Pedri")
espanna.agregar_jugador("Gavi")
