import os 
import time

os.system("cls")

soma = 0
QUANTIDADE_NOTAS = 3
for i in range(QUANTIDADE_NOTAS):
    nota = float(input("Digite uma nota"))
    media = soma / QUANTIDADE_NOTAS

if media >= 7:
    print("aprovado")
if 4 <= media < 7:
    print("recuperaçao")
if media < 4:
    print("reprovado")