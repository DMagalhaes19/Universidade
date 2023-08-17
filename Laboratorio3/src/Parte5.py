import FunctionsParte5.functions as func

arq = "series.txt"
if __name__ == '__main__':
    opc = func.menu()
    while opc != "E":
        if opc == "LS": 
            func.listar_serie(arq)
        elif opc == "LT":   
            func.listar_ano(arq)
        elif opc == "LR":   
            func.listar_ranking(arq)
        elif opc == "LG":   
            func.listar_genero(arq)
        elif opc == "E":    
            break
        else:
            print("opção inválida")