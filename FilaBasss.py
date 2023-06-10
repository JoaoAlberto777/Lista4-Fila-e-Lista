class item:
    def __init__(self, valor):
        self.valor = valor
        self.next = None
    
class fila:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0
        
    def is_empty(self):
        return self.head is None
        
    def push(self, valor):
        NovoItem = item(valor)
        if self.tail is None:
            self.tail = NovoItem
        else:
            self.tail.next = NovoItem
            self.tail = NovoItem
            
        if self.head is None:
            self.head = NovoItem
        self.size += 1
    
    def remove(self):
        if self.is_empty() :
            raise IndexError("A fila está vazia !")
        valor= self.head.valor
        self.head= self.head.next
        if self.head is None:
            self.tail= None
        self.size -= 1
        return valor
        
    def get_size(self):
        
        return self.size
        
    def get_head(self):
        if self.is_empty():
            raise IndexError("A fila esta vazia!")
        return self.head.valor
    
    def get_fila(self):
        if self.is_empty() == True:
            raise IndexError("A fila está vazia !")
        else:
            FilaLista = []
            while not self.is_empty():
                valor = self.remove()
                FilaLista.append(valor)
        return FilaLista

    