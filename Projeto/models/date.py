class data:    
    def __init__(self,data):
        self.date = data

    def set_data(self,date)->None:
        self.date = date
    
    def get_data(self)->object:
        return self.date
    
    def has_data(self)->bool:
        if self.date == None:
            return False
        else:
            return True
    
    def check_data(self)->bool:
        if self.date == None:
            return True
        else:
            return False
    
    def dataHigher(self,data):
        if self.date >= data:
            return True
        else:
            return False