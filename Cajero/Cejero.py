print("Cajero automático")
print("Bienvenido al cajero")
saldo = 10000
with open("/Users/luisalonsorivera/Documents/GitHub/I-2026-Fundamentos-Python-LuisR/Cajero/informacion.txt", "w") as archivo:
    while True:
        print("1. Consultar saldo")
        print("2. Retirar dinero")
        print("3. Depositar dinero")
        print("4. Salir")
        
        opcion = int(input("Seleccione una opción: "))
        if opcion == 1:
            print("Su saldo es:", saldo)
        elif opcion == 2:
            cantidad = int(input("Ingrese la cantidad a retirar: "))
            if cantidad > saldo:
                print("Saldo insuficiente")
            else:
                saldo = saldo - cantidad
                print("Retiro exitoso. Su nuevo saldo es:", saldo)
        elif opcion == 3:
            cantidad = int(input("Ingrese la cantidad a depositar: "))
            saldo = saldo + cantidad
            print("Depósito exitoso. Su nuevo saldo es:", saldo)
        elif opcion == 4:
            print("Garcias por usar el cajero. ¡Hasta luego!")
            break
        else:
            print ("Opción no valida")
