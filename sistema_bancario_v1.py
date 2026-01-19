LIMITE_SAQUE = 3
LIMITE_VALOR_SAQUE = 500

def saque(*, saldo, valor, extrato, limite, numero_saques, limite_saques):
    if numero_saques < limite_saques:
        if valor > 0 and valor <= limite:
            if valor <= saldo:
                saldo -= valor
                extrato.append(f'Saque de R$ {valor:.2f}')
                print("Saque realizado com sucesso.")
                return saldo, valor
            else:
                print("Saldo insuficiente.")
                return saldo, valor
        else:
            print("O valor limite de saque foi excedido.")
            return saldo, valor
    else:
        print("O limite de saque diário foi excedido.")
        return saldo, valor


def deposito(saldo, valor, extrato, /):
    if valor > 0:
        saldo += valor
        extrato.append(f"Deposito de R$ {valor:.2f}")
        print("Deposito realizado com sucesso")
        return saldo, valor
    else:
        print("Valor inválido")
        return saldo, valor


def ver_extrato(saldo,/,*, extrato):
    print("\nExtrato da Conta")
    for transacao in extrato:
        print(transacao)
    print(f"\nSaldo: R$ {saldo:.2f}")


def criar_usuario(nome, data_nascimento, cpf, endereco, usuarios):
    if nome and data_nascimento and cpf and endereco:
        novo_usuario = dict(nome=nome, data_nascimento=data_nascimento, cpf=cpf, endereco=endereco)
        usuarios.append(novo_usuario)
        print("Usuário cadastrado com sucesso.")
    else:
        print("Os dados não foram passados corretamente.")


def criar_conta(num_conta, usuario, contas, agencia="0001"):
    if num_conta and usuario:
        contas.append(dict(agencia=agencia, num_conta=num_conta, usuario=usuario, saldo=0))
        print("Conta criada com sucesso.")
    else:
        print("Os dados não foram passados corretamente.")
        

def listar_usuarios(usuarios):
    print("\nLista de Usuários")
    for usuario in usuarios:
        print(f"""
Nome: {usuario['nome']}
Data de nascimento: {usuario['data_nascimento']}
CPF: {usuario['cpf']}
Endereço: {usuario['endereco']}
""")


def listar_contas(contas):
    print("\nLista de Contas")
    for conta in contas:
        print(f"""
Agencia: {conta['agencia']}
Número da Conta: {conta['num_conta']}
Dono da Conta: {conta['usuario']['nome']}
""")
        

def verificar_cpf(cpf, usuarios):
    if [u for u in usuarios if u.get('cpf', '') == cpf]:
        return True
    return False


usuarios = []
contas = []
saldo = 0
extrato = []
num_saques = 0


while True:
    print("""Menu
1 - Sacar
2 - Depositar
3 - Extrator
4 - Criar Usuário
5 - Criar Conta
6 - Listar Usuários
7 - Listar Contas
0 - Sair\n""")
    op = int(input("Digite sua opção: "))
    if op is 1:
        valor = float(input(f'Informe o valor de saque(menor ou igual a R$ {LIMITE_VALOR_SAQUE}): '))
        saldo_retorno, valor_saque = saque(saldo=saldo, valor=valor, extrato=extrato, limite=LIMITE_VALOR_SAQUE, numero_saques=num_saques, limite_saques=LIMITE_SAQUE)
        if saldo_retorno < saldo :
            saldo = saldo_retorno
            num_saques += 1
    elif op is 2:
        valor = float(input('Infomar o valor do deposito: '))
        saldo, valor = deposito(saldo, valor, extrato)
    elif op is 3:
        ver_extrato(saldo, extrato=extrato)
    elif op is 4:
        nome = input("Digite o nome do usuário: ")
        data_nascimento = input("Digite a data de nascimento(dd/mm/yyyy): ")
        cpf = input('Digite o número do CPF: ')
        logradouro = input("Digite o logradouro: ")
        num_casa = input("Digite o número da casa: ")
        bairro = input("Digite o bairro: ")
        cidade = input("Digite o a cidade: ")
        estado = input("Digite o estado(sigla): ")
        if verificar_cpf(cpf, usuarios):
            print("Já existe um usuário com esse CPF.")
        else:
            endereco = f'{logradouro}, {num_casa} - {bairro} - {cidade}/{estado}'
            criar_usuario(nome, data_nascimento, cpf, endereco, usuarios)
            
    elif op is 5:
        cpf = input("Digite o CPF do usuário: ")
        if verificar_cpf(cpf, usuarios):
            usuario = [usuario for usuario in usuarios if usuario.get('cpf') == cpf][0]
            num_conta = len(contas)+1
            criar_conta(num_conta, usuario, contas)
        else:
            print("Não existe nenhum usuário cadastrado com esse CPF.")
    elif op is 6:
        listar_usuarios(usuarios)
    elif op is 7:
        listar_contas(contas)
    elif op is 0:
        break
    else:
        print('Operação inválida, por favor selecione novamente a operação desejada.')
    