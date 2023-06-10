from ListaBase import ListaEncadeada

lista = ListaEncadeada()

Cliente = []
InfoCliente = {}
Menu = ["1 - Adicionar Cliente", "2 - Remover Cliente", "3 - Pesquisar Cliente na Lista", "4 - Mostrar todos os Clientes", "5 - Sair"]

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
        if Cliente:
            nome = input("Informe o nome do cliente que deseja remover?: ")
            found = False
            for c in Cliente:
                if c["Nome"] == nome:
                    Cliente.remove(c)
                    found = True
                    print(f"Cliente {c} foi removido da lista: ")
                
        else:
            print("A lista de clientes está vazia!")

    elif op == 3:
        if len(Cliente) > 0:
            nome = input("Informe o nome do cliente que deseja pesquisar: ")
            found = False
            for cliente in Cliente:
                if cliente["Nome"] == nome:
                    found = True
                    print("Cliente esta na lista:")
                    print("|NOME| CONTA |   SALDO   |")
                    print("| {} |  {}   |    {}    |".format(cliente["Nome"], (cliente["Conta"]), (cliente["Saldo"])))
                    break
            if not found:
                print("Cliente não esta na lista!")
        else:
            print("A lista de clientes está vazia!")
    elif op == 4:
        print("Lista de clientes:")
        print("|   NOME   |   CONTA   |   SALDO   |")
        for cliente in Cliente:
            print("|   {}   |    {}      |    {}    |".format(cliente["Nome"], (cliente["Conta"]), (cliente["Saldo"])))
        else:
            print("A lista de clientes está vazia!")
    elif op == 5:
        print("Programa Encerrado!!")
        break
   
