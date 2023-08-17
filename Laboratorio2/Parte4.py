# -*- coding: utf-8 -*-
"""
Created on Tue Nov 10 13:34:24 2020

@author: alexd
"""
#Exercicio 1
def Maior(num1,num2,num3):
    if(num1>num2):
        if(num1>num3):
            return num1
        else:
            if(num3>num2):
                return num3    
    else:
        if(num2>num3):
            return num2
        else:
            if(num3>num1):
                return num3

def Menor(num1,num2,num3):
    if(num1<num2):
        if(num1<num3):
            return num1
        else:
            if(num3<num2):
                return num3
    else:
        if(num2<num3):
            return num2
        else:
            if(num3<num1):
                return num3
            

numero1=int(input("Introduza um numero: "))
numero2=int(input("Introduza um numero: "))        
numero3=int(input("Introduza um numero: "))

highest =Maior(numero1,numero2,numero3)
lower= Menor(numero1,numero2,numero3)
print("O maior numero é {} e o menor numero é {}" .format(highest, lower))

#Exercicio 2:
def InverterFrase(frase):
    novafrase = ''
    idx= len(frase)
    while idx:
        idx-=1
        novafrase += frase[idx]
    return novafrase

def ContaVogais(frase):
    cnt=0
    idx= len(frase)
    for i in range(idx):
        if(frase[i].lower() == 'a' or frase[i].lower() == 'e' or frase[i].lower() == 'i' or frase[i].lower() == 'o' or frase[i].lower() == 'u'):
            cnt = cnt + 1
    return cnt

Palavra = str(input("Introduza uma frase que pretende inverter: "))
Conta = ContaVogais(Palavra)
inverter= InverterFrase(Palavra)
print("A frase ao contrario vai ficar desta forma: {}. E possui {} vogais".format(inverter, Conta()
                                                                                  )    

#Exercicio 3:  
def SubstituirCaracter(frase,caracter,substituir):    
    novocaracter=''
    idx = len(frase)
    for i in range(idx):
        if(frase[i].lower()==caracter):
            novocaracter = novocaracter + substituir
        else:
            novocaracter = novocaracter +  frase[i]
    return novocaracter
            
Nfrase = str(input("Introduza a sua frase: "))
Ncaracter = str(input("Introduza o caracter que deseja substituir: "))
Nsubstituir = str(input("Introduza o caracter que pretende introduzir ao inves do outro: "))

Nmaneira = SubstituirCaracter(Nfrase, Ncaracter, Nsubstituir)
print("A frase que colocou: {}. Fica desta forma {}".format(Nfrase,Nmaneira))