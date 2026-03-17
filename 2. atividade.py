import os 
import time

os.system("cls")

numero = int(input("Digite um numero: "))
for i in range (1,11) :
    print(f"{numero} x {i} = {numero = }")
    time.sleep(2)