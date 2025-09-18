menu = """

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
cliente = [{}]

# reescrevendo este programa com uso de funções
#criar funções para cada operação




#                           FUNÇÕES

#criar usuario
#criar conta-corrente


def depositar(valor, saldo, extrato, /):
    if valor > 0:
        saldo += valor
        extrato += f"Depósito: R$ {valor:.2f}\n"
        return 1
    else:
        return

def sacar(*, valor, saldo, limite, QtdSaque, extrato, /): # parametros posicionais obrigatorio
    if valor > 0 and valor <= saldo:
        saldo -= valor
        QtdSaque += 1
        extrato += f"Saque: R$ {valor:.2f}\n"
    else:
        return

def emitir_extrato(saldo, /, *, extrato): # parametros nomeados obrigatorio
    print("\n================ EXTRATO ================")
    print("Não foram realizadas movimentações." if not extrato else extrato) # é um if ternário 
    print(f"\nSaldo: R$ {saldo:.2f}")
    print("==========================================")
    return 1


# ==============================================




while True:

    opcao = input(menu)

    if opcao == "d":
        valor = float(input("Informe o valor do depósito: "))

        if (depositar(valor, saldo, extrato)):
            print("Operação realizada com sucesso!")
        else:
            print("Operação falhou! O valor informado é inválido.")
        

    elif opcao == "s":
        valor = float(input("Informe o valor do saque: "))

        excedeu_saldo = valor > saldo

        excedeu_limite = valor > limite

        excedeu_saques = numero_saques >= LIMITE_SAQUES

        if excedeu_saldo:
            print("Operação falhou! Você não tem saldo suficiente.")

        elif excedeu_limite:
            print("Operação falhou! O valor do saque excede o limite.")

        elif excedeu_saques:
            print("Operação falhou! Número máximo de saques excedido.")

        elif (sacar(valor, saldo, LIMITE_SAQUES, extrato)):
            print("Saque realizado com sucesso!")
        else:
            print("Operação falhou! O valor informado é inválido.")

    elif opcao == "e":
        emitir_extrato(extrato=extrato, saldo=saldo)

    elif opcao == "q":
        break

    else:
        print("Operação inválida, selecione novamente a operação desejada.")

