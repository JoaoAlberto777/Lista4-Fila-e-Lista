list1 = []
list2 = []
list3 = []
qtd = int(input("Quantos numeros que adcionar a lista?: "))

for i in range (qtd):
    Num = int(input("Informe os Numeros para a lista 1: "))
    list1.append(Num)
print()
for i in range (qtd):
    Num = int(input("Informe os Numeros para a lista 2: "))
    list2.append(Num)
    
for Num in list1:
    if Num in list2:
        list3.append(Num)
print(f"Numeros presentes nas duas lista {list3}")