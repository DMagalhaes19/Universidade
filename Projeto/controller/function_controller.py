import json

def Data():
    with open(arq, encoding="utf-8") as file:
        global data
        a = json.load(file)
        data = a.copy()

def VerifArq(nome):
    global arq
    try:
        arq = nome
        with open(nome, "r") as file:
            data = json.load(file)
    except:
        return False
    else:
        return True

def CriarArq(nome):
    with open(nome, "w", encoding='utf8') as file:
        a = {"Jogo": {"Jogador": {}, "Jogo em curso": [0]}}
        json.dump(a, file)

def Gravar(arquivo):
    try:
        with open(arquivo, "w", encoding="UTF-8") as file:
            json.dump(data, file, ensure_ascii=False, indent=2)
    except:
        print("Ocorreu um erro na gravação.")
    else:
        print("Jogo gravado.")

def Victory(m, vit):
    n = []
    m_index = [[x, y] for x in range(0, len(m[0])) for y in range(0, len(m))]
    check = [[lambda x, y, k: [x, y + k],
             lambda x, y, k: [x, y - k]],
             [lambda x, y, k: [x + k, y],
             lambda x, y, k: [x - k, y]],
             [lambda x, y, k: [x + k, y - k],
             lambda x, y, k: [x - k, y + k]],
             [lambda x, y, k: [x + k, y + k],
             lambda x, y, k: [x - k, y - k]]
             ]
    for coordinate in m_index:
        for line in check:
            for v1 in range(1, vit+1):
                location = line[0](coordinate[0], coordinate[1], v1)
                if location[0] >= 0 and location[1] >= 0:
                    try:
                        test = m[location[1]][location[0]]
                    except:
                        pass
                    else:
                        n.append(location)
            n.reverse()
            n.append(coordinate)
            for v1 in range(1, vit + 1):
                location = line[1](coordinate[0], coordinate[1], v1)
                if location[0] >= 0 and location[1] >= 0:
                    try:
                        test = m[location[1]][location[0]]
                    except:
                        pass
                    else:
                        n.append(location)
            combo = 1
            streak = []
            for index in range(1, len(n) + 1):
                try:
                    if m[n[index][1]][n[index][0]] == m[n[index + 1][1]][n[index + 1][0]] and isinstance(m[n[index][1]][n[index][0]], str) == True and isinstance(m[n[index + 1][1]][n[index + 1][0]], str) == True:
                        combo += 1
                    else:
                        streak.append(combo)
                        combo = 1
                except:
                    streak.append(combo)
                    break
            if max(streak) >= vit:
                return True
            n.clear()

def RJ(nome):
    Jogador = data["Jogo"]["Jogador"]
    if nome in Jogador:
        print("Jogador existente.")
    else:
        Jogador[nome] = {"jogos": 0, "vitorias": 0}
        print("Jogador registado com sucesso.")

def EJ(nome):
    Jogador = data["Jogo"]["Jogador"]
    jogo = data["Jogo"]["Jogo em curso"]
    if nome in Jogador and nome not in jogo:
        try:
            del Jogador[nome]
        except:
            pass
        else:
            print("Jogador removido com sucesso.")
    elif nome not in Jogador:
        print("Jogador não existente.")
    elif nome in jogo:
        print("Jogador participa no jogo em curso.")

def LJ():
    Jogador = data["Jogo"]["Jogador"]
    J = [jogador for jogador in Jogador]
    J.sort()
    if len(J) != 0:
        print("\n".join(f"{nome.capitalize()} {Jogador[nome]['jogos']} {Jogador[nome]['vitorias']}" for nome in J))
    else:
        print("Não existem jogadores registados.")

def IJ(Nome1, Nome2, Comprimento, Altura, TamanhoSequência, TamanhoPeça):
    Jogadores = data["Jogo"]["Jogador"]
    Jogo = data["Jogo"]["Jogo em curso"]
    if Jogo[0] == 1:
        print("Existe um jogo em curso.")
        return None
    elif Nome1 not in Jogadores or Nome2 not in Jogadores:
        print("Jogador não registado.")
        return None
    elif Altura not in range(int(Comprimento/2), Comprimento+1):
        print("Dimensões da grelha inválidas.")
        return None
    elif len(TamanhoPeça) != 0 and max(TamanhoPeça) >= TamanhoSequência:
        print("Dimensões de peças especiais inválidas.")
        return None
    else:
        data["Jogo"]["vitoria"] = int(TamanhoSequência)
        m = [[0 for _ in range(0, Comprimento)] for _ in range(0, Altura)]
        Jogo[0] += 1
        TamanhoPeça2 = TamanhoPeça[:]
        Jogo.extend([Nome1, Nome2, Comprimento, Altura, TamanhoPeça, TamanhoPeça2, m])
        print(f"Jogo iniciado entre {Nome1.capitalize()} e {Nome2.capitalize()}.")

def DJ():
    jogo = data["Jogo"]["Jogo em curso"]
    if jogo[0] == 0:
        print("Não existe jogo em curso.")
    else:
        t1 = reversed(list(set(jogo[5])))
        t2 = reversed(list(set(jogo[6])))
        print(f"{jogo[3]} {jogo[4]}\n{jogo[1].capitalize()}")
        try:
            for peça in t1:
                print(f"{peça} {jogo[5].count(peça)}")
        except:
            print("Sem peças especiais.")
        print(f"{jogo[2].capitalize()}")
        try:
            for peça in t2:
                print(f"{peça} {jogo[6].count(peça)}")
        except:
            print("Sem peças especiais.")

