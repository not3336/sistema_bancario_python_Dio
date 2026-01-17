saldo = 0
extrato = []
num_saques = 0
LIMITE_SAQUE = 3
LIMITE_VALOR_SAQUE = 500

while True:
    print("""Menu
1 - Sacar
2 - Depositar
3 - Extrator
0 - Sair\n""")
    op = int(input("Digite sua opção: "))
    if op is 1:
        valor = float(input(f'Informe o valor de saque(menor ou igual a R$ {LIMITE_VALOR_SAQUE}): '))
        if num_saques < LIMITE_SAQUE:
            if valor > 0 and valor <= LIMITE_VALOR_SAQUE:
                if saldo >= valor:
                    num_saques += 1
                    saldo -= valor
                    extrato.append(f'Saque de R$ {valor:.2f}')
                    print('Saque realizado com sucesso.\n')
                else:
                    print('Saldo insuficiente\n')
            else:
                print(f'Valor inválido. O valor precisa ser maior que 0 e menor ou igual a R$ {LIMITE_VALOR_SAQUE}\n')
        else:
            print('Limite diario de saque excedido.')
    elif op is 2:
        valor = float(input('Infomar o valor do deposito: '))
        if(valor > 0):
            saldo += valor
            extrato.append(f'Deposito de R$ {valor:.2f}')
            print('Deposito realizado com sucesso\n')
        else:
            print("Valor inválido.\n")
    elif op is 3:
        print('\n\n')
        print('Extrato da conta')
        for operacoes in extrato:
            print(operacoes)
        print(f'\nSaldo: R$ {saldo:.2f}\n')
    elif op is 0:
        break
    else:
        print('Operação inválida, por favor selecione novamente a operação desejada.')
    