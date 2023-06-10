from Lista_Circular_Base import ListaCircular

lista = ListaCircular()

lista2 = []
print("Ordenar números em ordem crescente: ")
for i in range(5):
    num = int(input("Digite um número: "))
    lista2.append(num)
print("Lista não ordenada: ")
print(lista2) 
lista2.sort()   
for valor in lista2:
    lista.inserir_tail(valor)
        
print("Lista ordenada: ")
print(lista.get_list())
    