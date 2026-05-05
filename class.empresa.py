import os 

os.system("cls")

def mostrar_dados(self):
    print(f'Nome:{self.nome}')
    print(f'CNPJ:{self.c}')
    print(f'Telefone: {self.telefone}\n')

lista_empresas = []

with open('contado_empresas.csv', 'r') as arquivo:
    for linha in arquivo:
        nome, cnpj, telefone = linha.sprip().split(',')
        lista_empresas.append(empresa(
            nome=nome,
            cnpj=cnpj,
            telefone=telefone,
        ))
for empresa in lista_empresas:
    empresa.mostrar_dados()