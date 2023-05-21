import re

print("Seja Bem Vindo ao GreenLight!")
print("Nosso objetivo é deixar o mundo mais verde!!")
print("Como deseja seguir por aqui?")
print("(1)-Fazer Login")
print("(2)-Fazer Cadastro")
print("Escolha entre '1' e '2'")
dec = int(input())
if not type(dec) is int:
    raise ValueError


def validarCpf(cpf):

    cpf = ''.join(filter(str.isdigit, cpf))

    if len(cpf) != 11:
        return False

    
    if cpf == cpf[0] * 11:
        return False

    soma = sum(int(cpf[i]) * (10 - i) for i in range(9))
    digito1 = (soma * 10) % 11
    if digito1 == 10:
        digito1 = 0
    soma = sum(int(cpf[i]) * (11 - i) for i in range(10))
    digito2 = (soma * 10) % 11

    if digito2 == 10:
        digito2 = 0

    if int(cpf[9]) != digito1 or int(cpf[10]) != digito2:
        return False

    return True

def validarEmail(email):
    if '@' not in email:
        return False

    if '.' not in email[email.index('@'):]:
        return False
    return True

def validarCelular(celular):
    celular = ''.join(filter(str.isdigit, celular))
    if len(celular) != 11:
        return False

    return True

def validar_senha(senha, ):
    if len(senha) < 8 or len(senha) > 12:
        return False


    return True

def validarSenha(senha, confirmacaoSenha):
    return senha == confirmacaoSenha

# LOGIN
if dec == 1:
    print("Bem vindo novamente!")
    print("Digite seu E-mail de login:")
    emailLogin = input()
    print("Digite sua senha:")
    senhaLogin = input()
    print("Seja Bem-Vindo novamente!")
    print("Transforme o mundo conosco")

# CADASTRO
if dec == 2:
    print("Seja Bem-Vindo ao GreenLight!")
    print("Para fazer cadastro complete as informações abaixo:")
    print("Nome completo:")
    nome = str(input())
    if not type(nome) is str:
        raise ValueError

    print("Email:")
    emailC = input()
    if validarEmail(emailC):
        print("E-mail válido!")
    else:
        print("Formato E-mail inválido!")
        raise ValueError
    
    print("CPF (formato XXXXXXXXX-XX):")
    cpf = input()
    if validarCpf(cpf):
        print("CPF válido!")
    else:
        print("CPF inválido!")
        raise ValueError

    print("Número de telefone (formato (XX)XXXXX-XXXX):")
    tel = input()
    if validarCelular(tel):
        print("Número de celular válido!")
    else:
       print("Formato de número de celular inválido!")
       raise ValueError
    
    print("Endereço :")
    endereco = input()
    print("Digite sua senha de cadastro (Mínimo de caracteres 8, e máximo 12):")
    senhaC = input()
    if validar_senha(senhaC):
        print("Confirmação de senha correta!")
    else: 
        print("Formato de senha incorreto")
        raise ValueError

    print("Confirme sua senha de cadastro:")
    senhaConf = input()
    if validarSenha(senhaC, senhaConf):
        print("Seu login foi confirmado!")
        print("Seja Bem-Vindo à família GreenLight!")
        print("Faça nosso mundo um lugar melhor!")
        print("Lembre-se, o lixo pode não ser seu, mas a Terra é")
    else:
        print("Senhas diferentes!")
        raise ValueError