# -*- coding: utf-8 -*-
"""
Created on Tue Nov 24 08:38:55 2020

@author: alexd
"""
#length(l) Retorna o comprimento da lista. Não pode utilizar a função len.
def lenght(l):
    idx = 0
    for i in range(l):
        idx += i
    return idx

#same_length(l1, l2) Retorna True se as duas listas forem do mesmo tamanho. Utilize a função length acima.

def same_lenght(l1,l2):
    elem_l1=lenght(l1)
    elem_l2=lenght(l2)
    if(elem_l1 == elem_l2):
        return True
    else:
        return False
#count_reps(l) Retorna uma lista com todos os valores repetidos em l, i.e., todos os valores que surgem mais que uma vez.    
def count_reps(l):
    cnt = 0
    idx = 0
    for i in range(l):
        if(idx[i] == l[i]):
            cnt+=1
        else:
            continue
    return cnt

#clear_reps(l) Retorna uma lista com os elementos de l, sem repetições.
def clear_reps(l):
    idx = 0
    for i in range(l):
        if(idx[i] == l[i]):
            l.remove(i)
        else:
            continue
    return l

lista1= [1,2,3,45,"Andre",5,45]        
lista2= [1,2,3,45,"Andre",5,45]        
tamanho = lenght(lista1)
print(tamanho)
if(same_lenght(lista1, lista2) == True):
    print("Verdadeiro")
print(count_reps(lista1))
print(clear_reps(lista1))