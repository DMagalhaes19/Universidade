class client():
    def __init__(self,id:int,plan:object,nome:str,family):
        self.plano = plan
        self.client_name = nome
        self.client_id = id
        self.family = family
    
    def get_name(self):
        return self.client_name
    
    def get_ID(self):
        return self.client_id
    
    def get_plan(self):
        return self.plano
    
    def get_family(self):
        return self.family

    def set_plan(self,plan)->None:
        self.plano = plan
    
    def set_family(self,family):
        self.family = family
    
    def remove(self):
        self.plano = None
        self.client_name = None
        self.client_id = None
        self.family = None

    def __le__(self, other: object) -> bool:
        if isinstance(other, client):
            return self.plan <= other.plan
        return False