import os
os.system("cls")

usuario = ''
senha = ''
tentativas = 0

while (usuario != "caua" and senha != "1234") and tentativas <5:
    usuario = input("Digite seu usuario: ")
    senha = input("Digite sua senha: ")
    tentativas +=1
if usuario == 'caua' and senha == '1234':
    print("Login efetuado com sucesso!")
else:
    print("Tente novamente em outra hora.")