import os 

os . system("cls")


# ENTRADA DE DADOS 
matriculas = input("Digite a sua matricula: ")

ano_nascimento = int(input("Digite seu ano de nascimento: "))

tempo_de_trabalho = int(input("Digite o tempo de  trabalho em anos: "))

# PROCESSAMENTO
idade = 2026 - ano_nascimento

if idade >= 65 or tempo_de_trabalho >= 30:
  
resultado = "Requerer aposentadoria"

    
# SAIDA
print("\n- Resultado")
print(f"idade: {idade}")
print(f"tempo de trabalho: {tempo_de_trabalho}")
print(f"Resultado: {resultado}")