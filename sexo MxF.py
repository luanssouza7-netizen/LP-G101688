import os

soma_salario = 0
total_pessoas = 0
maior_idade = -1 
menor_idade = 200
mulheres_salario_alto = 0

while True:
    print("--- MENU---")
    print("1 | Adicionar pessoa")
    print("2 | exibir resultados")
    
    opcao = input("Escolha uma opção: ")
    
if opcao == '1':
    
    os.system('cls' if os.name == 'nt' else 'clear')
    
    idade = int(input("Digite a idade: "))
    sexo  = input("Digite o sexo (M/F): ")
    salario = float(input("Digite o salario: R$ "))
    
    soma_salario += salario 
    total_pessoas += 1
    
    if idade > maior_idade:
        maior_idade = idade
    if idade < menor_idade:
        menor_idade = idade 
        
    if sexo == 'f' and salario >= 5000:
        mulheres_salario_alto += 1
        
    print ("\nDados adicionados com sucesso!. /n")
    
elif opcao == '2':
    if total_pessoas == 0: 
        print ("\nNenhum dado cadastrado ainda. \n")
    else:
        media_salario = soma_salario / total_pessoas
        print("\n--- RESULTADO---")
        print(f"a) Media de salario do grupo: R$ {media_salario:.2f}")
        print(f"b) Maior idade: {maior_idade}  |  menor idade: {menor_idade}")
        print(f"c) Quantidade de mulheres com salario >= R$ 5.000,00: { mulheres_salario_alto}")
        print("-------------------\n")
        
elif opcao == '3':
    print("salario do programa...")
    break
else:
    print("Opção invalida! Tente novamente.")