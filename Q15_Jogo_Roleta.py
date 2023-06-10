from Lista_Circular_Base import ListaCircular
from random import choice
import time

lista = ListaCircular()

print("Roleta:")
print("A roleta tem números de 20 a 30:")

for num in range(20, 31):
    lista.inserir_tail(num)

palpite = int(input("Diga qual número você acha que vai cair: "))
print("Girando a roleta...")
numSort = choice(lista.get_list())

print("3")
time.sleep(1)
print("2")
time.sleep(1)
print("1")
time.sleep(1)

print("O número da roleta foi: {}".format(numSort))
if palpite == numSort:
    print("Parabéns, você acertou!")
else:
    print("Que azar :(\nGire novamente!")
    
    
    
