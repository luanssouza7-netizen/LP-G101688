import os 

os.system("cls")

numeros = []
pares = 0 
impares = 0 

# lendo os 6 numeros
for i in range(6):
    num = int(input(f"Digite o [i+1] numero: "))
    numeros.append(num)
    
    #Verificando se é par ou impar
if num % 2 == 0:
    pares += 1
else:
    impares += 1

print ("-" * 30)
print (f"Numeros informados: {numeros}")
print (f" Quantidade de pares: {pares}")
print (f"Quantidade impares: {impares}")