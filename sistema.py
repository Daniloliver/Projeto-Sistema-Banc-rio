menu = '''
|-------------------------------|
Bem-vindo ao Sistema Bancário

[s] Sacar
[d] Depositar
[e] Extrato
[q] Sair

|--------------------------------|
=> '''

limite = 500
saldo = 0
qtd_tentativas = 3
extrato = ""
numero_saque = 0
limite_saque = 3


while True:

    opçao = input(menu)

    if opçao == "d":
        valor = float(input("Quanto deseja depositar? "))

        if valor > 0:
            saldo += valor
            extrato += f"deposito: R$ {valor:.2f}\n"
        else:
            print("Operação falhou! O valor informado é inválido.")


    elif opçao == "s":
        valor = float(input("Informe o valor do saque: "))

        excedeu_saldo = valor > saldo

        excedeu_limite = valor > limite

        excedeu_saque = numero_saque >= limite_saque

        if excedeu_saldo:
            print("Operação falhou! Você não tem saldo suciente.")
        
        elif excedeu_limite:
            print("Operação falhou! O valor do saque excedeu o limite.")
        
        elif excedeu_saque:
            print("Operação falhou! Número máximo de saques excedido.")
        
        elif valor > 0:
            saldo -= valor
            extrato += f"Saque: R$ {valor:.2f}\n"
            numero_saque += 1
        
        else: 
            print ("Operação falhou! O valor informado é inválido.")
    
    elif opçao == "e":
        print ("\n*************** EXTRATO **************")
        print("Não foram realizados operações." if not extrato else extrato)
        print (f"\nSaldo: R$ {saldo:.2f}")
        print("*****************************************")
    
    elif opçao == "q":
        break

    else:
        print("Operação inválida, por vafor selecione novamente a operação desejada.")

        

        
        

        

    
    
            
            
