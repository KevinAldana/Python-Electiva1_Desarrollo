# -*- coding: utf-8 -*-
"""
Created on Fri Nov 11 15:29:08 2022

@author: kevin
"""
import os
#Importa libreria que permite usar funcionalidades dependientes del sistema operativo
import numpy as np
# Importa la libreria de numpy para manejar arreglos y matrices
import pandas as pd
#Importa la libreria de pandas para el analisis y estructura de grandes cantidades de datos
def defdatos(a,b,c):
    #Define una funcion con 3 parametros
    labels = ['a','b','c']
    #Crea una lista con 3 etiquetas
    my_list = [a,b,c]
    #crea otra lista con 3 valores
    arr = np.array([a,b,c])
    #Crea un arreglo con numpy utilizando 3 valores
    dicc = {'a':a,'b':b,'c':c}
    #Crea un diccionario
    print("")
    #Crea un espacio en blanco
    print(pd.Series(my_list, labels))
    #Imprime en una matrix tipo serie de pandas las 2 listas que se crearon anteriormente
    print(type(my_list))
    #Imprime el tipo al que pertenece ese valor de esa variable
    print("")
    print(pd.Series(arr,labels))
    #Imprime en una matriz tipo serie de pandas el array que creamos con numpy
    print(type(arr))
    print("")
    print(pd.Series(dicc))
    #Imprime en una matriz tipo serie de pandas el diccionario que creamos
    print(type(dicc))
n1=input("digite valor num1: ")
n2=input("digite valor num2: ")
n3=input("digite valor num3: ")
#Ingresamos los 3 valores de los parametros de la funcion
defdatos(n1,n2,n3)
#Invocamos la funcion
print("")
print(os.getcwd())
#Imprime la ruta donde nos encontramos
print(os.listdir())
#Imprime los archivos de la carpeta donde nos encontramos
print("")
print("Nómina mensual CafeFull Colombia")
nomb1="Francisco Perez"
nomb2="Amira Nieto"
nomb3="Juan Cataño"
datos = np.array([[1000000,1200000,2000000],[900000,1100000,5000000],[1300000,1400000,2000000]])
#Se crea un array de (3,3) de dimension

datosfinal= pd.DataFrame(datos,
            index=[nomb1,nomb2,nomb3],
            columns=['Octubre','Noviembre','Diciembre'])
#Se crea un dataframe de la libreria de pandas con los datos del array y dos listas creadas 

print(datosfinal)
print("")

print("Nómina mensual CafeFull Colombia")
nomb1="Francisco Perez"
nomb2="Amira Nieto"
nomb3="Juan Cataño"
#nomb4= "Juanita Mora";

datosfinal= pd.DataFrame(datos,
            index=[nomb1,nomb2,nomb3],
            columns=['Octubre','Noviembre','Diciembre'])
print(datosfinal)
#Aplicar dos Listas en un Diccionario y mostrar el Diccionario en un DataFrame

Lista1=['Nombre','Apellido','Edad']
#Se crea una lista con los datos
Lista2=['Kevin','Aldana',21]
#Se crea otra lista con la informacion de los datos

diccionario={
    'Datos':Lista1,
    'informacion':Lista2
    }
#Se crea un diccionario con las 2 listas
Datos= pd.DataFrame(diccionario)
#En un dataframe se coloca la informacion del diccionario
print(Datos)