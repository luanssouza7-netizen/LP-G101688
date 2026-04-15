import os

os.system("cls")

def calcular_imc(peso, altura):
    return peso / (altura **2)

    #Função
def interpretar_imc(imc):
    if imc < 18.5:
        return"Abaixo do peso"
    elif 18.5 <= imc < 25:
        return"peso normal"
    elif 25 <= imc < 30:
        return"sobrepeso"
    elif 30 <= imc < 35:
        return"Obesidade grau I"
    elif 35 <= imc < 40:
        return "Obesidade grau II"
    else:
        return "Obesidade grau III (mórbida)"
    
    def processar_usuario(usuarios):
        for usuario in usuario:
         nome = usuario['nome']
        #Solicitar sobrenome (item 2.1)
        sobrenome = input(f"Digite o sobrenome de {nome}: ")
        nome_completo = f"{nome} {sobrenome}"

        peso = usuario ['peso']
        altura = usuario['altura']

#Calculo e classificação
        valor_imc = calcular_imc(peso, altura)
        situacao = interpretar_imc(valor_imc)

#exibição dos resultado (item 2)
print("-" * 30)
print(f"Nome Completo: {nome_complete}")
print(f"IMC calculando: {valor_imc:.2f}") # type: ignore
print(f"Situação: {situacao}")