# -*- coding: utf-8 -*-
campo = "minefield.csv"

import numpy as np
import csv

aux = []

def ler_jogo():
    File = open(campo,"r",encoding='utf-8')
    data = File.readlines()
    for linha in data:
        linha = linha.replace(";", " ")
        aux.append(linha)
    print("\n".join(f"{c}" for c in aux))


def ler_jogo1():
    aux.clear()
    File= open(campo,"r",encoding='utf-8')
    data = File.readlines()
    matriz = []
    for linha in data:
        linha = linha.split(";")
        for idx in range(len(linha)):
            matriz = [[linha[idx] for _ in range(10)] for _ in range(5)]
    print(matriz)


def ler_jogo3():
    with open(campo,"r") as File:
        Matriz = list(csv.reader(File, delimiter=";"))    
    Lista=np.array(Matriz[:])
    print(Lista)

def contar_bombas1():
    print("\n")
    cnt = 0
    with open(campo,"r") as File:
        Matriz = list(csv.reader(File, delimiter=";"))    
    Lista=np.array(Matriz[:])
    find = np.where(Lista == "-1")
    for idx in find:
        print(idx)    
    
        

def contar_bombas_adjacentes():
    print("\n")
    Lista_aux = []
    with open(campo,"r") as File:
        Matriz = list(csv.reader(File, delimiter=";"))    
    Lista=np.array(Matriz[:])
    aux = Lista.copy()
    print(aux)
    for idx in range(-1,2):
        for j in range(-1,2):
            if((idx != 0 or j != 0) and (x+idx)>-1 and (y+j) > -1 and (x+idx) < aux and (y+j) < aux[0][0]
               if()
                Lista_aux.append[(x+idx , y+j)]
    print(Lista_aux)


# ler_jogo3()
# contar_bombas1()
contar_bombas_adjacentes()