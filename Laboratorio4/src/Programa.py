# -*- coding: utf-8 -*-
import passes as ps

if __name__ == "__main__": 
   while True:
        line = input()
        line= line.upper()
        if(line == "R"):
            Nome = print("Introduza o nome: ")
            Nif =  print("Introduza o seu nif: ")
            idade =  print("Introduza a sua idade: ")
            escalao = print("Introduza o seu escalao: ")
            saldo_disponivel = print("Introduza o seu saldo:")
            Regista=ps.R(Nome,Nif,idade,escalao,saldo_disponivel)
        elif(line == "EP"):
            Nif =  print("Introduza o seu nif: ")
            Passe =  print("Introduza o tipo de passe que pretende: ")
            Regista = ps.EP(Nif,Passe)
        elif(line == "CV"):
            Nif =  print("Introduza o seu nif: ")
            Regista = ps.CV(Nif)
            pass
        elif(line == "G"):
            Ficheiro =  print("Introduza o ficheiro onde pretende gravar a informação:")
            Regista = ps.G(Ficheiro)
            pass
        elif(line == "L"):
            Ficheiro =  print("Introduza o ficheiro de onde pretende ler a informação:")
            Regista = ps.L(Ficheiro)
            pass
        elif(line == "Q"):
            break
        else:
            print("Instrução inválida.")