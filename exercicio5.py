import os

os.system("cls")

vetor_5=[]

qtr_negativo=0

soma_total_dos_positivos=0

for i in range(0,5):
    numero=int(input("Digite um numero"))
    
    vetor_5.append(numero)
    
    if vetor_5[i] <0:
       qtr_negativo+=1
       
    else:
        soma_total_dos_positivos+=vetor_5[i]
    
print(f"A soma dos positivos de:{soma_total_dos_positivos}")

print(f"A quantidade de Negativo é de:{qtr_negativo}")
        