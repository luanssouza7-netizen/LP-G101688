import os

os.system("cls")

vetor = []
tamanho_vetor = 5

for i in range(tamanho_vetor):
    valor = int(input(f"Digite o [i+1]ª numero: "))
    if valor < 0:
        vetor.append(valor)
        print("Valores no vetor:", vetor)