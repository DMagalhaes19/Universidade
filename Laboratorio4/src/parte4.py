# -*- coding: utf-8 -*-

import random
stock = "stock.csv"

Stock_dicionario =[]

def ler_stocks():
    File = open(stock,"r",encoding='utf-8')
    data = File.readlines()
    for idx in data:
        idx = idx.split(";")
        dicionario={"produtos":
                    [
                        {
                         "nome":idx[0],
                         "quantidade":idx[1],
                         "preco_unitario":idx[2]
                        }
                ],
                    "total": 0
            }        
        Stock_dicionario.append(dicionario)
    return Stock_dicionario
    

def gerar_cestos(min_produtos,max_produtos):
    stock=Stock_dicionario
    aux = []
    Total =0
    qtd = random.randint(min_produtos,max_produtos)
    rdm_idx = random.sample(range(0,len(stock)),qtd)
    for idx in rdm_idx:
        product = stock[idx]
        product = product.split(";")
        Total +=float(stock[2])
        dicionario={
            "nome": product[0],
            "quantidade": random.randint(min_produtos, max_produtos),
            "preco_unitario": product[2]
        }
        aux.append(dicionario)
    cesto={
        "produto":aux,
        "total":round(Total,2)
        }
    return cesto

def atualizar_cesto(stock,cestos):
    stock = Stock_dicionario
    
    
    
print(ler_stocks())
print(gerar_cestos(0, 10))
