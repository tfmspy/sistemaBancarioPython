menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """

saldo = 0.00
limite = 500.00
numero_saques = 0
LIMITE_SAQUES = 3

valor_saque = 0.00
valor_deposito = 0.00
saques = []
depositos = []

def depositar():
    
    global saldo, depositos

    valor_deposito = float(input("Valor que deseja depositar: "))

    if valor_deposito > 0 :
        saldo = saldo + valor_deposito

        depositos.append(valor_deposito)

        print(f"Depósito de R$ {valor_deposito:.2f} realizado com sucesso.")

    else:
        print("O valor do depósito deve ser maior que zero.")

def sacar():

    global saldo, saques, numero_saques
    
    if numero_saques < LIMITE_SAQUES:

        valor_saque = float(input("Valor que deseja sacar: "))

        if valor_saque > 0 and valor_saque <= limite:
            if valor_saque <= saldo:
                saldo -= valor_saque
                numero_saques += 1

                saques.append(valor_saque)
                
                print(f"Saque de R$ {valor_saque:.2f} realizado com sucesso.")
                print(f"Seu saldo atual é de R$ {saldo:.2f}.")

            else:
                print("Você não tem saldo para realizar esse saque.")

        else:
            print("O valor do saque deve ser maior que zero e menor ou igual ao Saldo.")

    else:
        print("Quantidade de saques excedida.")

def extrato():


    print(f"Seu saldo atual é de R$ {saldo:.2f}.")

    if saques:
        print("Saques realizados: ")
        for i, valor_saque in enumerate(saques, 1):
            print(f"{i} - R$ {valor_saque:.2f}")

    if depositos:
        print("Depósitos realizados: ")
        for i, valor_deposito in enumerate(depositos, 1):
            print(f"{i} - R$ {valor_deposito:.2f}")

while True:  

    opcao = input(menu)

    if  opcao == "d":
        print("Depósito")
        depositar()

    elif opcao == "s":
        print("Saque")
        sacar()

    elif opcao == "e":
        print("Extrato")
        extrato()

    elif opcao == "q":
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")



    

    
    