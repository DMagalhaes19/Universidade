# -*- coding: utf-8 -*-
"""
Created on Tue Nov  3 10:05:16 2020

@author: alexd
"""
#Exercicio 3 alinea a)
def areaRetangulo(b,a):
     return b*a

base=int(input("Introduza o valor da base: "))
aresta=int(input("Introduza o valor da aresta: "))
print("A area do retangulo é: ",areaRetangulo(base,aresta))


#Exercicio 3 alinea b)
def areatrapezoide(b1,b2,h):
    area=(b1*b2)/2*h
    return area        

base1= int(input("Introduza a primeira base: "))
base2= int(input("Introduza a segunda base: "))
hipotenusa =int(input("Introduza a hipotenusa: "))

print("A area do trapezoide é:",areatrapezoide(base1, base2, hipotenusa))

#Exercicio 3 alinea c)
import math
def areaTriangulo(a,b,c):
    s=(a+b+c)/2
    total=(s-a)*(s-b)*(s-c)
    total1= math.sqrt(s*total)
    return total1 

a= int(input("Introduza o primeiro valor: "))
b= int(input("Introduza o segundo valor: "))
c= int(input("Introduza o terceiro valor: "))
print("A area do triangulo é:", areaTriangulo(a, b, c))
