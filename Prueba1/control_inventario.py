print("Bienvenido " )

print("Digite la cantidad de productos a registrar")
producto = int(input())

for i in range(producto): 
    print("Seleccione una opción: ")  
    print("1. Registrar producto nuevo")
    print("2. Registrar cantidad de productos disponibles")
    print("3. Calcular valor total del inventario")

    eleccion =int(input())
    if eleccion == 1:
        print("Digite el nombre del producto")
        nombre = input()
        print("Precio del porducto")
        precio = float(input())
        if precio < 0:
            print("El precio no puede ser negativo")
            print("Digite la cantidad de productos a registrar")
            producto = int(input()) 
            valor_total= precio * producto
            print("El valor total del porducto {0}es: {1}".format(nombre, valor_total))

    if eleccion == 2:
            print("Catidad disponible del producto")
            print("La cantidad disponible del producto {0} es: {1}".format(nombre, producto))
    
    else:
        print("Opción no válida")

