from Lab1.funcionario import Funcionario
class Gestor(Funcionario):
    
    def __init__(nome,numero):
        Funcionario.__init__(nome,numero) 
        # super().__init__(nome,numero)    