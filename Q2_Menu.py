from FilaBasss import fila

Menu = ("1. Adicionar Número", "2. Remover Número", "3. Mostra Tamanho", "4. Mostrar Fila", "5. Sair")
filaNum = fila()
while True:
    print("-----MENU-----")
    for opção in Menu:
        print(opção)
    
    op = int(input("Escolha uma opção: "))
    
    if op == 1:
        qtd = int(input("Quantos números quer adicionar a fila?: "))
        for i in range(qtd):
            Num = float(input("Adicione um Número a Fila: "))
            filaNum.push(Num)
            print(f"Numero {Num} adicionado a Fila!")
    
    elif op == 2:
        qtd = int(input("Quantos números quer removar da fila?: "))
        for i in range (qtd):
            if filaNum.is_empty():
                print("A fila está vazia.")
        else:
            NumR = float(input("Remova um Número da Fila: "))
            NumR = filaNum.remove()
            print(f"Número removido da fila: {NumR}")
    
    elif op == 3:
        print(f"o tamanho da fila é {filaNum.get_size()}")
    
    elif op == 4:
        print(filaNum.get_fila())
    
    elif op == 5:
        print("programa encerrado...")
        break
    else: 
        raise IndexError("Opção Invalida!!!!")
        

