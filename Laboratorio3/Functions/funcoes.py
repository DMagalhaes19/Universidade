# -*- coding: utf-8 -*-
from time import sleep

alunos = "Alunos.txt"
notas = "Notas.txt"
temp = "temp.txt"

lista_auxiliar =[]
lista_auxiliar2 =[]
lista_auxiliar3 =[]

def Menu():
    print("*--------------------*")
    print("Unidade Curricular")
    print("*--------------------*")
    print("R. Registar aluno")
    print("RM. Registar notas do aluno")
    print("AM. Alterar nota")
    print("CM. Calcular media")
    print("G. Gravar ficheiro")
    print("L. Ler informação")
    print("E. Sair")
    opc= str(input("Indique a sua opção->"))
    return opc.upper()


def criarArq(arq):
    try:
        a = open(arq, "wt+")
        a.close()
    except:
        pass
    else:
        pass


def verificarArq(arq):
    try:
        a = open(arq, "rt")
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True
    
    
def register():
    aux = False
    aux2 = False
    aux3 = False
    try:
        file = open(alunos,"a")
    except:
        print("Erro ao abrir o ficheiro")
    else:
        while (aux==False):
            first_name = str(input("Introduza o seu primeiro nome: "))
            if(first_name != ""):
                aux= True
            else:
                aux= False
        while (aux2== False):
            last_name=str(input("Introduza o seu ultimo nome: "))
            if(last_name != ""):
                aux2= True
            else:
                aux2= False
    
        while(aux3== False):
            Number = int(input("Introduza o seu numero de aluno"))
            lines = ler(2)
            if (lines == []):
                aux3=True
            else:
                for idx in lines:
                    find = idx.split(";")
                    if(find == ["\n"]):
                        pass
                    else:
                        if(Number == int(find[2])):
                            print("Ja existe um aluno com esse numero")
                            aux3=False
                        else:
                            aux3=True
    finally:
        file.close()
    if(aux==True& aux2==True & aux3==True):
        lista_auxiliar.append(first_name)
        lista_auxiliar.append(last_name)
        lista_auxiliar.append(Number)

def procuraAluno(numero):
    aux = []
    lines = ler(2)
    for idx in lines:
        find = idx.split(";")
        aux.append(int(find[2]))
    if numero in aux:
        return True
    else:
        return False
    
def register_notes():
    lista_auxiliar2.clear()
    aux=[]
    number = int(input("Introduza o numero do aluno"))
    lines = ler(3)
    for idx in lines:
        idx= idx.split(";")
        if(int(idx[0]) == number):
            aux.append(idx[1])
    if(not procuraAluno(number)):
        print("Aluno nao encontrado")
        return None
    else:
        lines2 = ler(3)
        moment = None
        while(moment != "t1" & moment != "t2" & moment != "p"):
            moment =input("Primeiro teste - [T1]\n"
                          "Segundo Teste - [T2]\n"
                          "Projeto- [P]\n"
                          "Momento: ").lower().strip()
            if(moment == ""):
                return None
            else:
                for idx in lines2:
                    find = idx.split(";")
                    if int(find[0]) == number and find[1] == moment:
                        if moment == "t1": m = "primeiro teste"
                        elif moment == "t2": m = "segundo teste"
                        elif moment == "p": m = "projeto"
                        print(f"Este(a) aluno(a) já tem nota para o {m}.")
                        sleep(2)
                        return None
                    else:
                        pass
        value = float(input("Nota: "))
        while value < 0 or value > 20:
            value = float(input("A nota deve ser entre 0 e 20.\n"
                                "Nota: "))
            if value == "":
                return None
    lista_auxiliar2.append(number)
    lista_auxiliar2.append(moment)
    lista_auxiliar2.append(value)
    
