print ("Binvenido al programa de calculo de IMC")
print ("Ingrese su nombre")
nombre = input()
print ("Hola " + nombre)
print ("Ingrese sus apellidos")
apellidos = input()
print ("Ingrese su edad")
edad = int(input())
print (" Ingrese su peso en kilogramos ")
peso = float(input())
print (" Ingrese su estatura en metros expresado en formato decimal (ejemplo: 1.75)")
estatura = float(input())


#Calculo del IMC
imc = float(peso) / (float(estatura) * float(estatura))

if imc < 18.5:
    categoria = "bajo peso"
elif imc >= 18.5 and imc < 25:
    categoria = "peso normal"
elif imc >= 25 and imc < 30:
    categoria = "sobrepeso"
else:
    categoria = "obesidad"

    #Resultado final
    print ("ººººººººResultadosººººº")
    
print ("nombre: " + nombre + " " + apellidos)
print ("edad: " + str(edad))
print ("IMC calculado es : " + str(imc))
print ("categoria: " + categoria)