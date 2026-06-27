from colorama import init,Fore

class convertor:
    def __init__(self,celcius,farainhith):
        self.celcius=0
        self.farainhith=0

    def convertir_celcius_a_fahrenheit(self,celcius):
        fahrenheit=(celcius*1.8) + 32
        return fahrenheit

    def convertir_fahrenheit_a_celcius(self,fahrenheit):

        return (fahrenheit - 32)/1.8
    
    def convertir_longitud(self, kilometros, metros, centimetros, milimetros, millas, pies, pulgadas):
        self.kilometros = 1000
        self.metros = 1
        self.centimetros = 0.01
        self.milimetros = 0.001
        self.millas = 1909
        self.pies = 3.281
        self.pulgadas = 39.3701

print("Bienvenido al convertor de unidades")
convertidor = 0
while True:
    print(Fore.LIGHTBLUE_EX + "1. Temperatura")
    print(Fore.MAGENTA + "2. Longitud")
    print(Fore.GREEN + "3. Salir")
    opcion = int(input("Ingrese su opcion: "))

    if opcion == 1:  # menu 
        print("Seleccione la opcion de Temperatura")
        print("1.Convertir de celcius a farainhaith")
        print("2.Convertir de farainhith a celcius")
        print("Regresar al menu principal")
        #menu temperatura
        temp = int(input("Ingrese la opcion de temperatura: "))
        if temp == 1:  # celcius a fahrenheit
            celcius = float(input("Ingrese la temperatura en celcius:"))
            fahrenheit = (celcius * 9 / 5) + 32
            print(f"Los grados celcius: {celcius} son {fahrenheit} grados fahrenheit")

        elif temp == 2: #fahrenheit a celcius
            fahrenheit = float(input("Ingrese la temperatura en fahrenheit:"))
            celcius = (fahrenheit - 32) * 5 / 9
            print(f"Los grados fahrenheit: {fahrenheit} son {celcius} grados celcius")

        elif temp == 3:
            print("Regresar")
            break

      if opcion == 2:
            print("Selecione su unidad de longitud")
            print("1. Kilometros")
            print("2. Metros")
            print("3. centimetros")
            print("4. milimetros")
            print("5. Millas")
            print("6. Pies")
            print("7. Pulgadas")
            long == int(input("Ingrese la lomgitud que desea convertir "))
            if long == 1:
                print(Fore.MAGENTA + "1. Convertir Kilometros a Metros")
                print(Fore.MAGENTA + "2. Convertir Kilometros a Centimetros")
                print(Fore.MAGENTA + "3. Convertir Kilometros a Milimetros")
                print(Fore.MAGENTA + "4. Convertir Kilometros a Millas")
                print(Fore.MAGENTA + "5. Convertir Kilometros a Pies")
                print(Fore.MAGENTA + "6. Convertir Kilometros a Pulgadas")
                long = float(input("Ingrese la longitud en kilometros: "))
                if long == 1:
                    kilometros == int(input("Ingrese la cantidad de Kilometros"))
                    metros= kilometros * 1000
                    print(f"{kilometros} son: {metros}")
                
                if long == 2:
                    kilometros == int(input("Ingrese la cantidad de Kilometros"))
                    centimetros = kilometros * 1000000
                    print(f"{kilometros} son: {centimetros}")

                if long == 3:
                    kilometros == int(input("Ingrese la cantidad de Kilometros"))
                    milimetros= kilometros * 1000000
                    print(f"{kilometros} son: {milimetros}")   

                if lomg == 4:
                    kilometros == int(input("Ingrese la cantidad de Kilometros"))
                    millas = kilometros * 0.6213
                    print(f"{kilometros} son: {millas}")    





            

            
            
            

   


          



 
    




  
    
   