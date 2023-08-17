# -*- coding: utf-8 -*-
"""
Created on Tue Nov 24 10:54:07 2020

@author: alexd
"""
#only_string(l) Retorna uma lista apenas com os elementos do tipo string em l (ver função isinstance).
def only_string(l):
    aux=[]
    for i in range(len(l)):
        if(isinstance(l[i],str) == True):
            aux.append(l[i])
        else:
            continue
    return aux

#int_average(l) Retorna a média de todos os valores inteiros em l.
def int_average(l):
     soma = 0
     avg = 0
     idx = 0
     for i in range(len(l)):
         if(isinstance(l[i], int)== True):
             soma = soma + l[i]
            
         avg = soma / len(l)
         return avg

#round_floats(l) Altera a lista l, substituindo todos os float por um arredondamento int.
def round_floats(l):
    for i in range(len(l)):
        if(isinstance(l[i], float)==True):
            l[i] = round(l[i])
    return l
            

lista_1 = ["Paulo",10.25,35.5,"Andre",7]
print(only_string(lista_1))
print(int_average(lista_1))
print(round_floats(lista_1))