import os 

os.system("cls")

notas = []

for i in range (4):
     nota = float(input(f"Digite a nota {i+1} "))
notas.append(nota)

# Calcula a media aritmédica 
media = sum(notas) / len(notas)

# Verifica a situação do aluno
if media >= 7:
    situação = "aprovado"
elif media >= 5:
    situacao = "Recuperação"
else:
    situação = "reprovado"

#Exibe os Resultado.

print("\n--- Resultado Final---")
print(f"Notas informadas: {notas}")
print(f"media: {media:.2f}")
