from models.date import data
from models.store import store

date = data(None)
loja = store()

def DD(current_date):
    if date.has_data():
        if date.dataHigher(int(current_date)):
            print("Data indicada é anterior à data atual.")
        else:
            date.set_data(int(current_date))
            print("Data alterada.")
    else:
        date.set_data(int(current_date))
        print("Data alterada.")

def RC(plano,name):
    if date.check_data():
        print("Sem data definida.")
    elif loja.has_client_name(name):
        print("Cliente existente.")
    elif loja.check_plan(plano):
        print("Plano inexistente.")
    else:
        id = loja.Insert_Client(name,plano)
        print(f"Cliente registado com identificador {id}.")

def RP(family_name):
    if date.check_data():
        print("Sem data definida.")
    elif loja.has_family(family_name):
        print("Família existente.")
    else:
        id = loja.Insert_Family(family_name)
        print(f"Família registada com identificador {id}.")

def RS(series_name):
    if loja.has_series(series_name):
        print("Série existente.")
    else:
        id = loja.Insert_Series(series_name)
        print(f"Série registada com o identificador {id}.")

def RE(ID_Series,Num_seasons,num_episode,episode_name):
    if loja.has_series_ID(ID_Series):
        print("Série inexistente.")
    elif loja.has_episode(ID_Series,Num_seasons,num_episode):
        print("Episódio existente.")
    else:
        loja.register_series_episode(ID_Series,Num_seasons,num_episode,episode_name)
        print("Registo efetuado com sucesso.")

def AP(ID_client,plan):
    if date.check_data():
        print("Sem data definida.")
    elif loja.has_client(ID_client):
        print("Cliente inexistente.")
    elif loja.Family_client(ID_client):
        print("Cliente associado a família.")
    else:
        loja.change_plan(ID_client,plan)
        print("Plano alterado com sucesso.")

def CP(ID_client):
    if loja.has_client(ID_client):
        print("Cliente inexistente.")
    else:
        loja.change_plan_cancel(ID_client)
        print("Plano cancelado com sucesso.")


def AF(ID_family,ID_client):
    if loja.has_family(ID_family):
        print("Família inexistente.")
    elif loja.has_client(ID_client):
        print("Cliente inexistente.")
    elif loja.Family_client(ID_client) == False:
        print("Cliente associado a outra família.")
    else:
        loja.Associate_Family_Client(ID_family,ID_client)
        print("Cliente associado com sucesso.")

def DF(ID_client):
    if loja.has_client(ID_client):
        print("Cliente inexistente.")
    elif loja.Family_client(ID_client):
        print("Cliente não associado a família.")
    else:
        loja.Remove_client(ID_client)
        print("Cliente desassociado com sucesso.")

def ES(ID_series,num_season = None,num_episode= None):
    if loja.has_series_ID(ID_series):
        print("Série inexistente.")
    elif loja.has_season(num_season):
        print("Temporada inexistente.")
    elif loja.has_episode_number(ID_series,num_season,num_episode):
        print("Episódio inexistente.")
    else:
        loja.Remove_Series(ID_series,num_season,num_episode)
        print("Conteúdo eliminado com sucesso.")

def EC(ID_client):
    if loja.has_client(ID_client):
        print("Cliente inexistente.")
    else:
        loja.Remove_client(ID_client)
        print("Cliente eliminado com sucesso.")

def LP():
    if loja.has_clients():
        print("Sem clientes registados.")
    else:
        loja.List_Clients()

def LF():
    if loja.has_family():
        print("Sem famílias registadas.")
    else:
        loja.List_Family()

def LS():
    if loja.has_series():
        print("Sem séries registadas.")
    else:
        loja.List_Series()

def LSA(ID_client):
    if date.check_data():
        print("Sem data definida.")
    elif loja.has_client(ID_client):
        print("Cliente inexistente.")
    elif loja.has_series():
        print("Sem episódios alugados.")
    else:
        loja.Client_Series(ID_client)

def LSAF(ID_Family):
    if date.check_data():
        print("Sem data definida.")
    elif loja.has_family(ID_Family):
        print("Família inexistente.")
    elif loja.has_series():
        print("Sem séries alugadas.")
    else:
        loja.Family_Series(ID_Family)

def AS(ID_client,ID_series,num_season,num_episode= None):
    if date.check_data():
        print("Sem data definida.")
    elif loja.has_client(ID_client):
        print("Cliente inexistente.")
    elif loja.has_series_ID(ID_series):
        print("Série inexistente.")
    elif loja.has_season(num_season):
        print("Temporada inexistente.")
    elif loja.has_episode_check(ID_series,num_season,num_episode):
        print("Episódio inexistente.")
    else:
        loja.Rent_Series(ID_client,ID_series,num_season,num_episode)
        print("Conteúdo alugado com sucesso.")

def CA(ID_client,ID_series,num_season = None,num_episode= None):
    if date.check_data():
        print("Sem data definida.")
    elif loja.has_client(ID_client):
        print("Cliente inexistente.")
    elif loja.has_rent_series(ID_series):
        print("Série sem aluguer registado.")
    elif loja.has_rent_season_episode(ID_series,num_season):
        print("Temporada sem aluguer registado.")
    elif loja.has_rent_episode(ID_series,num_season,num_episode):
        print("Episódio sem aluguer registado.")
    else:
        loja.cancel_rent(ID_client,ID_series,num_season,num_episode)
        print("Aluguer de conteúdo cancelado com sucesso.")