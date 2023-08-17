# -*- coding: utf-8 -*-
import Functions.funcoes as func
import sys

alunos = "Alunos.txt"
notas = "Notas.txt"
temp = "temp.txt"


if __name__ == '__main__':
    if not func.verificarArq(alunos):
        func.criarArq(alunos)
    else:
        pass
    if not func.verificarArq(notas):
        func.criarArq(notas)
    else:
        pass
    if not func.verificarArq(temp):
        func.criarArq(temp)
    else:
        pass
    opc = func.Menu()
    while opc != "E":
        if(opc == "R"):
            func.register()
            sys.stdin.flush()
        elif(opc == "RM"):
            func.register_notes()
            sys.stdin.flush()
        elif(opc == "AM"):
            func.alterarNota()
            sys.stdin.flush()
        elif(opc == "G"):
            func.Gravar()
            sys.stdin.flush()
        elif(opc == "L"):
            func.ler()
            sys.stdin.flush()
        elif(opc == "E"):
            sys.stdin.flush()
            break
        else:
            print("opçao invalida")