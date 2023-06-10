lista_dicionario = []
qtd = int(input("Quantos alunos deseja adicionar?: "))

for i in range(qtd):
    nome = str(input("Digite o nome do aluno: "))
    nota = float(input("Digite a nota do aluno: "))
    dicionario = {"Nome": nome,"Nota": nota}
    lista_dicionario.append(dicionario)

maior_nota = 0
nome_maior_nota = ""

for aluno in lista_dicionario:
    nome = aluno["Nome"]
    nota = aluno["Nota"]
    if nota > maior_nota:
        maior_nota = nota
        nome_maior_nota = nome
    
print(lista_dicionario)
print()
print(f"o aluno com a maior nota é {nome_maior_nota}")