class temperatura:
    def _int_(self,temperatura,celcius,farenheit):
        self.temperatura=temperatura
        self.celcius=celcius
        self.farenheit=farenheit
    def convertir_celcius_a_farenheith(self,celcius):
        farenheit=(celcius*9/5)+32
        def convertir_farenheit_a_celcius(self,farenheit):
            celcius=(farenheit-32)*5/9
            
  
print("Calculadora de temperatura")
print("Ingrese una opcion para convertir la temperatura")
while True:
    print("1. Convertir de celcius a farenheit")
    print("2. Convertir de farenheit a celcius")
    opcion = int(input("Seleccione una opción: "))
    if opcion == 1:
        celcius = float(input("Ingrese la temperatura en celcius: "))
    if opcion == 2:
        fararenheit  = float(input("Ingrese la temperatura en farenheit: "))   
        
