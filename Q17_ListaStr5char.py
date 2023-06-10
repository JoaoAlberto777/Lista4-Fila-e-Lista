lista = []

qtd = (int(input("Informe quantas palavras deseja inserir na Lista: ")))

for i in range(qtd):
    palavras = str(input("Digite uma palvara: "))
    if len(palavras) >= 5:
        lista.append(palavras)

print(lista)



    

