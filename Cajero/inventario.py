while True:
    print("1.Registar estudiantes")
    print("2.Ver todos los estudiantes")
    print("3.Salir")
    opcon = int(input("Seleccione una opción: "))
    if opcon == 1:
        archivo = open(r"/Users/luisalonsorivera/Documents/GitHub/I-2026-Fundamentos-Python-LuisR/Cajero/actividad.txt", "a")
        print("Ingrese el nombre del estudiante: ")
        nombre= str(input("Ingrese el nombre del estudiante: "))
        carnet= str(input("Ingrese el número de carnet del estudiante: "))
        nota= float(input("Ingrese la nota del estudiante: "))
        #Para guardar los datos en en acrchivo de texto
        archivo.write(f"Nombre: {nombre}\n")
        archivo.write(f"Carnet: {carnet}\n")
        archivo.write(f"Nota: {nota}\n")
        archivo.close()
    elif opcon == 2:
        archivo = open(r"/Users/luisalonsorivera/Documents/GitHub/I-2026-Fundamentos-Python-LuisR/Cajero/actividad.txt", "r")
        print("Ver todos los estudiantes registrados:")
        estudiantes = archivo.read()
        print(estudiantes)      
        archivo.close()
    elif opcon == 3:
        break
    print("Salir")
    break