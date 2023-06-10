from ListaBase import ListaEncadeada

lista = ListaEncadeada()
lista_reversa = []
qtd = int(input("Quantos numeros deseja adicionar a lista?: "))

for i in range(qtd):
    Num = int(input(f"Digite o {i+1}° Número: "))
    lista.insert_tail(Num)
    lista_reversa.insert(0, Num)
    
print("Lista original: ", lista.get_list())
print("Lista reversa: ", lista_reversa)