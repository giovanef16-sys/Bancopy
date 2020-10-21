from typing import List
from time import sleep

from models.cliente import Cliente
from models.conta import Conta

contas: List[Conta] = []

def main() -> None:
    menu()


def menu():
    print("===================================")
    print("=============== ATM ===============")
    print("============= Geek Bank ===========")
    print("===================================")
    print('Selecione uma opção do menu: ')
    print('[1] - Criar conta')
    print('[2] - Efetuar saque')
    print('[3] - Efetuar depósito')
    print('[4] - Efetuar transferência')
    print('[5] - Listar contas')
    print('[6] - Sair')

    opcao: int = int(input())

    if opcao == 1:
        criar_conta()

    elif opcao == 2:
        efetuar_saque()

    elif opcao == 3:
        efetuar_deposito()

    elif opcao == 4:
        efetuar_transferencia()
    elif opcao == 5:
        listar_contas()
    elif opcao == 6:
        print("Volte sempre!")
        sleep(2)
        exit(0)
    else:
        print("Opção inválida")
        sleep(2)
        menu()


def criar_conta():
    print("Informe os dados do cliente: ")
    nome: str = input("Nome do cliente: ")
    email: str = input("Email do cliente: ")
    cpf: str = input("Cpf do cliente: ")
    data_nasci: str = input("Data de nascimento: ")

    cliente: Cliente = Cliente(nome, email, cpf, data_nasci)

    conta: Conta = Conta(cliente)
    contas.append(conta)
    print("Conta criada com sucesso!")
    print("Dados da conta: ")
    print("----------------")
    print(conta)
    sleep(2)
    menu()


def efetuar_saque():
    if len(contas) > 0:
        numero: int = int(input("Informe o número da sua conta: "))
        conta: Conta = buscar_conta_por_numero(numero)

        if conta:
            valor: float = float(input("Informe o valor do saque: "))
            conta.sacar(valor)
        else:
            print(f"Não foi encontrada a conta com o número {numero}")

    else:
        print("Ainda não existem contas cadastradas")

    sleep(2)
    menu()

def efetuar_deposito():
    if len(contas) > 0:
        numero: int = int(input("Informe o numero da sua conta: "))
        conta: Conta = buscar_conta_por_numero(numero)

        if conta:
            valor: float = float(input("Informe o valor do depósito: "))
            conta.depositar(valor)
        else:
            print(f"Conta não encontrada a conta {numero}")
    else:
        print("Ainda não existem contas cadastradas.")
    sleep(2)
    menu()

def efetuar_transferencia():
    if len(contas) > 0:
        numero_o: int = int(input("Informe o número da sua conta: "))
        conta_o: Conta = buscar_conta_por_numero(numero_o)

        if conta_o:
            numero_d: int = int(input("Informe o número da conta destino: "))
            conta_d: Conta = buscar_conta_por_numero(numero_d)

            if conta_d:
                valor: float = float(input("Informe o valor da transferência: "))
                conta_o.transferir(conta_d, valor)
            else:
                print(f"A conta destino com número {numero_d} não foi encontrada")

        else:
            print(f"A sua conta com o número {numero_o} não foi encontrada")
    else:
        print("Ainda não existem contas cadastradas")
    sleep(2)
    menu()


def listar_contas():
    if len(contas) > 0:
        print("Listagem de contas")

        for conta in contas:
            print(conta)
            print("-----------")
            sleep(1)
    else:
        print("Não existem contas cadastradas")
    sleep(2)
    menu()


def buscar_conta_por_numero(numero: int) -> Conta:
    c: Conta = None

    if len(contas) > 0:
        for conta in contas:
            if conta.numero == numero:
                c = conta
    return c

if __name__ == '__main__':
    main()

