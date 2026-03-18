import os 

#Limpa terminal
os. system("clas")


login_correto = "Meuca"

Senha_incorreta = 2006


while True :
    login=input("Digite o seu login")
    
    semha=input("Digite sua senha")
    
    if login == login_correto and semha ==Senha_incorreta:
       
        print ("seja bem vindo Meuca")
        
        print ("Se arrombe")
        
        
        break
    
    else:
        print(" Login ou senha invalido...")
        print("Digite sua senha e seu login novamente")