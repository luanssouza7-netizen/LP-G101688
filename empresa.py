import os
import csv

os.system("cls")
from dataclasses import dataclass

@dataclass
class Empresas:
    nome : str
    cnpj : str
    telefone : str

    def mostra_dados(self):
        print(f"nome : {self.nome}")
        print(f" Cnpj :{self.cnpj}")
        print(f"telefone : {self.telefone}")

empresas = Empresas(
    nome=input("Digite o nome da empresa:"),
    cnpj=input("Digite o cnpj")
    telefone=input("Digite o numero do telefone da empresa: ") )

lista_de_empresas = []
lista_empresas.append(empresas)

with open('contado_empresa.cvs','a', enconding='utf-8') as file:
    for empresa in lista_empresas:
        file.write(f"{empresa.nome},{empresa.cnpj},{empresa.telefone}")

    for empresa  in lista_empresas:
        empresa.mostra_dados()