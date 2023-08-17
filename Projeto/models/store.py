from models.client import client
from models.family import family
from models.plan import plan
from models.series import series
from models.rent import rent
from aed_ds.dictionaries.open_hash_table import OpenHashTable

class store:
    def __init__(self):
        self.client = OpenHashTable(1000)
        self.series = OpenHashTable(1000)
        self.family = OpenHashTable(1000)
        self.rent = OpenHashTable(1000)
        self.standard = plan("Standard",4)
        self.premium = plan("Premium",7)
        self.pack_family = plan("Pack",4)
        self.cancelado = plan("Cancelado",0)
        self.client_id = 0
        self.family_id = 0
        self.series_id = 0
            
####################################################### Client #############################################################################
    def Insert_Client(self,cliente:str,plan:str)->int:
        id = 1
        self.client_id = id + self.client.size()
        self.client.insert_cliente(self.client_id,client(self.client_id,plan,cliente,None))
        return self.client_id

    def has_client_name(self,nome)->bool:
        return self.client.has_client_plan(nome,self.cancelado.get_name())
    
    def has_client(self,ID_client)->bool:
        return self.client.has_client_ID(int(ID_client))

    def change_plan(self,ID_client,plan)->None:
        new_plan = self.NewPlan(plan)
        self.client.update_plan(int(ID_client),new_plan)
    
    def Remove_client(self,ID_client)->None:
        if self.client.check_family_id_client(int(ID_client)):
            self.family.Desassociate_Family_client_ID(int(ID_client))
        else:
            self.client.Desassociate_Family_client(int(ID_client))
    
    def has_clients(self):
        return self.client.size() == 0

    def List_Clients(self):
        lista = self.series.list_clients()
        return self.series.__build_string(lista,lista)

####################################################### Plano #############################################################################    
    def change_plan_cancel(self,id_client)->None:
        if self.client.check_family_id_client(int(id_client)):
            self.family.update_plan_cancel(int(id_client),self.cancelado)
        else:
            self.client.update_plan(int(id_client),self.cancelado)

    def check_plan(self,plan)->bool:
        if plan == self.standard.get_name().lower() or plan == self.premium.get_name().lower() or plan == self.cancelado.get_name().lower():
            return False
        else:
            return True
    
    def NewPlan(self,plan:object)->object:
        if plan == self.standard.get_name().lower():
            plano = self.standard
            return plano
        elif plan == self.premium.get_name().lower():
            plano = self.premium
            return plano
    
####################################################### Family #############################################################################
    
    def Insert_Family(self,family_name)->int:
        id = 1
        self.family_id = id + self.family.size()
        self.family.insert_family(self.family_id,family(self.family_id,family_name))
        return self.family_id
    
    def has_family(self,name)->bool:
        return self.family.has_family_plan(name)
    
    def Family_client(self,ID_client)->bool:
        return self.client.check_family_id_client(int(ID_client))
    
    def Associate_Family_Client(self,ID_family,id_client)->None:
        cliente = self.client.get_all(int(id_client),int(ID_family))
        self.family.Associate(int(ID_family),cliente)

####################################################### Series #############################################################################
    def Insert_Series(self,series_name,Num_seasons=None,num_episode=None,episode_name=None)->int:
        id = 1
        self.series_id = id + self.series.size()
        self.series.insert_series(self.series_id,series(self.series_id,series_name,Num_seasons,num_episode,episode_name))
        return self.series_id            

    def has_series(self,series_name)->bool:
        return self.series.has_series_name(series_name)

    def register_series_episode(self,ID_Series,Num_seasons,num_episode,episode_name)->None:
        self.series.update_series_episode(int(ID_Series),Num_seasons,num_episode,episode_name)
    
    def has_episode(self,id,season,num_episode)->bool:
        return self.series.has_episode(int(id),season,num_episode)        

    def has_episode_number(self,id,num_season,num_episode)->bool:
        return self.series.check_episode_number(int(id),num_season,num_episode)

    def has_series_ID(self,ID_series)->bool:
        return self.series.has_series_id(int(ID_series))

    def has_season(self,num_season)->bool:
        return self.series.has_season(num_season)
    
    def Remove_Series(self,ID_series,num_season,num_episode):
        if num_season is None:
            self.series.remove_Series(ID_series)
        elif num_episode is None:
            self.series.remove_Season(ID_series,num_season)
        else:
            self.series.remove_episode(ID_series,num_season,num_episode)
    
    def has_episode_check(self,id,season,num_episode)->bool:
        return self.series.has_episode(int(id),season,num_episode)
####################################################### Rent #############################################################################
    def Rent_Series(self,ID_client,ID_series,num_season,num_episode):
        if num_episode == None:
            if self.series.get_season_status(int(ID_series),num_season):
                self.rent.rent_season(int(ID_client),rent(ID_client,ID_series,num_season,None))
                self.series.change_season_status(int(ID_series),num_season)
            else:
                return
        else:
            if self.series.get_episode_status(int(ID_series),num_season,num_episode):
                self.rent.rent_episode(int(ID_client),int(ID_series),num_season,num_episode,rent(ID_client,ID_series,num_season,num_episode))
                self.series.change_episode_status(int(ID_series),num_season,num_episode)
            else:
                return
    
    def has_rent_series(self,ID_series):
        return self.series.get_series_status(int(ID_series))

    def has_rent_episode(self,episode):
        pass