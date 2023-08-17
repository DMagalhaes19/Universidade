from aed_ds.dictionaries.open_hash_table import OpenHashTable

class family:
    def __init__(self,family_id:int,family_name:str):
        self.Family_id = family_id
        self.family_name = family_name
        self.client = OpenHashTable(5)    
    
    def get_ID(self):
        return self.Family_id

    def get_name(self):
        return self.family_name

    def get_client_id(self):
        return self.Client_ID 

    