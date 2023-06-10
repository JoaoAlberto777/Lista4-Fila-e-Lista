class Item:
    def __init__(self,dado):
        self.valor = dado
        self.prev = None
        self.next = None

class ListaEncadeadaDupla:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0
    
    def insert_head(self,valor):
        novo_valor = Item(valor)
        if self.head is None:
            self.head = novo_valor
            self.tail = novo_valor
        else:
            novo_valor.next = self.head
            self.head.prev = novo_valor
            self.head = novo_valor
        self.size += 1
    def insert_tail(self,valor):
        novo_valor = Item(valor)
        if self.tail is None:
            self.head = novo_valor
            self.tail = novo_valor
        else:
            novo_valor.prev = self.tail
            self.tail.next = novo_valor
            self.tail = novo_valor
        self.size += 1
    def remove_head(self):
        if self.head is None:
            raise IndexError("A lista está vazia !!")
        valor = self.head.valor
        if self.head == self.tail:
            self.head = None
            self.tail = None
        else:
            self.head = self.head.next
            self.head.prev = None
        self.size -= 1   
        return valor 
    def remove_tail(self):
        if self.head is None:
            raise IndexError("A lista está vazia !!")
        else:
            valor = self.tail.valor
            self.tail = self.tail.prev
            self.tail.next = None
        self.size -= 1
        return valor
    def get_size(self):
        return self.size
    def in_empty(self):
        return self.head == None
    def get_list(self):
        listaAux = []
        while not self.in_empty():
            valor = self.remove_head()
            listaAux.append(valor)
        return listaAux    

lista = ListaEncadeadaDupla()
lista.insert_head(11)
lista.insert_tail(22)
lista.insert_tail(33)
print("Esta Vazia?:", lista.in_empty())
print("Tamanho: ",lista.get_size())
print("Remover na Frente: ",lista.remove_head())
print("Itens Lista: ")
print(lista.get_list())
