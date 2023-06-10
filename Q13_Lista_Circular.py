class Item:
    def __init__(self,valor: object = None, prev: 'Item' = None, next: 'Item' = None):
        self.valor = valor
        self.next = next
        self.prev = next
    def __str__(self):
        return str(self.valor)    
        
class ListaCircular:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0
    def insert_head(self,valor):
        novo_item = Item(valor)
        if self.head is None:
            self.head = self.tail = novo_item
        else:
            novo_item.next = self.head
            self.head = novo_item
            novo_item.next.prev = novo_item
            self.head.prev = self.tail
            self.tail.next = self.head
        self.size += 1
        
    def inserir_tail(self,valor):
        novo = Item(valor)
        if self.head is None:
            self.head = self.tail = novo
        else:
            novo.prev = self.tail
            novo.prev.next = novo
            self.tail = novo
            self.tail.next = self.head
            self.head.prev = self.tail
        self.size += 1 
               
    def remove_head(self):
        if self.head is None:
            print("A lista está vazia !!")
            return
        if self.head == self.tail:
            self.head = self.tail = None
        else:
            carga =self.head.valor
            self.head = self.head.next
            self.head.prev = self.tail
            self.tail.next = self.head
        self.size -= 1
        return carga
        
    def remove_tail(self):
        if self.head is None:
            print("A lista está vazia !!")
            return
        if self.head == self.tail:
            self.head = self.tail = None
        else:
            carga = self.tail.valor
            self.tail = self.tail.prev
            self.tail.next = self.head
            self.head.prev = self.tail
        self.size -= 1
        return carga
        
    def get_head(self):
        return self.head.valor
    def get_tail(self):
        return self.tail.valor
    def get_list(self):
        listaAux = []
        if self.head is None:
            print("A lista está vazia !!")
            return
        current: 'Item' = self.head
        listaAux.append(str(current))
        while current is not self.tail:
            listaAux.append(str(current.next))
            current = current.next
        return listaAux 

lista = ListaCircular()
lista.insert_head(55)
lista.inserir_tail(77)
print("Intes na Lista: ")
print(lista.get_list())
print("Elemento do fim: ", lista.get_tail())
print("Valor do inicio: ", lista.get_head())
print("Removendo fim: ",lista.remove_tail())
print("Removendo inicio: ", lista.remove_head())
print("Lista")
print(lista.get_list())
