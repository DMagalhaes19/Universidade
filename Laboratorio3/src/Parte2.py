# -*- coding: utf-8 -*-
"""
Created on Tue Nov 24 08:56:27 2020

@author: alexd
"""
#sum_extremes(l) Retorna a soma do primeiro e último elementos da lista.

def sum_extremes(l):
    soma = l[-1] + l[0]
    return soma

#print_list(l) Imprime todos (um por cada linha) os elementos da lista.
def print_list(l):
    for i in range(0,len(l)):
        print("[{}] representa {} na lista fornecida".format(i, l[i]))

#sort_list(l, descend=False) Retorna uma cópia da lista, ordenada de acordo com o parâmetro descend (i.e., se este for True, a ordenação deve ser descendente).
def sort_list(l,descend):
    if(descend == True):
        for i in range(0,len(l)):
            for j in range(len(l)-1):
                if(l[j] > l[j+1]):
                    idx = l[j]
                    l[j] = l[j+1]
                    l[j+1] = idx
        return l
    elif(descend == False):
        for i in range(0,len(l)):
            for j in range(len(l)-1):
                if(l[j]<l[j+1]):
                    idx = l[j]
                    l[j] = l[j+1]
                    l[j+1] = idx
        return l
                
#min_max(l) Retorna uma lista com dois valores: o mínimo e o máximo da lista l.
def min_max(l):
    max_number= l[0]
    min_number= l[0]
    for i in range(0,len(l)):
        if(l[i]>max_number):
            max_number = l[i]
        elif(l[i]<min_number):
            min_number = l[i]
    return max_number,min_number

# =============================================================================
# sum_positions(l1, l2) Retorna uma lista onde cada elemento é o resultado a soma dos
# elementos em l1 e l2 na mesma posição. A lista resultante deve ter o tamanho da lista
# mais pequena entre l1 e l2.
# 
# =============================================================================
def sum_positions(l1,l2):
     soma = []
     aux = 0 
     if(len(l1)<len(l2)):
         for j in range(0, len(l2)-len(l1)):
                aux = l1[j]+l2[j]
                soma.append(aux)
                aux = 0
     else:
         for j in range(0,len(l1)-len(l2)):
                 aux = l1[j]+l2[j]
                 soma.append(aux)
                 aux = 0
     return soma

# =============================================================================
# append_positions(l1, l2) Retorna uma lista que intercala os elementos de l1 e l2, i.e.,
# retorna a lista rl11, l21, l12, l22, ...s. A lista resultante deve ter o tamanho da lista mais
# pequena entre l1 e l2 
# =============================================================================
def append_positions(l1,l2):
    total=[]
    if(len(l1)<len(l2)):
        for i in range(0,len(l2)-len(l1)):
            total.append(l1[i])
            total.append(l2[i])
    else:
        for i in range(0,len(l1)-len(l2)):
            total.append(l1[i])
            total.append(l2[i])
    return total
                        



lista_1 = [1,2,3,4,5,6,7,8,9,10]
lista_2 = [1,10,35,45,7]
Total=sum_extremes(lista_1)
print(Total)        
print(print_list(lista_1))
print(sort_list(lista_1, True))
print(min_max(lista_1))
print(sum_positions(lista_1, lista_2))

print(append_positions(lista_1, lista_2))