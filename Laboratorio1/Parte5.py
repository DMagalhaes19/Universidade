# -*- coding: utf-8 -*-
"""
Created on Tue Nov  3 10:06:56 2020

@author: alexd
"""
#Parte 5 alinea a)

num=0
num1=1
numero= int(input("Qual e o valor que pretende encontrar em f(x): "))
for i in range(numero):
    idx=num1
    num1= num+num1
    num=idx
print(num1)
#exercicio 5 b)

num=0
num1=1
for i in range(2020):
    idx=num1
    num1= num+num1
    num=idx
print(num1)