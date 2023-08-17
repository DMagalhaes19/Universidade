# -*- coding: utf-8 -*-
"""
Created on Tue Nov 10 09:15:03 2020

@author: alexd
"""
#Exercicio 2.1:
num= int(input("Fatorial de: "))
if(num<=0):
    print("Nao existe fatorial de: {}".format(num))
else:
    resultado=1
    for i in range(1,num+1):
        resultado *=i
        print("O fatorial de {} corresponde a {} ".format(i, resultado))

# print(math.prod(range(5,10)))

#Exercicio 2.2:
    
numero= int(input("Indique o numero ao qual pretende começar o produtorio: "))
numero2= int(input("Indique o numero que pretende chegar no produtorio: "))

if(numero<= 0):
    print("Nao existe o produtorio de: {} ".format(numero))
else:
    resultado=1
    for i in range(numero,numero2+1):
        resultado *=i
        print("O fatorial de {} começando apartir do valor {} , corresponde a {} ".format(i, numero2, resultado))    