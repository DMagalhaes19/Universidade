from lab1.vendedor import Vendedor
from lab1.cliente import Cliente
from lab1.item import Item
from lab1.fatura import Fatura
from lab1.data import Data
from lab1.gestor import Gestor

#public class Gestor extends Gestor
class Loja:
    def __init__(self,gestor):
        self.gestor= gestor
        self.vendedores = []
        self.cliente = []
        self.item = []
        self.fatura= []
    
    def obter_gestor(self):
        return self.gestor
    
    def obter_vendedores(self):
        return self.vendedores
    
    def obter_clientes(self):
        return self.cliente
    
    def obter_itens(self):
        return self.item
        
    def registar_gestor(self,nome,numero_de_funcionario):
        self.gestor = Gestor(nome,numero_de_funcionario)
    
    # registar_vendedor(nome : str, numero_de_funcionario : str) -> None
    # Cria um novo objeto Vendedor, e regista-o na lista.
    def registar_vendedor(self,nome,numero_de_funcionario):
        self.vendedores.append(Vendedor(nome,numero_de_funcionario))
    
    # registar_cliente(nome : str, numero_de_cliente : str) -> None
    # Cria um novo objeto Cliente, e regista-o na lista.
    def registar_cliente(self,nome,numero_de_cliente):
        self.cliente.append(Cliente(nome,numero_de_cliente))
        

    # registar_item(nome : str) -> None
    # Cria um novo objeto Item, e regista-o na lista.
    def registar_item(self,nome):
        self.item.append(Item(nome))
        
        
    # registar_fatura(numero_de_cliente : str, itens : list, numero_de_funcionario_do_vendedor : str, ano : int, mes : int, dia : int) -> None
    # Cria um novo objeto Fatura, com os objetos Cliente e Vendedor relativos aos números indicados, com um objeto Data com os parâmetros indicados, e regista-o na lista.
    
    def registar_fatura(self,numero_de_cliente,item,numero_de_funcionario,ano,mes,dia):
        for num_cliente in self.cliente:
            if(num_cliente.numero == numero_de_cliente):
                aux_cliente = num_cliente
            else:
                pass
            
        for num_funcionario in self.vendedores:
            if(num_funcionario.numero == numero_de_funcionario):
                aux_func = num_funcionario
            else:
                pass
            
        registo= Fatura(numero_de_funcionario,Data(ano,mes,dia),aux_cliente,aux_func,item)
        num_cliente.faturas.append(registo)
        num_funcionario.faturas.append(registo)
        
    # obter_faturas_cliente(numero_de_cliente : str) -> list
    # Retorna a lista de objetos Fatura do cliente com o número indicado.
    def obter_faturas_cliente(self,numero_de_cliente):
        for i in self.cliente:
            if(i.numero == numero_de_cliente):
                return i.faturas

        
# obter_faturas_vendedor(numero_de_funcionario : str) -> list
# Retorna a lista de objetos Fatura associados ao vendedor o número indicado.
    def obter_faturas_vendedor(self,numero_de_funcionario):
        for i in self.vendedores:
            if(i.numero == numero_de_funcionario):
                return i.faturas