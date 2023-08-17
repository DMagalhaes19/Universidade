class client_aux:

    def __init__(self,plan:str,name:str):
        self.plan = plan
        self.name = name

    def get_name(self):
        return self.name
    
    def get_plan(self):
        return self.plan
    
    def __le__(self, other: object) -> bool:
        if isinstance(other, client_aux):
            return self.plan <= other.plan
        return False