menu = """

[1] Despositar
[2] Sacar
[3] Extrato
[0] Sair

=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:

    opção = input(menu)

    if opção == "1":
        valor = float(input("Informe o valor do depósito: "))

        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"

        else:
            print("Operação falhou! o valor informado é invalido")


    elif opção == "2":
        valor = float(input("Informe o valor do saque: "))

        excedeu_saldo = valor > saldo

        excedeu_limite = valor > limite

        excedeu_saque = numero_saques >= LIMITE_SAQUES

        if excedeu_saldo:
            print("Operação falhou! saldo insuficiente.")
            print("Seu saldo é de:",saldo)
        
        elif excedeu_limite:
            print("Operação falhou! o valor do saque excede o limite.")
            print("Seu limite é de:", limite)

        elif excedeu_saque:
            print("Operação falhou! Número maximo de saques excedido.")
        
        elif valor > 0:
            saldo -= valor
            extrato += f"saque: R$ {valor:.2f}\n"
            numero_saques += 1

        else:
            print("Operação falhou! O valor informado é inválido.")


    

    elif opção =="3":
        print("\n============= EXTRATO =============")
        print("Não foram realizadas movimentações") if not extrato else extrato
        print(f"\nSaldo: R${saldo:.2f}")
        print("=====================================")


    elif opção == "0":
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada ")






























