from datetime import datetime
from dateutil.relativedelta import relativedelta

read = []

def R(nome,nif,idade,escalao,saldo_disponivel):
    if(len(read) == 0):
        if(isinstance(nome, str) == True):
            if(int(saldo_disponivel) > 0):
                if(escalao.lower() == "normal" or escalao.lower() == "social b" or escalao.lower() == "social a" or escalao.lower() == "sub23"):
                    dicionario={
                                "nome":nome,
                                "nif":nif,
                                "idade": idade,
                                "escalao":escalao,
                                "saldo_disponivel":saldo_disponivel,
                                "passe": "",
                                "validade": ""
                            }
                    read.append(dicionario)
                    return dicionario
                else:
                    raise Exception("O escalao que introduziu nao existe, por favor introduza um escalao que exista!")
            else:
                raise Exception("Nao e possivel ter saldo negativo!")
        else:
            raise Exception("Introduza um nome valido!")
    else:
        for idx in range(len(read)):
            if(read[1] == nif):
                raise Exception("O cliente com esse nif: {} . Ja existe por favor introduza um novo nif!".format(nif))
            else:
                if(isinstance(nome, str) == True):
                   if(saldo_disponivel > 0):
                        if(escalao.lower() != "normal" or escalao.lower() != "social b" or escalao.lower() != "social a" or escalao.lower() != "sub23"):
                            dicionario={
                                "nome":nome,
                                "nif":nif,
                                "idade": idade,
                                "escalao":escalao,
                                "saldo_disponivel":saldo_disponivel,
                                "passe": "",
                                "validade": ""
                            }
                            read.append(dicionario)
                        else:
                            raise Exception("O escalao que introduziu nao existe, por favor introduza um escalao que exista!")
                   else:
                        raise Exception("Nao e possivel ter saldo negativo!")
                else:
                    raise Exception("Introduza um nome valido!")                

def EP(nif,tipoPasse):
    Pagamento= Mensal()
    for idx in read:
        if(idx["nif"] == nif):
            if(idx["escalao"] == "normal" or tipoPasse == "metropolitano" ):
                if(idx["saldo_disponivel"]>40):
                    idx["passe"] += tipoPasse
                    idx["validade"] += Pagamento
                    print("A sua mensalidade é: {} euros, a proxima mensalidade e no dia : {}".format(40,Pagamento))
                    break
                else:
                    print("Saldo insuficiente.")
                    break
            elif(idx["escalao"] == "social b" or tipoPasse == "metropolitano"):
                if(idx["saldo_disponivel"]>30):
                    idx["passe"] += tipoPasse
                    idx["validade"] += Pagamento
                    print("A sua mensalidade é: {} euros, a proxima mensalidade e no dia : {}".format(30,Pagamento))
                    break
                else:
                    print("Saldo insuficiente.")
                    break                    
            elif(idx["escalao"] == "social a" or tipoPasse == "metropolitano"):
                if(idx["saldo_disponivel"]>20):
                    idx["passe"] += tipoPasse
                    idx["validade"] += Pagamento
                    print("A sua mensalidade é: {} euros, a proxima mensalidade e no dia : {}".format(20,Pagamento))
                    break
                else:
                    print("Saldo insuficiente.")
                    break
            elif(idx["escalao"] == "sub23" or tipoPasse == "metropolitano"):
                if(idx["saldo_disponivel"]>20):
                    idx["passe"] += tipoPasse
                    idx["validade"] += Pagamento
                    print("A sua mensalidade é: {} euros, a proxima mensalidade e no dia : {}".format(20,Pagamento))
                    break
                else:
                    print("Saldo insuficiente.")
                    break
            elif(idx["escalao"] == "normal" or tipoPasse == "municipal"):
                if(idx["saldo_disponivel"]>30):
                    idx["passe"] += tipoPasse
                    idx["validade"] += Pagamento
                    print("A sua mensalidade é: {} euros, a proxima mensalidade e no dia : {}".format(30,Pagamento))
                    break
                else:
                    print("Saldo insuficiente.")
                    break
            elif(idx["escalao"] == "social b" or tipoPasse == "municipal"):
                if(idx["saldo_disponivel"]>22.5):
                    idx["passe"] += tipoPasse
                    idx["validade"] += Pagamento
                    print("A sua mensalidade é: {} euros, a proxima mensalidade e no dia : {}".format(22.5,Pagamento))
                    break
                else:
                    print("Saldo insuficiente.")
                    break
            elif(idx["escalao"] == "social a" or tipoPasse == "municipal"):
                if(idx["saldo_disponivel"]>15):
                    idx["passe"] += tipoPasse
                    idx["validade"] += Pagamento
                    print("A sua mensalidade é: {} euros, a proxima mensalidade e no dia : {}".format(15,Pagamento))
                    break
                else:
                    print("Saldo insuficiente.")
                    break
            elif(idx["escalao"] == "sub23" or tipoPasse == "municipal"):
                if(idx["saldo_disponivel"]>12):
                    idx["passe"] += tipoPasse
                    idx["validade"] += Pagamento
                    print("A sua mensalidade é: {} euros, a proxima mensalidade e no dia : {}".format(12,Pagamento))
                    break
                else:
                    print("Saldo insuficiente.")
                    break
            elif(tipoPasse == "-12" or idx["saldo_disponivel"]>0):
                if(idx["idade"]<= 12):
                    idx["validade"] += Pagamento
                    break
                else:
                    print("Não apresenta os requisitos necessários para adquirir este passe.")
                    break
            elif(tipoPasse == "+65" or idx["saldo_disponivel"]>20):
                if(idx["idade"] >= 65):
                    idx["passe"] += tipoPasse
                    idx["validade"] += Pagamento
                    print("A sua mensalidade é: {} euros , a proxima mensalidade e no dia : {}".format(20,Pagamento))
                    break
                else:
                    print("Não apresenta os requisitos necessários para adquirir este passe.")
                    break

def CV(nif):
    Mes = Hoje()
    for idx in read:
        if(idx["nif"] == nif):
            if(idx["validade"] < Mes):
                raise Exception("Data de validade expirada")
            

def G(ficheiro):
    with open(ficheiro, 'w') as f: 
        for idx in read:
            for chave, valor in idx.items(): 
                f.write('%s:%s\n' % (chave, valor))

def L(ficheiro):
    data = dict()
    with open(ficheiro) as raw_data: 
        for idx in raw_data: 
            if ':' in idx: 
                chave,valor = idx.split(':', 1) 
                data[chave]=valor
    print(data)


def Mensal():
    hoje = datetime.now()
    novaData = hoje + \
        relativedelta(months=1)
    return novaData.strftime("%x")
    
def Hoje():
    dia = datetime.now()
    return dia.strftime("%x")