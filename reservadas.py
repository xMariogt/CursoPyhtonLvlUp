def saludar():
    print("Saludos a todos")

saludar()

#esta variable es un string
nombre = "Mario"
apellido = "Chavarria"
print(nombre)

#Enteros
edad = 20

#decimal 
peso = 2.65
print(type(peso))

#boolean
valor = True
print(type(valor))

#concatenar strings
print(f'{nombre} {apellido}')

#Listas
alumnos = ["Angel", "Manuel", "Miguel"]
#uso de indices
print(alumnos[2])

#Diccionarios
persona = {
    "Nombre" : "Mario",
    "Apellido" : "Chavarria",
    "edad" : 20,
    "Altura" : 1.70
}

print(persona["Altura"])

#se puede crear una lista de diccionarios
estudiantes = [{'nombre': 'Jose', 'apellido' : 'Hernandez'},
               {'nombre': 'Daniel', 'apellido' : 'Perez'},
               {'nombre': 'Andre', 'apellido' : 'Paz'}
]

print(estudiantes[2]['apellido'])
