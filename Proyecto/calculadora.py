from colorama import init, Fore
# pip install colorama

init()
class Calculadora:
    def __init__(self, celcius, fahrenheit):
        self.celcius = celcius
        self.fahrenheit = fahrenheit

    def convertir_celcius_a_fahrenheit(self):
        return (self.celcius * 9/5) + 32

    def convertir_fahrenheit_a_celcius(self):
        return (self.fahrenheit - 32) * 5/9
    
    def convertir_longitud(self, kilometros,metros,centimetros,milimetros,millas,pies,pulgadas):
        self.kilometros = 1000
        self.metros = 1
        self.centimetros = 0.01
        self.milimetros = 0.001
        self.millas = 1909
        self.pies = 3.281
        self.pulgadas = 39.3701

def main():
    calculadora = Calculadora()
    print("Bienvenido al convertidor de unidades")

    while True:
        #menu pricipal
        print(Fore.LIGHTBLUE_EX + "1. Temperatura")
        print(Fore.MAGENTA + "2. Longitud")
        print(Fore.GREEN + "3. Salir")
        opcion = int(input("Ingrese su opción: "))

    if opcion == 1:
        print(Fore.LIGHTBLUE_EX + "Seleccione la opción de temperatura:")
        print("1. Celcius a Fahrenheit")
        print("2. Fahrenheit a Celcius")
        opcion_temp = int(input("Ingrese su opción: "))
        # opcion de temperatura a convertir
        if opcion_temp == 1:
            celcius = float(input("Ingrese la temperatura en Celcius: "))
            calculadora = Calculadora(celcius=celcius)
            resultado = calculadora.convertir_celcius_a_fahrenheit()
            print(Fore.LIGHTBLUE_EX + f"{celcius} grados Celcius son {resultado} grados Fahrenheit")
        elif opcion_temp == 2:
            fahrenheit = float(input("Ingrese la temperatura en Fahrenheit: "))
            calculadora = Calculadora(fahrenheit=fahrenheit)
            resultado = calculadora.convertir_fahrenheit_a_celcius()
            print(Fore.LIGHTBLUE_EX + f"{fahrenheit} grados Fahrenheit son {resultado} grados Celcius")
        else:
            print(Fore.RED +  "Opción no válida")
