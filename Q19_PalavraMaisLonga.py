lista = []
qtd = int(input("Quantas palavras deseja por na lista?: "))

for i in range(qtd):
    palavra = input("Digite uma palavra: ")
    lista.append(palavra)
    
palavra_longa = ""

for palavra in lista:
    if len(palavra) > len(palavra_longa):
        palavra_longa = palavra
     
print(f"As palavras presente na lista são: {lista}")
print(f"a palavra mais longa da lista é: {palavra_longa} ")