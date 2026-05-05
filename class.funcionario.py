import os 

os.system("Cls")

class funcionario:
    idade: int

    def mostrar_dados(self):
        print(f"Nome: {self.nome}")
        print(f"idade: {self.idade}")

Quantidade_Funcionario = 2
lista_funcionarios = []

print('= Solicitando dados = ')
for i in range(Quantidade_Funcionario):
    novo_funcionario = funcionario(
        nome=input('Digite seu nome: '),
    idade=int(input('Digite sua idade: ')),
    )
    print('')
    lista_funcionarios.append(novo_funcionario)

    print('= salvando dados =')
    with open('lista_funcionario.csv, 'a', encoding='utf-8') as arquivos:
    for funcionario in lista_funcionarios:
        arquivos.write(f'{funcionario,nome}, {funcionario.idade}\n')
    
        print('= fim do programa. ='):
        