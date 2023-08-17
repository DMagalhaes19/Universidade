from lab1.vendedor import Vendedor
from lab1.cliente import Cliente
from lab1.item import Item
from lab1.fatura import Fatura


#public class Gestor extends Gestor
class Loja:
    def __init__(self,gestor):
        self.gestor= gestor
        self.vendedores = []
        self.cliente = []
        self.item = []
    
    def obter_gestor(self):
        return self.gestor
    
    def obter_Vendedores(self):
        return self.vendedores
    
    def obter_Clientes(self):
        for i in self.cliente:
            return i
    
    def obter_Items(self):
        for i in self.item:
            return i 
        
    def registar_gestor(self,nome,numero_de_funcionario):
        self.gestor.__init__(nome,numero_de_funcionario)
    
    # registar_vendedor(nome : str, numero_de_funcionario : str) -> None
    # Cria um novo objeto Vendedor, e regista-o na lista.
    def registar_vendedor(self,nome,numero_de_funcionario):
        Vendedor.__init__(nome,numero_de_funcionario)
        self.vendedor.append(Vendedor)
    
    # registar_cliente(nome : str, numero_de_cliente : str) -> None
    # Cria um novo objeto Cliente, e regista-o na lista.
    def registar_cliente(self,nome,numero_de_cliente):
        Cliente.__init__(nome,numero_de_cliente)
        self.Cliente.append(Cliente)

    # registar_item(nome : str) -> None
    # Cria um novo objeto Item, e regista-o na lista.
    def registar_item(self,nome):
        Item.__init__(nome)
        self.item.append(Item)
        
    # registar_fatura(numero_de_cliente : str, itens : list, numero_de_funcionario_do_vendedor : str, ano : int, mes : int, dia : int) -> None
    # Cria um novo objeto Fatura, com os objetos Cliente e Vendedor relativos aos números indicados, com um objeto Data com os parâmetros indicados, e regista-o na lista.
    
    def registar_fatura(numero_de_cliente,item,numero_de_funcionario,ano,mes,dia):
        Fatura.__init__(numero_de_cliente,item,numero_de_funcionario,ano,mes,dia)
        
    # obter_faturas_cliente(numero_de_cliente : str) -> list
    # Retorna a lista de objetos Fatura do cliente com o número indicado.
    def obter_faturas_cliente(self,numero_de_cliente):
        for i in self.clientes:
            if(i.numero == numero_de_cliente):
                return Cliente.obter_faturas()
            else:
                pass
        
# obter_faturas_vendedor(numero_de_funcionario : str) -> list
# Retorna a lista de objetos Fatura associados ao vendedor o número indicado.
    def obter_faturas_vendedor(self,numero_de_funcionario):
        for i in self.vendedor:
            if(i.numero == numero_de_funcionario):
                return Vendedor.obter_faturas()
            else:
                pass