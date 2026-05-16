
#inicializar variables 
nombre = "luis"
#preguntar por la edad
edad: int = int(input("¿Cual es tu edad:"))
#calculo del año de nacimiento
anno_de_nacimiento:int = 2026 -edad

#ver el año de nacimiento del usuario y verificar si es mayor de edad 
print (anno_de_nacimiento)
mayor_de_edad:bool = edad >= 18
print(mayor_de_edad)

#comparaciones del usuario para verificar el usuario
no_soy_yo = not ( nombre == "luis" and edad == 22)
soy_yo = nombre == "luis" and edad == 22
quizas_soy_yo = (nombre == "luis" or edad == 22)

#resultados de las comparaciones 
print (soy_yo)
print(no_soy_yo)
print(quizas_soy_yo)
 

