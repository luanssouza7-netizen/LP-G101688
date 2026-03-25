import os 

os.system("cls")

# Criando um vetor.
vetor_notas = []
QUANTIDADE_NOTAS = 3

print("Adicionando 3 notas. ")
for i in range(QUANTIDADE_NOTAS):
    nota = float(input(f"Digite a {i+1}ª nota "))
# Adiciona nota no vetor
vetor_notas.append(nota)

# sum(vetor) = soma todas  os valores no vetor.
media = sum (vetor_notas) / QUANTIDADE_NOTAS

print("\nexibido as notas informadas. ")
# foreach = percorre o vetor sem informar a quantidade.
# eumerate = atraves da variavel i, numero a quantidade de repetições.
for i, uma_nota in enumerate(vetor_notas, start=1):
    print(f"{i}ª nota: {uma_nota}")
    
    print(f"Media: {media}")