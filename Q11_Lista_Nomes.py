from Lista_Dupla_Base import ListaEncadeadaDupla

def ordenar(nomes):
    lista = ListaEncadeadaDupla()  
    nomes.sort()
    for name in nomes:
        lista.insert_tail(name)
    return lista.get_list()    

print("Preencha com os nomes: ")
nome = []
for i in range(0, 3):
    nome.append(input(f"Nome {i + 1}: "))

nomeOrdenado = ordenar(nome)  
print("A Lista em ordem alfabética é: ")
print(nomeOrdenado)