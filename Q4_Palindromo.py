from FilaBasss import fila

Frase = str(input("Digite uma frase: ")).replace(" ", "").lower()

FilaFrase = fila()

for char in Frase:
    FilaFrase.push(char)

if Frase == Frase[::-1]:
    print("A frase digite é um palindormo!")
else: 
    print("A frase digitada NÃO é um palindromo!")