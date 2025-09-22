menu = """

[u] Cadastrar usuairo
[c] Cadastar conta
[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """

###

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3


#usuario

clientes = [{}]

# contas

contas = [{}]

"""
cliente = [
    usuario1 = {
        nome: ,
        data_nascimento: ,
        cpf: string(apenas numeros),
        endereço: string (logradouro, nº - bairro - cidade/sigla estado)
    }
]

*Não pode haver mais de um usuario com mesmo cpf

conta-corrente 

contas = [
    conta1: {
        ag: ,
        numero_conta: ,
        usuario: ,
    }
]

*numero_conta é sequencial comecando em 1
*agencia é fixo 0001
*usuario pode ter mais de um conta, mas cada conta tem 
 apenas um usuario

 DIca: p/ vincular um usuario a uma conta, filtre a lista
  de usuarios buscando o nº cpf informado p/ cada usuario
  da lista
"""
clientes = [
    dict.fromkeys([
        'nome',
        'data_nascimento',
        'CPF',
        'endereco'
        ], '')
]

"""
        nome: ,
        data_nascimento: ,
        cpf: string(apenas numeros),
        endereço: string (logradouro, nº - bairro - cidade/sigla estado)
"""

#                           FUNÇÕES

def cadastrar_usuario(*, nome: str, data_nascimento: str, CPF: str, endereco: str):

    #check if cpf already exists
    for usuario in clientes:
        if usuario['cpf'] == CPF:
            return
    
    clientes.append({
        'nome': nome,
        'data_nascimento': data_nascimento,
        'cpf': CPF,
        'endereco': endereco
    })

    return 1

#def cadastrar_conta():

def depositar(valor, saldo, extrato, /): # arametros posicionais obrigatorio
    if valor > 0:
        saldo += valor
        extrato += f"Depósito: R$ {valor:.2f}\n"
        return 1
    else:
        return

def sacar(*, valor, saldo, limite, QtdSaque, extrato): # parametros nomeados obrigatorio
    if(valor>limite): 
        print('o valor é maior que o limite por operação')
        return
    if(QtdSaque >= LIMITE_SAQUES):
        print('Você ja atingiu a quantidade de saques diário. Faça upgrade do seu plano para saques ilimitados :)')
        return
    if(valor <= 0):
        print('O valor precisa ser maior do que 0')
        return 
    if valor <= saldo:
        saldo -= valor
        QtdSaque += 1
        extrato += f"Saque: R$ {valor:.2f}\n"
        return 'success'
    else:
        print('Saldo insuficiente')
        return

def emitir_extrato(saldo, /, *, extrato): # parametros posicionais e nomeados obrigatorio
    print("\n================ EXTRATO ================")
    print("Não foram realizadas movimentações." if not extrato else extrato) # é um if ternário 
    print(f"\nSaldo: R$ {saldo:.2f}")
    print("==========================================")
    return 1


# ==============================================



while True:

    opcao = input(menu)

    if opcao == "u":
        print("### Cadastro de usuario. Preencha as informações abaixo ###")
        user_name = str(input("Informe o nome: "))
        user_birth = str(input("Informe a data de nascimento: "))
        user_cpf = str(input("Informe o cpf: "))
        user_address = str(input("Informe o endereço: "))

        isUserCreated = cadastrar_usuario(nome = user_name, data_nascimento=user_birth, CPF=user_cpf, endereco=user_address)
        if isUserCreated:
            print("Usuario já possui cadastro !")
        else:
            print("Usuario criado com sucesso")


    if opcao == "d":
        valor = float(input("Informe o valor do depósito: "))

        if (depositar(valor, saldo, extrato)):
            print("Operação realizada com sucesso!")
        else:
            print("Operação falhou! O valor informado é inválido.")
        

    elif opcao == "s":
        valor = float(input("Informe o valor do saque: "))

        if (sacar(valor=valor, saldo=saldo, limite=LIMITE_SAQUES, QtdSaque=numero_saques ,extrato=extrato)):
            print("Saque realizado com sucesso!")
        else:
            continue

    elif opcao == "e":
        emitir_extrato(saldo, extrato=extrato)

    elif opcao == "q":
        break

    else:
        print("Operação inválida, selecione novamente a operação desejada.")

