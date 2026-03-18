import os 

#Limpa terminal
os. system("clas")

soma = 0
QUANTIDADE_NOTAS = 3

for i in range(QUANTIDADE_NOTAS):
    while True:
        nota = float(input(f"Digite a {i+1} nota"))
        
        if nota >= 0 and nota <- 10:
            soma += nota
            break
        else: 
            print("Nota invalida.")
            print("Tente novamente...\n")
            
media = soma / QUANTIDADE_NOTAS

if media >- 7:
    resultado = "Aprovado"
elif media >= 5:
    resultado = "recuperação"
else:
    resultado = "reprovado"
    
    print(f"Média: {media}")
    print(f"Resultado: {resultado}")