from models.rent import rent
from models.rented import rented
from models.client_aux import client_aux
from aed_ds.dictionaries.adt_dictionary import Dictionary
from aed_ds.lists.singly_linked_list import SinglyLinkedList
from aed_ds.dictionaries.item import Item
from aed_ds.exceptions import EmptyListException,InvalidPositionException,NoSuchElementException,EmptyStackException,FullStackException,EmptyQueueException,FullQueueException,DuplicatedKeyException,EmptyDictionaryException,EmptyTreeException
import ctypes

class OpenHashTable(Dictionary,SinglyLinkedList):
    def __init__(self, size):
        self.quantity = size
        self.buckets = (self.quantity * ctypes.py_object)()
        for i in range(self.quantity):
            self.buckets[i] = SinglyLinkedList()
        self.lenght = 0
        

####################################################### OpenHashTable #############################################################################        
    def is_full(self) -> bool:
        for i in range(self.quantity):
            if self.buckets[i].is_empty():
                return False
        return True
        """Returns true if the dictionary is full.
        Throws NoSuchElementException"""

    def get(self, k: object) -> object:
        index=self.hash(k)
        it=self.buckets[index].iterator()
        while it.has_next():
            item=it.get_next()
            if item.get_key()==k:
                return item.get_value()
        raise NoSuchElementException()
        """Returns the value associated with key k.
            Throws NoSuchElementException"""

    def update(self, k: object, v: object) -> None:     
        i = 0
        index=self.hash(k)
        it=self.buckets[index].iterator()
        while it.has_next():
            item=it.get_next()
            if item.get_key()==k:
                self.buckets[index].remove(i)
                self.buckets[index].insert(Item(k,v),i)
                return
            i += 1
        raise NoSuchElementException()
        """Updates the value associated with key k.
        """"Throws NoSuchElementException"""
    
    def remove(self, k: object) -> object:  
        i = 0
        index=self.hash(k)
        it=self.buckets[index].iterator()
        while it.has_next():
            item=it.get_next()
            if item.get_key()==k:
                self.buckets[index].remove(i)
                return item.get_value()
            i +=1
            self.lenght -= 1
        raise NoSuchElementException()                
        """Removes the item with key k, and returns the value associated with it.
        Throws NoSuchElementException"""
        
    def keys(self)->list:        
        lista=SinglyLinkedList()
        for i in self.buckets:
            it=i.iterator()
            while it.has_next():
                item=it.get_next()
                lista.insert_last(item.get_key())
        return lista
        """Returns a List with all the keys in the dictionary."""
    
    def values(self) -> list:
        lista= SinglyLinkedList()
        for i in self.buckets:
            it=i.iterator()
            while it.has_next():
                item=it.get_next()
                lista.insert_last(item.get_value())
        return lista
        """Returns a List with all the values in the dictionary."""

    def items(self) -> list:
        lista = SinglyLinkedList()
        for i in self.buckets:
            it=i.iterator()
            while it.has_next():
                item=it.get_next()
                lista.insert_last(item)
        return lista
        """Returns a List with all the key value pairs in the dictionary."""
    def insert(self, k: object, v: object) -> None:                        
        index = self.hash(k)
        it = self.buckets[index].iterator()
        while it.has_next():
            item = it.get_next()
            if item.get_key() == k:
                raise DuplicatedKeyException
        item = Item(k,v)
        self.buckets[index].insert_last(item)
        self.lenght += 1            
        """Inserts a new value, associated with key k.
            Throws DuplicatedKeyException"""    

####################################################### Client #############################################################################
    def insert_cliente(self, k: object, v:object) -> None:                        
        index = self.hash(k)
        it = self.buckets[index].iterator()
        while it.has_next():
            cliente = it.get_next()
            if cliente.get_name() == v.get_name():
                raise DuplicatedKeyException
        self.buckets[index].insert_last(v)
        self.lenght += 1
        """Inserts a new value, associated with key k.
            Throws DuplicatedKeyException"""

    def has_client_ID(self,k)->bool:
        index = self.hash(k)
        it= self.buckets[index].iterator()
        while it.has_next():
            cliente = it.get_next()
            if cliente.get_ID() == k:
                return False
        return True

    def get_all(self,k,v)->object:
        index = self.hash(k)
        it = self.buckets[index].iterator()
        while it.has_next():
            cliente = it.get_next()
            cliente.set_family(v)
            return cliente
    
    def Desassociate_Family_client(self,k):
        index = self.hash(k)
        it = self.buckets[index].iterator()
        while it.has_next():
            cliente = it.get_next()
            cliente.remove()
            self.lenght-=1
            return
    
    def list_clients(self):
        lista = SinglyLinkedList()
        index = self.size()
        i = 0
        while i<= index:
            it = self.buckets[index].iterator()
            while it.has_next():
                cliente = it.get_next()
                if cliente.get_Family() == None:
                    client = client_aux(cliente.get_plan(),cliente.get_name())
                    lista.insert_last(client)
            i+=1
        return lista

    def __build_string(list : SinglyLinkedList, key : object)->object:
        Aux = str()
        it = list.iterator()
        while it.has_next():
            Aux += key(it.get_next())
            if it.has_next():
                Aux += '\n'
        return Aux
