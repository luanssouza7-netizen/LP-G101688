import os

os.system("cls")

#Função
def calcular_idade(ano):
    idade = 2026 - ano
    print(f"idade: {idade}")


print("=Solicitado dados =")
anos_nascimento = int(input("Digite o ano de seu nascimento"))

#chamando função para calcular idade.
calcular_idade(anos_nascimento)