def alterarNota():
    aux = []
    lista_auxiliar3.clear()
    try:
        number = int(input("Número do aluno: "))
    except:
        print(f"Dado invalido.")
        return None
    else:
        pass
    lines = ler(3)
    if not procuraAluno(number):
        print("Aluno não encontrado")
        sleep(2)
        return None
    moment = None
    while moment != "t1" and moment != "t2" and moment != "p":
        moment = input("Primeiro teste - [T1]\n"
                       "Segundo teste - [T2]\n"
                       "Projeto - [P]\n"
                       "Momento: ").lower().strip()
        if moment == "":
            return None
    for idx in lines:
        find = idx.split(";")
        if number == int(find[0]):
            aux.append(find[1])
        else:
            continue
    if moment not in aux:
        nome = ler(2)
        for idx in nome:
            find = idx.split(";")
            if number == int(find[2]):
                nome = [find[0], find[1]]
                break
        if moment == "p":
            print(f"{nome[0]} {nome[1]}({number}) não tem nota registada para o Projeto (P).")
        elif moment == "t1":
            print(f"{nome[0]} {nome[1]}({number}) não tem nota registada para o Primeiro teste (T1).")
        elif moment == "t2":
            print(f"{nome[0]} {nome[1]}({number}) não tem nota registada para o Segundo teste (T2).")
        sleep(2)
        return None
    else:
        valor = float(input("Nota: "))
        while valor < 0 or valor > 20:
            valor = float(input("A nota deve ser entre 0 e 20.\n"
                                "Nota: "))
        lista_auxiliar3.append(number)
        lista_auxiliar3.append(moment)
        lista_auxiliar3.append(valor)

def gravar():
    if len(lista_auxiliar) == 0 and len(lista_auxiliar2) == 0 and len(lista_auxiliar3) == 0:
        print("Sem valores para serem guardados")
    if len(lista_auxiliar) != 0:
        try:
            file = open(alunos, "a")
        except:
            print(f"Não foi possível abrir o arquivo: {alunos}")
        else:
            file.write(f"{lista_auxiliar[0]};{lista_auxiliar[1]};{lista_auxiliar[2]}\n")
        finally:
            lista_auxiliar.clear()
            file.close()
    if len(lista_auxiliar2) != 0:
        try:
            file = open("notas.txt", "a")
        except:
            print("Não foi possível abrir o arquivo")
        else:
            file.write(f"{lista_auxiliar2[0]};{lista_auxiliar2[1]};{lista_auxiliar2[2]}\n")
        finally:
            lista_auxiliar2.clear()
            file.close()

    if len(lista_auxiliar3) != 0:
        try:
            file = open(notas, "r")
            fileaux = open(temp, "w+")
        except Exception as g:
            print(g)
        else:
            line = file.readlines()
            fileaux.write("")
            fileaux = open(temp, "a")
            for idx in line:
                find = idx.split(";")
                if int(find[0]) == int(lista_auxiliar3[0]) and find[1] == lista_auxiliar3[1]:
                    fileaux.write(f"{lista_auxiliar3[0]};{lista_auxiliar3[1]};{lista_auxiliar3[2]}\n")
                else:
                    fileaux.write(f"{find[0]};{find[1]};{find[2]}")
            file = open(notas, "w+")
            file.write("")
            file = open(notas, "a")
            fileaux = open(temp, "r")
            line = fileaux.readlines()
            for idx in line:
                find = idx.split(";")
                file.write(f"{find[0]};{find[1]};{find[2]}")
            fileaux = open(temp, "w+")
            fileaux.write("")
        finally:
            lista_auxiliar3.clear()
            file.close()
            fileaux.close()

def ler(x=1):
    try:
        file = open(alunos, "r+")
        fileaux = open(notas, "r+")
    except Exception as g:
        print(g)
    else:
        if x == 1:
            linhas = file.readlines()
            linhas2 = fileaux.readlines()
            for idx in linhas:
                find = idx.split(";")
                print(f"Nome: {find[0]} {find[1]}\nNúmero: {find[2]}", end="")
                for idx2 in linhas2:
                    findaux = idx2.split(";")
                    if int(findaux[0]) == int(findaux[2]):
                        print(f"{findaux[1].upper()}: {findaux[2]}", end="")
                    else:
                        pass
                print(end="\n")
        elif x == 2:
            return file.readlines()
        elif x == 3:
            return fileaux.readlines()
    finally:
        file.close()
        fileaux.close()

    