####################################################### Plan #############################################################################
    def has_client_plan(self, k: object,plano:object) -> bool:
        index = self.size()
        i = 0
        while i <= index:
            it = self.buckets[i].iterator()
            while it.has_next():
                cliente = it.get_next()
                if cliente.get_name() == k:
                    if cliente.get_plan() == plano:
                        return False
                    else:
                        return True
            i+=1
        return False
        """Returns the value associated with key k.
            Throws NoSuchElementException"""

    def update_plan(self,k:object,v:object)->None:
        index = self.hash(k)
        it = self.buckets[index].iterator()
        while it.has_next():
            cliente = it.get_next()
            cliente.set_plan(v)
            return

    def update_plan_cancel(self,k:object,v:object)->None:
        index = self.size()
        i = 0
        while i<= index:
            it = self.buckets[i].iterator()
            while it.has_next():
                familia = it.get_next()
                if familia.client.has_client_ID(k) == False:
                    familia.client.update_plan(k,v)
                    return 
            i+=1


    def has_family_plan(self, k: object) -> bool:
        index = self.size()
        i = 0
        while i <= index:
            it = self.buckets[i].iterator()
            while it.has_next():
                family = it.get_next()
                if family.get_name() == k:
                    return True
            i+=1
        return False

####################################################### Family #############################################################################
    def insert_family(self,k:object,v:object)->None:
        index = self.hash(k)
        it = self.buckets[index].iterator()
        while it.has_next():
            familia= it.get_next()
            if familia.get_nome() == v.get_name():
                raise DuplicatedKeyException
        self.buckets[index].insert_last(v)
        self.lenght += 1
        """Inserts a new value, associated with key k.
            Throws DuplicatedKeyException"""
    
    def check_family_id_client(self,k:object)->bool:
        index = self.hash(k)
        it = self.buckets[index].iterator()
        while it.has_next():
            cliente = it.get_next()
            if cliente.get_family() == None:
                return True
        return False


    def Associate(self,ID_family:int,v:object)->None:
        index= self.hash(ID_family)
        it = self.buckets[index].iterator()
        while it.has_next():
            family = it.get_next()
            family.client.insert_cliente(v.client_id,v)
            return

    def Desassociate_Family_client_ID(self,k)->None:
        index = self.size()
        i = 0
        while i <= index:
            it = self.buckets[i].iterator()
            while it.has_next():
                family = it.get_next()
                index2 = family.client.size()
                j = 0
                while j <= index2:
                    it2 = self.buckets[j].iterator()
                    while it2.has_next():
                        client = it2.get_next()
                        if client.get_ID() == k:
                            client.remove_client(k)
                    j+=1
            i+=1

