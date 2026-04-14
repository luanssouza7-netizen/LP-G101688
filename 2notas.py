import os

os.system("cls")

def calcular_media(n1, n2):
    return (n1 + n2) / 2

def verificar_situaçao(media):
    if media >= 7:
        resultado = "Aprovado"
    else:
        resultado = "Reprovado"
    return resultado

print("= solicitando dados =")
while true:
primero_nota = float(input("Digite a primeira nota: "))
if primero_nota >= 0 or primeiro_nota <10:
    break

while true:    
    segundo_nota = float(input("Digite a segunda nota:"))
    if segunda_nota>= 0 and segunda_nota <= 10:
    break
media = calcular_media(primeira_nota, segunda_nota) # type: ignore
situacao = verificar_situaçao(media)

print("\n= Exibindo dados =")
print(f"Média: {media}")
print (f"Resultado: {situacao}")