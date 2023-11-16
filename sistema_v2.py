import textwrap

def menu():

    menu = '''\n
    |-------------------------------|
        Bem-vindo ao Sistema Bancário

    [d]\tDepositar
    [s]\tSacar
    [e]\tExtrato
    [nc]\tNova conta
    [lc]\tListar conta
    [nu]\t Novo usuario
    [q]\tSair

    |--------------------------------|
    => '''
    return input(textwrap.dedent(menu))

def depositar(saldo, valor, extrato, /):

    if valor > 0:
        saldo += valor
        extrato += f"deposito:\tR$ {valor:.2f}\n"
        print("\n=== Depósito realizado com sucesso! ===")
    else:
        print("\n@@@ Operação falhou! O valor informado é inválido. @@@")
    
def sacar(*, saldo, valor, extrato, limite, numero_saques, limite_saques):

    excedeu_saldo = valor > saldo
    excedeu_limite = valor > limite
    excedeu_saque = numero_saques > limite_saques

    if excedeu_saldo:
            print("\n@@@ Operação falhou! Você não tem saldo suciente. @@@")
        
    elif excedeu_limite:
        print("\n@@@ peração falhou! O valor do saque excedeu o limite. @@@")
        
    elif excedeu_saque:
        print("\n@@@ Operação falhou! Número máximo de saques excedido. @@@")
    
    elif valor > 0:
        saldo -= valor
        extrato += f"Saque:\t\tR$ {valor:.2f}\n"
        numero_saques += 1
        print("\n=== Saque realizado com sucesso! ===")
        
    else: 
        print ("\n@@@ Operação falhou! O valor informado é inválido. @@@")
    
    return saldo, extrato

def exibir_extrato(saldo, /, *, extrato):
    
    print ("\n*************** EXTRATO **************")
    print("Não foram realizados operações." if not extrato else extrato)
    print (f"\nSaldo: R$ {saldo:.2f}")
    print("*****************************************")

def criar_usuario(usuarios):
    cpf = input("Informe o CPF (somente número): ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("\n@@@ Já existe usuário com esse cPF! @@@")
        return
    
    nome = input("Informe o nome  completo: ")
    data_nascimento = input("Informe a data de nascimento (dd-mm-aaaa): ")
    endereco = input("Informe o endereço (logradouro, numero - bairro - cidade/sigla estado): ")

    usuarios.append({"nome": nome, "data_nascimento": data_nascimento, "cpf": cpf, "endereco": endereco})

    print("=== Usuário criado com sucesso! ===")

def filtrar_usuario(cpf, usuarios):

    usuarios_filtrados = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None

def criar_conta(agencia, numero_conta, usuarios):
    cpf = input("Informe o cPF do usuário: ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("\n==== Conta criado com sucesso! ===")
        return {"agencia": agencia, "numero_conta": numero_conta, "usuario": usuario}
    
    print("\n@@@ Usuário não encontrado, fluxo de criação de conta encerrado! @@@")

def listar_contas(contas):
    for conta in contas:
        linha = f"""\
            Agência:\t{conta['agencia']}
            C/C:\t\t{conta['numero_conta']}
            Titular:\t{conta['usuario']['nome']}
        """
        print("#" * 100)
        print(textwrap.dedent(linha))


def main():

    LIMITE_SAQUES = 3
    AGENCIA = "0001"

    saldo = 0
    limite = 500
    extrato = ""
    numero_saques = 0
    usuarios = []
    contas = []
    

    while True:

        opçao = menu()

        if opçao == "d":
            valor = float(input("Quanto deseja depositar? "))
    
            saldo, extrato = depositar(saldo, valor, extrato)

        elif opçao == "s":
            valor = float(input("Informe o valor do saque: "))

            saldo, extrato = sacar(
                saldo=saldo,
                valor=valor,
                extrato=extrato,
                limite=limite,
                numero_saques=numero_saques,
                limite_sauqes=LIMITE_SAQUES
            )
    
        elif opçao == "e":
            exibir_extrato(saldo, extrato=extrato)
    
        elif opçao == "nu":
            criar_usuario(usuarios)
    
        elif opçao == "nc":
            numero_conta = len(contas) + 1
            conta = criar_conta(AGENCIA, numero_conta, usuarios)

            if conta:
                contas.append(conta)
        
        elif opçao == "lc":
            listar_contas(contas)
        
        elif opçao == "q":
            break

        else:
            print("Operação Inválida, por favor selecione a operação desejada.")