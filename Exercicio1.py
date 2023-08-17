def implica(p1,p2): # exercicio 1
    result = 0
    if p1 == False: #percorrer a tabela de verdade do P
        result = True
    elif p2 == False:
        result = False
    else:
        result = True
    return result#s implica t e (u ou t ou nao s) = s implica t
