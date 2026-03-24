import os

os.system("cls")

soma_notas = 0
contador_notas = 0
resposta = ""

while  True:
nota = float(input("Digite a nota: "))

soma_notas += nota
contador_notas += 1

resposta = input("Deseja inserir mais uma nota? (S/n): ")

print("Entrada invalida. Por favor, digite um numero para a nota")

if contador_notas > 0:
    media = soma_notas / contador_notas
    print (f"A media aritmédica das {contador_notas} notas informadas é: {media:.2f}")
else:
    print("Nenhuma nota foi informada")
    