def D(F):
    jogadores = data["Jogo"]["Jogador"]
    for jogador in F:
        if jogador not in jogadores:
            print("Jogador não registado.")
            return None
    if data["Jogo"]["Jogo em curso"][0] == 0:
        print("Não existe jogo em curso.")
        return None
    for jogador in F:
        if jogador not in data["Jogo"]["Jogo em curso"]:
            print("Jogador não participa no jogo em curso.")
            return None
    p1 = data["Jogo"]["Jogo em curso"][1]
    p2 = data["Jogo"]["Jogo em curso"][2]
    data["Jogo"]["Jogo em curso"] = [0]
    del data["Jogo"]["vitoria"]
    if p1 in F and p2 not in F:
        data["Jogo"]["Jogador"][p2]["vitorias"] += 1
    elif p2 in F and p1 not in F:
        data["Jogo"]["Jogador"][p1]["vitorias"] += 1
    data["Jogo"]["Jogador"][p2]["jogos"] += 1
    data["Jogo"]["Jogador"][p1]["jogos"] += 1
    print(f"Desistência com sucesso. Jogo terminado.")

def CP(Nome, TamanhoPeça, Posição, Sentido=None):
    Posição = int(Posição) - 1
    if data['Jogo']['Jogo em curso'][0] == 0:
        print("Não existe jogo em curso.")
        return None
    elif Nome not in data['Jogo']['Jogo em curso']:
        print("Jogador não participa no jogo em curso.")
        return None
    elif int(TamanhoPeça) not in data['Jogo']['Jogo em curso'][data['Jogo']['Jogo em curso'].index(Nome)+4] and int(TamanhoPeça) != 1:
        print("Tamanho de peça não disponível.")
        return None
    elif int(TamanhoPeça) == 0:
        print("Tamanho de peça não disponível.")
        return None
    elif int(Posição) < 0:
        print("Posição irregular.")
        return None
    elif int(TamanhoPeça) > 1 and Sentido == None:
        print("Indique um sentido para a peça.")
        return None
    elif Sentido not in [None, "e", "d"]:
        print("Sentido inválido.")
        return None
    width = data["Jogo"]["Jogo em curso"][7][0][:]
    matriz = data["Jogo"]["Jogo em curso"][7]
    if int(TamanhoPeça) >= len(width):
        print("Posição irregular.")
        return None

    if Sentido == "e" and int(TamanhoPeça) > 1:
        for v in range(0, int(TamanhoPeça)):
            loop = True
            try:
                test = width[int(Posição) - v]
            except:
                print("Posição irregular.")
                return None
            else:
                move = 0
                if move == 0 and type(matriz[move][int(Posição) - v]) == str:
                    print("Posição indisponível.")
                    return None
                while loop == True:
                    try:
                        if matriz[move + 1][int(Posição) - v] == 0:
                            move += 1
                            continue
                        else:
                            matriz[move][int(Posição) - v] = Nome
                            loop = False
                    except:
                        matriz[move][int(Posição) - v] = Nome
                        loop = False

    elif Sentido == "d" and int(TamanhoPeça) > 1:
        for v in range(0, int(TamanhoPeça)):
            loop = True
            try:
                test = width[int(Posição) + v]
            except:
                print("Posição irregular.")
                return None
            else:
                move = 0
                while loop == True:
                    try:
                        if matriz[move + 1][int(Posição) + v] == 0:
                            move += 1
                            continue
                        else:
                            matriz[move][int(Posição) + v] = Nome
                            loop = False
                    except:
                        matriz[move][int(Posição) + v] = Nome
                        loop = False

    elif int(TamanhoPeça) == 1:
        move = 0
        loop = True
        while loop == True:
            try:
                if matriz[move + 1][int(Posição)] == 0:
                    move += 1
                    continue
                else:
                    matriz[move][int(Posição)] = "a" if data["Jogo"]["Jogo em curso"][1] == Nome else "b"
                    loop = False
            except:
                matriz[move][int(Posição)] = Nome
                loop = False
    if int(TamanhoPeça) != 1:
        (data["Jogo"]["Jogo em curso"][data["Jogo"]["Jogo em curso"].index(Nome) + 4]).remove(int(TamanhoPeça))

    i = Victory(matriz, data["Jogo"]["vitoria"])
    if i == True:
        print("Sequência conseguida. Jogo terminado.")
        p1 = data["Jogo"]["Jogo em curso"][1]
        p2 = data["Jogo"]["Jogo em curso"][2]
        data["Jogo"]["Jogo em curso"] = [0]
        del data["Jogo"]["vitoria"]
        if Nome == p1:
            data["Jogo"]["Jogador"][p1]["vitorias"] += 1
        elif Nome == p2:
            data["Jogo"]["Jogador"][p2]["vitorias"] += 1
        data["Jogo"]["Jogador"][p2]["jogos"] += 1
        data["Jogo"]["Jogador"][p1]["jogos"] += 1
    else:
        print("Peça colocada.")

def V():
    if data["Jogo"]["Jogo em curso"][0] == 0:
        print("Não existe jogo em curso.")
    else:
        matriz = data["Jogo"]["Jogo em curso"][7]
        w = data["Jogo"]["Jogo em curso"][3]
        h = data["Jogo"]["Jogo em curso"][4]
        for alt in range(0, h):
            for comp in range(0, w):
                if type(matriz[alt][comp]) == str:
                    print(alt + 1, comp + 1, matriz[alt][comp].capitalize())
                else:
                    print(alt + 1, comp + 1, "Vazio")

def L(arquivo):
   try:
       with open(arquivo, encoding="utf-8") as file:
           data = json.load(file)
   except:
        print("Ocorreu um erro no carregamento.")
   else:
       print("Jogo carregado.")
