def resolve():
    #tabela de verdade de S-->T e (U ou T ou ~S)
    table_2 = [["u","t","s","s-->T","u V t V ~s","S"],["V","V","V","V","V","V"],["V","V","F","F","V","F"],["V","F","V","F","V","F"],["V","F","F","V","V","V"],["F","V","V","V","V","V"],["F","V","F","V","V","V"],["F","F","V","F","V","F"],["F","F","F","V","V","V"]]
    for i in range(len(table_2)):
        if i > 0:
            table_3 = table_2[i]
            print("|"+table_3[0], "|" + table_3[1],"|" + table_3[2],"|" + table_3[3],"    |" + table_3[4],"         |" + table_3[5]+"|")
        else:
            table_3 = table_2[i]
            print("|"+table_3[0], "|" + table_3[1],"|" + table_3[2],"|" + table_3[3],"|" + table_3[4],"|" + table_3[5]+"|")            
    print("\ncomo de cada vez que o s-->T é verdadeiro, a soluçao da resposta também é verdadeira, assim como quando é falso, podemos concluir que s-->T & u V t V ~s, é equivalente a apenas S--> T ")
    return table_2
