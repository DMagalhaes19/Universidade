class Cliente:
    def __init__(self,numero,faturas):
        self.numero = numero
        self.faturas = faturas
        
    def obter_numero(self):
        return self.numero
    
    def obter_faturas(self):
        List = []
        List.append(self.faturas)
        return List