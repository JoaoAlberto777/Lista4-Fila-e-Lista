from FilaBasss import fila
from time import sleep

filaCliente = fila()

print("Informe o N° de identificação do Cliente: ")

for i in range(5):
    Num = int(input(f"{i+1}° Cliente: "))
    filaCliente.push(Num)
    
print("Caixa Aberto!!!")

for j in range(5):
    sleep(5) 
    print(f"Atendendo {j+1}° cliente!")
    print("Codigo: ", filaCliente.remove())
    print("Atendimento bem sucessido!")
    
print("Todos os Clientes foram atendidos!")
  