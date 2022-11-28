# -*- coding: utf-8 -*-
"""
Created on Mon Oct  3 16:41:22 2022

@author: kevin
"""
#Ejercicio 1
lista=[2,4,6,8,10]
x=0
suma=0
while x <len(lista):
    suma=suma+lista[x]
    x=x+1

print("La suma de todos sus elementos es")    
print(suma)    



#Ejercicio 2
meses=["enero", "febrero", "marzo", "abril"]
print(meses[0]) 
print(meses[3]) 




##Ejercicio 3 Definir por asignación una lista con 8 elementos enteros. Contar (ciclo) cuantos
#de dichos valores almacenan un valor superior a 100. Mostrar los elementos de
#la lista y los valores superiores a 100.
lista=[20,50,103,203,1,524,4,98]
x=0
mayores=0
print("Los elementos de la lista son ",lista)
print("Numeros mayores a 100 ")
while x<len(lista):
    if lista[x]>100:
        mayores=mayores+1

        print(lista[x])
    x=x+1
    

#Ejercicio 4 Definir una lista por asignación con 5 enteros. Mostrar por pantalla (ciclo) solo
#los elementos con valor iguales o superiores a 7.


lista=[2,5,10,8,3]
x=0
contador=0
print("Los elementos de la lista son: ")
print(lista)
print("Los valores mayores o iguales a 7: ")
while x<len(lista):
    if lista[x]>=7:
        contador=contador+1
        print(lista[x])
    x=x+1
 
        
    