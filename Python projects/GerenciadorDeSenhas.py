# 1. criação da senha dentro de uma variável
# 2. criptografia dessa senha com a biblioteca bcrypt 
# 3. armazenamento da senha criptografada 
# 4. descriptografia da senha e exibição

import bcrypt as bc


def criptografia(senha):
    senha_crypto = bc.hashpw(senha.encode('utf-8'), bc.gensalt())
    return senha_crypto

senha = input('Digite sua senha: ')

senha_criptografada = criptografia(senha)

try:
    senha_criptografada = str(senha_criptografada)
    with open('D:\Fiap\Python projects\Gerenciador_de_Senhas.csv', 'a') as arq:
        arq.write(senha_criptografada +'\n')
except FileNotFoundError:
    senha_criptografada = str(senha_criptografada)
    with open('D:\Fiap\Python projects\Gerenciador_de_Senhas.csv', 'w') as arq:
        arq.write(senha_criptografada + '\n')
arq.close()

# em construção