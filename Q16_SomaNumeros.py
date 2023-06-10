from FilaBasss import fila

lista = []

qtd = int(input("Iforme quantos numeros deseja colocar na fila: "))
for num in range(qtd):
    Num = (int(input("Digite um Numero: ")))
    lista.append(Num)
    
    
soma = sum(lista)

print(f"a soma dos numeros da lista é: {soma}")