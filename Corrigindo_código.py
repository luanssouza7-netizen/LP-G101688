import os

os.system("cls")

numeros = []
pares = []
impares = []
positivo = []
negativos =[]

#Entradas de dados
for i in range(5):
    num = int(input(f"Digite o {i+1}ª numero"))
numeros.apprend(num)

#Verificação de par/impar
if num % 2 == 0:
    pares.append(num)
else:
    impares.append(num)


if num > 0:
    positivo += 1
elif num < 0:
    negativos += 1

#Proscessamento de dados
maior = max(numeros)
menor = min(numeros)
meidia_total= sum(numeros) / len(numeros)
quantidade_pares = sum(pares) / len(pares) if pares else 0
quantidade_impares = sum(impares) / len(impares) if impares  else 0

print("\n---Resultado---")
print(f"pares: {len(pares)} | impares: {len(impares)}")
print(f"Positvos: {positivo} | Negativos: {negativos}")
print(f"Total de números interidos: {len(numeros)}")
print(f"Maior: {maior} | menor: {menor}")
print(f"Media dos pares: {media_pares:.2f}")
print(f"Meida dos impares: {media_impares:.2f}")
print("Media geral: {meida_total:.2f}")
print(f"Ordem inversa: {numeros}[::-1]")