# REGRAS 
#     clientes
#         *Não pode haver mais de um usuario com mesmo cpf

#     conta-corrente 
#         *numero_conta é sequencial comecando em 1
#         *agencia é fixo 0001
#         *usuario pode ter mais de uma conta, mas cada conta tem 
#         apenas um usuario

#     DIca: p/ vincular um usuario a uma conta, filtre a lista
#     de usuarios buscando o nº cpf informado p/ cada usuario
#     da lista



menu = """

[u] Cadastrar usuairo
[c] Cadastar conta
[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """


saldo = 0
limite = 500 # limite de saque por operação
extrato = ""
numero_saques = 0  # contador de saques diarios
LIMITE_SAQUES = 3 # limite de saques diarios


#usuario

clientes = [
    dict.fromkeys([
        'nome',
        'data_nascimento',
        'cpf',
        'endereco'
        ], '')
]

# contas

contas = []
 
# {
#   'ag',
#   'numero_conta',
#   'usuario'
# }



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

    return "success"

def cadastrar_conta(*, cpf):
    isUserRegistered = False
    #check if list is not empty and user exists
    if not len(clientes) == 0:
        for user in clientes:
            if user['cpf'] == cpf:
                isUserRegistered = True
    
        if(not isUserRegistered):
            return
        else:
            #get last account number to iterate by counting accounts quantities
            account_number = len(contas) + 1
            contas.append({
                'ag': '0001',
                'numero_conta': account_number,
                'usuario': cpf
            })
            return "success"
    else:
        contas.append({
                'ag': '0001',
                'numero_conta': 1,
                'usuario': cpf
            })
        return "success"


def depositar(valor, saldo, extrato, /): # arametros posicionais obrigatorio
    if valor > 0:
        saldo += valor
        extrato += f"Depósito: R$ {valor:.2f}\n"
        return "success", saldo, extrato
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
        return 'success', saldo, QtdSaque, extrato
    else:
        print('Saldo insuficiente')
        return

def emitir_extrato(saldo, /, *, extrato): # parametros posicionais e nomeados obrigatorio
    print("\n================ EXTRATO ================")
    print("Não foram realizadas movimentações." if not extrato else extrato) # é um if ternário 
    print(f"\nSaldo: R$ {saldo:.2f}")
    print("==========================================")
    return "success"


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
        if not isUserCreated:
            print("Usuario já possui cadastro !")
            continue
        else:
            print("Usuario criado com sucesso")
            continue

    if opcao == 'c':
        print("### Cadastro de conta. Preencha as informações abaixo ###")
        user_cpf = str(input("Informe o cpf do usuario titular da conta: "))

        isAccountCreated = cadastrar_conta(cpf = user_cpf)

        if(not isAccountCreated):
            print("Usuario não cadastrado. É necessario criar um usuario antes de possuir uma conta")
            continue
        else:
            print("Conta criada com sucesso")
            print(contas[-1], '\n')
            continue

    if opcao == "d":
        valor = float(input("Informe o valor do depósito: "))
        depositSuccessfull = depositar(valor, saldo, extrato)
        if depositSuccessfull:
            saldo = depositSuccessfull[1]
            extrato = depositSuccessfull[2]
            print("Operação realizada com sucesso!")
            continue
        else:
            print("Operação falhou! O valor informado é inválido.")
            continue
        

    elif opcao == "s":
        print(f"O limite de saque por operação é: {limite}")
        print(f"Saldo disponível: {saldo}")
        print(f"Quantidade de saques realizados: {numero_saques}")
        print("########################################")
        valor = float(input("Informe o valor do saque: "))
        withdrawSuccessfull = sacar(valor=valor, saldo=saldo, limite=limite, QtdSaque=numero_saques, extrato=extrato)

        if withdrawSuccessfull:
            saldo = withdrawSuccessfull[1]
            numero_saques = withdrawSuccessfull[2]
            extrato = withdrawSuccessfull[3]
            print("Saque realizado com sucesso!")
            continue
        else:
            continue

    elif opcao == "e":
        emitir_extrato(saldo, extrato=extrato)
        continue

    elif opcao == "q":
        break

    else:
        print("Operação inválida, selecione novamente a operação desejada.")


# print("clientes", clientes)
# print("\n\n\ncontas", contas)

