class Item:
    def __init__(self,valor):
        self.valor = valor
        self.next = None
class ListaEncadeada:
    def __init__(self):
        self.head = None
        self.size = 0
        
    def is_empty(self):
        return self.head == None
    
    def insert_head(self,valor):
        novo_item = Item(valor)
        novo_item.next = self.head
        self.head = novo_item
        self.size += 1
        
    def insert_tail(self,valor):
        novo_item = Item(valor)
        if self.is_empty():
            self.head = novo_item 
        else:
            current = self.head
            while not current.next is None:
                current = current.next
            current.next = novo_item
            self.size += 1
    def remove_head(self):
        if self.is_empty():
            raise IndexError("A lista está vazia !!")  
        else: 
            valor = self.head.valor
            self.head = self.head.next
            self.size -= 1
        return valor   
    def remove_tail(self):
        if self.is_empty():
            raise IndexError("A lista está vazia !!")
        elif self.head.next is None:
            valor = self.head.valor
            self.head = None
            self.size -= 1
        else:
            current = self.head
            prev = None
            while not current.next is None:
                prev = current
                current = current.next
            valor = current.valor
            prev.next = None
            self.size -= 1
        return valor    
    
    def get_list(self):
        mostrar = []
        while not self.is_empty():  
            valor = self.remove_head()
            mostrar.append(valor)
        return mostrar 
    
    def get_head(self):
        return self.head.valor
    
    def get_tail(self):
        current = self.head
        prev = None
        while not current.next is None:
            prev = current
            current = current.next
        return current.valor
    
    def get_size(self):
        return self.size
    
lista = ListaEncadeada()
lista.insert_head(77)
lista.insert_tail(88)
lista.insert_tail(99)
print("size: ", lista.get_size())
print("head: ",lista.get_head())         
print("Final: ",lista.get_tail())
print("Remove fim: ",lista.remove_tail())
print("Remove head: ",lista.remove_head())
print(lista.is_empty())
print("Lista: ")
print(lista.get_list())                   
print(lista.is_empty())