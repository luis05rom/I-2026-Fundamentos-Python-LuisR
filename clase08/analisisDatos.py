import pandas

datos = pandas.read_csv("clase08/Estudiantes.csv")
#imprime las 5 primeras filas del dataframe
print(datos.head())

#para imprimir las columnas deeadas
print(datos[["nombre","apellido"]]).head()

# calcular estadisticas 
print(datos.describe())

#calcular el maximo de la edad
print(datos["edad"].max())

#minimo de edad 
print(datos["edad"].min())


#filtar las notas mayores a 85
estudiantes_altos=datos[datos["nota"]>85]
print(estudiantes_altos)

#agrupar filas 
media_por_genero=datos.groupby("sexo")
media_por_genero=media_por_genero["nota"].mean()
media_por_genero =datos.groupby("sexo")["nota"].mean()
print(media_por_genero )