# opcion 2 de longitud
    if opcion == 2:     
        print(Fore.MAGENTA + "Ingrese su opcion de longitud:")
        print(Fore.MAGENTA + "1. Kilometros ")
        print(Fore.MAGENTA + "2. Metros ")
        print(Fore.MAGENTA + "3. Centimetros ")
        print(Fore.MAGENTA + "4. Milimetros ")
        print(Fore.MAGENTA + "5. Millas ")
        print(Fore.MAGENTA + "6. Pies ")
        print(Fore.MAGENTA + "7. Pulgadas ")
        opcion_longitud = int(input("Ingrese su opción: "))
      
        #elegir la distacia a de kilometros al resto 
        if opcion_longitud == 1:
            print(Fore.MAGENTA + "Convertir Kilometros a Metros")
            print(Fore.MAGENTA + "Convertir Kilometros a Centimetros")
            print(Fore.MAGENTA + "Convertir Kilometros a Milimetros")
            print(Fore.MAGENTA + "Convertir Kilometros a Millas")
            print(Fore.MAGENTA + "Convertir Kilometros a Pies")
            print(Fore.MAGENTA + "Convertir Kilometros a Pulgadas")
            kilometros = float(input("Ingrese la longitud en kilometros: "))
            # de kilometros al resto de unidades
            if  kilometros == 1:
             resultado = convertir_longitud(kilometros=kilometros)
              print(f"{kilometros} kilometros son {resultado} metros")
                if kilometros == 2:
                 resultado = convertir_longitud(kilometros=centimetros)
                 print(f"{kilometros} kilometros son {resultado} centimetros")
                if kilometros == 3:
                 resultado = convertir_longitud(kilometros=milimetros)
                 print(f"{kilometros} kilometros son {resultado} milimetros")
                if kilometros == 4:
                 resultado = convertir_longitud(kilometros=millas)
                 print(f"{kilometros} kilometros son {resultado} millas")
                if kilometros == 5:
                 resultado = convertir_longitud(kilometros=pies)
                 print(f"{kilometros} kilometros son {resultado} pies")
                if kilometros == 6:
                 resultado = convertir_longitud(kilometros=pulgadas)
                 print(f"{kilometros} kilometros son {resultado} pulgadas")

            # meytros a las demas unidades
        if opcion_longitud == 2:
            print(Fore.MAGENTA + "Convertir Metros a Kilometros")
            print(Fore.MAGENTA + "Convertir Metros a Centimetros")
            print(Fore.MAGENTA + "Convertir Metros a Milimetros")
            print(Fore.MAGENTA + "Convertir Metros a Millas")
            print(Fore.MAGENTA + "Convertir Metros a Pies")
            print(Fore.MAGENTA + "Convertir Metros a Pulgadas")
            metros = float(input("Ingrese la longitud en metros: "))
            if  metros == 1:
                resultado = convertir_longitud(metros=kilometros)
                print(Fore.MAGENTA + f"{metros} metros son {resultado} kilometros")
            if metros == 2:
                resultado = convertir_longitud(metros=centimetros)
                print(Fore.MAGENTA + f"{metros} metros son {resultado} centimetros") 
            if metros == 3:
                resultado = convertir_longitud(metros=milimetros)
                print(Fore.MAGENTA + f"{metros} metros son {resultado} milimetros")
            if metros == 4:
                resultado = convertir_longitud(metros=millas)
                print(Fore.MAGENTA + f"{metros} metros son {resultado} millas")
            if metros == 5:
                resultado = convertir_longitud(metros=pies)
                print(Fore.MAGENTA + f"{metros} metros son {resultado} pies")
            if metros == 6:
                resultado = convertir_longitud(metros=pulgadas)
                print(Fore.MAGENTA + f"{metros} metros son {resultado} pulgadas")

                #eleccion centimetros a las demas unidades 
         if opcion_longitud == 3:
            print(Fore.MAGENTA + "Convertir Centimetros a Kilometros")
            print(Fore.MAGENTA + "Convertir Centimetros a Metros")
            print(Fore.MAGENTA + "Convertir Centimetros a Milimetros")
            print(Fore.MAGENTA + "Convertir Centimetros a Millas")
            print(Fore.MAGENTA + "Convertir Centimetros a Pies")
            print(Fore.MAGENTA + "Convertir Centimetros a Pulgadas")
            centimetros = float(input("Ingrese la longitud en centimetros: "))
            if  centimetros == 1:
                resultado = convertir_longitud(centimetros=kilometros)
                print(Fore.MAGENTA + f"{centimetros} centimetros son {resultado} kilometros")
            if centimetros == 2:
                resultado = convertir_longitud(centimetros=metros)
                print(Fore.MAGENTA + f"{centimetros} centimetros son {resultado} metros") 
            if centimetros == 3:
                resultado = convertir_longitud(centimetros=milimetros)
                print(Fore.MAGENTA + f"{centimetros} centimetros son {resultado} milimetros")
            if centimetros == 4:
                resultado = convertir_longitud(centimetros=millas)
                print(Fore.MAGENTA + f"{centimetros} centimetros son {resultado} millas")
            if centimetros == 5:
                resultado = convertir_longitud(centimetros=pies)
                print(Fore.MAGENTA + f"{centimetros} centimetros son {resultado} pies")
            if centimetros == 6:
                resultado = convertir_longitud(centimetros=pulgadas)
                print(Fore.MAGENTA + f"{centimetros} centimetros son {resultado} pulgadas") 

                #opcion de milimetros a lo demas unidades
      if opcion_longitud == 4:
            print(Fore.MAGENTA + "Convertir Milimetros a Kilometros")
            print(Fore.MAGENTA + "Convertir Milimetros a Metros")
            print(Fore.MAGENTA + "Convertir Milimetros a Centimetros")
            print(Fore.MAGENTA + "Convertir Milimetros a Millas")
            print(Fore.MAGENTA + "Convertir Milimetros a Pies")
            print(Fore.MAGENTA + "Convertir Milimetros a Pulgadas")
            milimetros = float(input("Ingrese la longitud en milimetros: "))
            if  milimetros == 1:
                resultado = convertir_longitud(milimetros=kilometros)
                print(Fore.MAGENTA + f"{milimetros} milimetros son {resultado} kilometros")
            if milimetros == 2:
                resultado = convertir_longitud(milimetros=metros)
                print(Fore.MAGENTA + f"{milimetros} milimetros son {resultado} metros") 
            if milimetros == 3:
                resultado = convertir_longitud(milimetros=centimetros)
                print(Fore.MAGENTA + f"{milimetros} milimetros son {resultado} centimetros")
            if milimetros == 4:
                resultado = convertir_longitud(milimetros=millas)
                print(Fore.MAGENTA + f"{milimetros} milimetros son {resultado} millas")
            if milimetros == 5:
                resultado = convertir_longitud(milimetros=pies)
                print(Fore.MAGENTA + f"{milimetros} milimetros son {resultado} pies")
            if milimetros == 6:
                resultado = convertir_longitud(milimetros=pulgadas)
                print(Fore.MAGENTA + f"{milimetros} milimetros son {resultado} pulgadas")

                #opcion de. millas a las demas unidades
        if opcion_longitud == 5:
            print(Fore.MAGENTA + "Convertir Millas a Kilometros")
            print(Fore.MAGENTA + "Convertir Millas a Metros")
            print(Fore.MAGENTA + "Convertir Millas a Centimetros")
            print(Fore.MAGENTA + "Convertir Millas a Milimetros")
            print(Fore.MAGENTA + "Convertir Millas a Pies")
            print(Fore.MAGENTA + "Convertir Millas a Pulgadas")
            millas = float(input("Ingrese la longitud en millas: "))
            if  millas == 1:
                resultado = convertir_longitud(millas=kilometros)
                print(Fore.MAGENTA + f"{millas} millas son {resultado} kilometros")
            if millas == 2:
                resultado = convertir_longitud(millas=metros)
                print(Fore.MAGENTA + f"{millas} millas son {resultado} metros") 
            if millas == 3:
                resultado = convertir_longitud(millas=centimetros)
                print(Fore.MAGENTA + f"{millas} millas son {resultado} centimetros")
            if millas == 4:
                resultado = convertir_longitud(millas=milimetros)
                print(Fore.MAGENTA + f"{millas} millas son {resultado} milimetros")
            if millas == 5:
                resultado = convertir_longitud(millas=pies)
                print(Fore.MAGENTA + f"{millas} millas son {resultado} pies")
            if millas == 6:
                resultado = convertir_longitud(millas=pulgadas)
                print(Fore.MAGENTA + f"{millas} millas son {resultado} pulgadas")

             #opcion de pies a las demas unidades
        if opcion_longitud == 6:
            print(Fore.MAGENTA + "Convertir Pies a Kilometros")
            print(Fore.MAGENTA + "Convertir Pies a Metros")
            print(Fore.MAGENTA + "Convertir Pies a Centimetros")
            print(Fore.MAGENTA + "Convertir Pies a Milimetros")
            print(Fore.MAGENTA + "Convertir Pies a Millas")
            print(Fore.MAGENTA + "Convertir Pies a Pulgadas")
            pies = float(input("Ingrese la longitud en pies: "))
            if  pies == 1:
                resultado = convertir_longitud(pies=kilometros)
                print(Fore.MAGENTA + f"{pies} pies son {resultado} kilometros")
            if pies == 2:
                resultado = convertir_longitud(pies=metros)
                print(Fore.MAGENTA + f"{pies} pies son {resultado} metros") 
            if pies == 3:
                resultado = convertir_longitud(pies=centimetros)
                print(Fore.MAGENTA + f"{pies} pies son {resultado} centimetros")
            if pies == 4:
                resultado = convertir_longitud(pies=milimetros)
                print(Fore.MAGENTA + f"{pies} pies son {resultado} milimetros")
            if pies == 5:
                resultado = convertir_longitud(pies=millas)
                print(Fore.MAGENTA + f"{pies} pies son {resultado} millas")
            if pies == 6:
                resultado = convertir_longitud(pies=pulgadas)
                print(Fore.MAGENTA + f"{pies} pies son {resultado} pulgadas")

             #opcion de pulgadas a las demas unidades
        if opcion_longitud == 7:
            print(Fore.MAGENTA + "Convertir Pulgadas a Kilometros")
            print(Fore.MAGENTA + "Convertir Pulgadas a Metros")
            print(Fore.MAGENTA + "Convertir Pulgadas a Centimetros")
            print(Fore.MAGENTA + "Convertir Pulgadas a Milimetros")
            print(Fore.MAGENTA + "Convertir Pulgadas a Millas")
            print(Fore.MAGENTA + "Convertir Pulgadas a Pies")
            pulgadas = float(input("Ingrese la longitud en pulgadas: "))
            if  pulgadas == 1:
                resultado = convertir_longitud(pulgadas=kilometros)
                print(Fore.MAGENTA + f"{pulgadas} pulgadas son {resultado} kilometros")
            if pulgadas == 2:
                resultado = convertir_longitud(pulgadas=metros)
                print(Fore.MAGENTA + f"{pulgadas} pulgadas son {resultado} metros") 
            if pulgadas == 3:
                resultado = convertir_longitud(pulgadas=centimetros)
                print(Fore.MAGENTA + f"{pulgadas} pulgadas son {resultado} centimetros")
            if pulgadas == 4:
                resultado = convertir_longitud(pulgadas=milimetros)
                print(Fore.MAGENTA + f"{pulgadas} pulgadas son {resultado} milimetros")
            if pulgadas == 5:
                resultado = convertir_longitud(pulgadas=millas)
                print(Fore.MAGENTA + f"{pulgadas} pulgadas son {resultado} millas")
            if pulgadas == 6:
                resultado = convertir_longitud(pulgadas=pies)
                print(Fore.MAGENTA + f"{pulgadas} pulgadas son {resultado} pies")
    if opcion == 3:
            
        




        