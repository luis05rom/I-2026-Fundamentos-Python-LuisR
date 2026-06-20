d





print("Cajero automático")
print("Bienvenido al cajero")
saldo = 10000

while True:
    print("1. Consultar saldo")
    print("2. Retirar dinero")
    print("3. Depositar dinero")
    print("4. Salir")
    
    opcion = int(input("Seleccione una opción: "))
    
    if opcion == 1:
        print("Su saldo es:", saldo)
        with open(r"/Users/luisalonsorivera/Documents/GitHub/I-2026-Fundamentos-Python-LuisR/Cajero/informacion.txt", "a") as archivo:
            archivo.write(f"Saldo consultado: {saldo}\n")
            archivo.close()
    elif opcion == 2:

        cantidad = int(input("Ingrese la cantidad a retirar: "))
        
        if cantidad > saldo:
            print("Saldo insuficiente")
        else:
            saldo = saldo - cantidad
            with open(r"/Users/luisalonsorivera/Documents/GitHub/I-2026-Fundamentos-Python-LuisR/Cajero/informacion.txt", "a") as archivo:
                archivo.write(f"Retiro realizado: {cantidad}\n")
                archivo.close()
            print("Retiro exitoso. Su nuevo saldo es:", saldo)

    elif opcion == 3:
        cantidad = int(input("Ingrese la cantidad a depositar: "))
        saldo = saldo + cantidad
        with open(r"/Users/luisalonsorivera/Documents/GitHub/I-2026-Fundamentos-Python-LuisR/Cajero/informacion.txt", "a") as archivo:
            archivo.write(f"Depósito realizado: {cantidad}\n")
            archivo.close()
        print("Depósito exitoso. Su nuevo saldo es:", saldo)

    elif opcion == 4:
        print("Gracias por usar el cajero. ¡Hasta luego!")
        break
    else:
        print("Opción no valida")
