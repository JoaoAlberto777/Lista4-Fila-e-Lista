from ListaBase import ListaEncadeada

lista = ListaEncadeada()

Cliente = []
InfoCliente = {}
Menu = ["1 - Adicionar Cliente", "2 - Remover Cliente", "3 - Pesquisar Cliente na Lista", "4 - Sair"]

for i in range(2):
    nome = str(input(f"Informe o nome do {i+1}° Cliente: "))
    conta = int(input(f"Informe o N° da Conta do {i+1}° Cliente: "))
    saldo = float(input(f"Informe o saldo do {i+1}° Cliente: "))
    InfoCliente = {"Nome": nome, "Conta": conta, "Saldo": saldo}
    Cliente.append(InfoCliente)

while True:
    print("-----OPÇÕES-----")
    for opção in Menu:
        print(opção)
    op = int(input("Escolha uma opção: "))
    if op == 1:
        nome = input("Informe o nome do cliente: ")
        conta = int(input("Informe o número da conta: "))
        saldo = float(input("Informe o saldo do cliente: "))
        InfoCliente = {"Nome": nome, "Conta": conta, "Saldo": saldo}
        Cliente.append(InfoCliente)
        print(Cliente)

    elif op == 2:
        if len(Cliente) > 0:
            index = int(input("Informe o índice do cliente que deseja remover: "))
            if index >= 0 and index < len(Cliente):
                Cliente.pop(index)
                print(Cliente)
            else:
                print("Índice inválido!")
        else:
            print("A lista de clientes está vazia!")

    elif op == 3:
        if len(Cliente) > 0:
            nome = input("Informe o nome do cliente que deseja pesquisar: ")
            found = False
            for cliente in Cliente:
                if cliente["Nome"] == nome:
                    found = True
                    print("Cliente encontrado:")
                    print("|   NOME   |   CONTA   |   SALDO   |")
                    print("|", cliente["Nome"].ljust(9), "|", str(cliente["Conta"]).ljust(9), "|", str(cliente["Saldo"]).ljust(9), "|")
                    break
            if not found:
                print("Cliente não encontrado!")
        else:
            print("A lista de clientes está vazia!")
    elif op == 4:
        print("Programa Encerrado!!")
        break
   