####################################################### Series #############################################################################
    def has_series_name(self,k:object)->bool:
        index = self.size()
        i= 0
        while i<= index:
            it = self.buckets[i].iterator()
            while it.has_next():
                series = it.get_next()
                if series.get_series_name() == k:
                    return True
            i+=1
        return False
    
    def has_season(self,k:object)->bool:
        index = self.size()
        i = 0
        while i<= index:
            it = self.buckets[i].iterator()
            while it.has_next():
                series = it.get_next()
                if series.get_season() == k:
                    return False
            i+=1
        return True
    
    def check_episode_number(self,num_season,num_episode)->bool:
        index = self.size()
        i = 0
        while i <= index:
            it = self.buckets[i].iterator()
            while it.has_next():
                series = it.get_next()
                if series.get_season() == num_season:
                    if series.get_episode_number() == num_episode:
                        return False
                    else:
                        return True
            i+=1
    #Original
    def check_episode(self,id,num_season,num_episode)->bool:
        index = self.hash(id)
        it = self.buckets[index].iterator()
        while it.has_next():
            series = it.get_next()
            if series.get_season() == num_season:
                if series.get_episode_number() == num_episode:
                    return False
                else:
                    return True

    def update_series_episode(self,k,Num_seasons,num_episode,episode_name):
        index = self.hash(k)
        it = self.buckets[index].iterator()
        while it.has_next():
            series= it.get_next()
            series.set_series(Num_seasons,num_episode,episode_name)
            return 
            
    def insert_series(self,k:object,v:object)->None:                        
        index = self.hash(k)
        it = self.buckets[index].iterator()
        while it.has_next():
            series = it.get_next()
            if series.get_nome() == v.get_series_name():
                raise DuplicatedKeyException
        self.buckets[index].insert_last(v)
        self.lenght += 1
        """Inserts a new value, associated with key k.
            Throws DuplicatedKeyException"""        
    
    def has_series_id(self,k:object):
        if self.size() == 0:
            return True
        else:
            index = self.hash(k)
            it= self.buckets[index].iterator()
            while it.has_next():
                series = it.get_next()
                if series.get_ID() == k:
                    return False
            return True
    
    def remove_Series(self,k:object)->None:
        index = self.hash(k)
        it = self.buckets[index].iterator()
        while it.has_next():
            series = it.get_next()
            self.lenght -=1
        raise NoSuchElementException()

    def remove_Season(self,k:object,num_season:object):
        index = self.hash(k)
        it = self.buckets[index].iterator()
        while it.has_next():
            series = it.get_next()
            if series.get_season() == num_season:
                series.set_season()
                return 
        raise NoSuchElementException()
    
    def remove_episode(self,k,num_season,num_episode):
        index = self.hash(k)
        it = self.buckets[index].iterator()
        while it.has_next():
            series= it.get_next()
            series.remove_episode(k,num_season,num_episode)
            return
    
    def get_episode_status(self,id_series,num_season,num_episode):
        index = self.hash(id_series)
        it = self.buckets[index].iterator()
        while it.has_next():
            series= it.get_next()
            if series.get_season() == num_season:
                if series.get_episode_number() == num_episode:
                    if series.see_episode_status() == 0:
                        return True
                    else:
                        return False
    
    def get_season_status(self,ID_series,num_season):
        index = self.hash(ID_series)
        it = self.buckets[index].iterator()
        while it.has_next():
            series= it.get_next()
            if series.get_season() == num_season:
                if series.see_season_status() == 0:
                    return True
                else:
                    return False

    def change_season_status(self,ID_series,num_season):
        index = self.hash(ID_series)
        it = self.buckets[index].iterator()
        while it.has_next():
            series = it.get_next()
            if series.get_season() == num_season:
                series.change_season_status()
                return
    def change_episode_status(self,ID_series,num_season,num_episode):
        index = self.hash(ID_series)
        it = self.buckets[index].iterator()
        while it.has_next():
            series = it.get_next()
            if series.get_season() == num_season:
                series.change_episode_status()
                return
    
    #Alterada
    def has_episode(self,id,season,num_episode)->bool:
        index = self.hash(id)
        it = self.buckets[index].iterator()
        while it.has_next():
            series = it.get_next()
            if series.get_season() == season:
                if series.get_episode_number() == num_episode:
                    return True
                else: 
                    return False

####################################################### Rent #############################################################################
    def rent_episode(self,ID_client,ID_series,num_season,num_episode,v):
        index = self.hash(ID_client)
        it=  self.buckets[index].iterator()
        while it.has_next():
            rent = it.get_next()
            if rent.get_client() == ID_client:
                if rent.get_season() == ID_series:
                    if rent.get_num_season() == num_season:
                        if rent.get_num_episode() == num_episode:
                            return
        self.buckets[index].insert_last(v)
        self.lenght += 1

        
    def rent_season(self,ID_client,v):
        index = self.hash(ID_client)
        it = self.buckets[index].iterator()
        while it.has_next():
            rent = it.get_next()
            if rent.get_client() == ID_client:
                return
        self.buckets[index].insert_last(v)
        self.lenght += 1

    def get_series_status(self,k):
        index = self.hash(k)
        it = self.buckets[index].iterator()
        while it.has_next():
            series = it.get_next()
            if series.get_status() == 0:
                return True
            else:
                return False
            

####################################################### Global #############################################################################
    def size(self) -> int:
        return self.lenght
        """Returns the number of elements in the dictionary."""

    def hash(self,key):
        return key % self.quantity