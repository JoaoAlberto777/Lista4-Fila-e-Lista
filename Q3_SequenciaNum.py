from FilaBasss import fila

Seq = fila()

print("Se um número negativo for digitado a inserção sera interrompida!")
while True:
    Num = int(input("Digite um número: "))
    
    
    if Num < 0:
       break
    else:
        Seq.push(Num)
    
print(f"Numeros inseridos na fila: {Seq.get_fila()}")
