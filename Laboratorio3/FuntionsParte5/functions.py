def Menu():
    print("*--------------------*")
    print("Consultar Series")
    print("*--------------------*")
    print("LS. Listar Series")
    print("LT. Listar Series em intervalos de anos")
    print("LR. Listar por Ranking")
    print("LG. Listar por genero e ranking minimo")
    print("E. Sair")
    opc= str(input("Indique a sua opção->"))
    return opc.upper()

def listar_serie(arq):
    aux = []
    num = 0
    try:
        file = open(arq, "r+")
    except Exception as g:
        print(g)
    else:
        lines= file.readlines()
        for idx in lines:
            idx = idx.split(";")
            if idx[0] == "SÃ©rie":
                pass
            else:
                aux.append(idx[0])
        aux.sort()
        for idx in aux:
            num += 1
            print(f"{num}. {idx}", end="\n")
    finally:
        file.close()

def listar_ano(arq):
    aux = []
    ano0 = int(input("Ano inicial: "))
    while ano0 < 1990:
        ano0 = int(input("O ano mínimo é 1990: "))
    ano1 = int(input("Ano Final: "))
    while ano1 > 2019:
        ano1 = int(input("O ano máximo é 1990: "))
    try:
        file = open(arq, "r+")
    except Exception as error:
        print(error)
    else:
        line = file.readlines()
        for idx in line:
            find = idx.split(";")
            if find[1] == "Ano":
                pass
            else:

                if find[2] == "Ano":
                    pass
                else:
                    if int(find[2]) <= ano1 and int(find[2]) >= ano0:
                        aux.append(find[0])
                        aux.append(int(find[2]))
                        print(f"{find[2]} - {find[0]}")
                    else:
                        pass
    finally:
        file.close()

def listar_ranking(arq):
    num = 0
    rm = float(input("Ranking mínimo: "))
    try:
        file = open(arq, "r+")
    except Exception as error:
        print(error)
    else:
        line = file.readlines()
        for idx in line:
            find = idx.split(";")
            if find[2] == "Ano":
                pass
            else:
                if float(find[3]) >= rm:
                    num += 1
                    print(f"{num}. {find[0]} - {find[3]}", end="")
                else:
                    pass
        print(end="\n")
    finally:
        file.close()
    
def listar_genero(arq):
    gen = ["drama", "crime", "comédia", "comedia", "biografia", "ação", "açao", "animação", "animaçao"]
    num = 0
    rm = float(input("Ranking mínimo: "))
    g = input("Género: ").lower()
    while g not in gen:
        g = input("Género: ").lower()
        if g == "":
            return None
    try:
        file = open(arq, "r+")
    except Exception as error:
        print(error)
    else:
        line = file.readlines()
        for idx in line:
            find = idx.split(";")
            if find[1].lower() == g and float(find[3]) >= rm:
                num += 1
                print(f"{num}. {find[0]} - {find[3]}", end="")
            else:
                pass
        print(end="\n")

    finally:
        file.close()
