nome = "nomes.csv"
lista_dicionario=[]

def ler_nomes():
    File= open(nome,"r",encoding='utf-8')
    data = File.readlines()
    for cnt in data:
        cnt = cnt.split(";")
        dicionario={"nome":cnt[0],
                     "registos":cnt[1],
                     "genero":cnt[2].replace("\n","")
                     }
        lista_dicionario.append(dicionario)      
    print(lista_dicionario)

def listar_Nomes(lista_dicionario):
    for dicionario in lista_dicionario:
        print(dicionario["nome"])
        
def listas_nomes_genero(gender):
    for dicionario in lista_dicionario:
        if(gender.upper().strip() == dicionario["genero"]):
            print(dicionario["nome"])
            
def listas_nomes_registo(min_registos):
    for dicionario in lista_dicionario:
        if(str(min_registos) >= dicionario["registos"]):
            print(dicionario["nome"])
        
ler_nomes()
listar_Nomes(lista_dicionario)
listas_nomes_genero("F")
listas_nomes_registo(1)        