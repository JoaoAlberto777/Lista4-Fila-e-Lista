from Lista_Dupla_Base import ListaEncadeadaDupla



lista = ListaEncadeadaDupla()
    
infoContato = {}
    
op = 0
    
while op != 4:
    print("Menu: ")
    print("1 -- Inserir contato")
    print("2 -- Buscar contato")
    print("3 -- Remover contato")
    print("4 -- Sair")
    op = int(input(": "))
   
    if op == 1:
        print("Informações do contato: ")
        nome = input("Nome: ")
        num = int(input("Número: "))
        infoContato = {"nome": nome, "numero": num}
        lista.insert_head(infoContato)
        print(f"O contato {nome} foi inserido")
    if op == 2:
        listaBusca = []
        contatoBuscar = input("Digite o nome do contato que deseja pesquisar: ")
        while not lista.is_empty():
            contato = lista.remove_head()
            if contato["nome"] == contatoBuscar:
                print("Informações do contato: ")
                print(f"Nome: {contato['nome']}")
                print(f"Número: {contato['numero']}")
            else:
                print("Contato não encontrado!")
            listaBusca.append(contato)
        for i in listaBusca:
            lista.insert_tail(i)    
                 
    if op ==  3:
        listaRemove = []
        contatoRemove = input("Digite o nome do contato que deseja apagar: ")
        while not lista.is_empty():
            cont = lista.remove_head()
            if not cont['nome'] == contatoRemove:
                listaRemove.append(cont)
            elif cont['nome'] == contatoRemove :
                print(f"Contato '{cont['nome']}' foi apagado !")
        for com in listaRemove:
            lista.insert_tail(com)                              
                
    if op == 4:
        print("Programa Encerrado!!")
        break


