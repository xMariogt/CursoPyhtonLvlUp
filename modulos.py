#import reservadas
#reservadas.saludar()

#from reservadas import * #Obtiene todo lo que se encuentre en el modulo y permite utilizarlo
#saludar()

#from reservadas import saludar, nombre #Permite importar ciertos atributos del modulo
#print(nombre)
#saludar()

#*******************************************************************************************
#Se realiza lo siguiente para poder utilizar modulos que esten dentro de otras carpetas

#import sys

#sys.path.append(r'C:\Users\Mario\Desktop\CursoPythonLvlUP\importar\modulo')
#import os
#os.environ['PYTHONPATH'] = "C:/Users/Mario/Desktop/CursoPythonLvlUP/importar/modulo"
#import modulo 
#print(modulo.x)

#*********************************************************************************************
#Manejo de excepciones

#try:
#    import moduloinexistente
#except ModuleNotFoundError as e:
#    print("Ups, no se pudo importar el modulo.", e)

#print("Hola")
#*****************************************************************************************
#para solo definir el codigo
#En el modulo caminar se utiliza un if para que las funciones no se ejecuten directamente al importar, solo cuando se haga el llamado a un metodo o variable

#import caminar

#caminar.avanzar()
#*****************************************************************************************

#Para hacer que toda una carpeta funcione como un modulo
#Utilizamos modulo_carpeta como ejemplo

import modulo_carpeta

print(modulo_carpeta.y)

