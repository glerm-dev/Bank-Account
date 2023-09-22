# Bank Account;

from bank_account import *

# Funções
def action(a1, a2):
    while(True):
        opition = input("d - depositar | s - sacar: | t - transferir: ")
        if(opition == 'd'):
            depositValue = float(input("Quantidade a ser depositada: "))
            a1.deposit(depositValue)
        elif(opition == 's'):
            cashoutValue = float(input("Quantidade a ser retirada: "))
            a1.cashout(cashoutValue)
        elif(opition == 't'):
            transfer_value = float(input("Quantidade a ser transferida para outra conta: "))
            a1.cashout(transfer_value)
            a2.deposit(transfer_value)
        
        quit = input("Sair(s) | Continuar(c): ")
        if(quit == 's'):
            break

# Main
def main():

    print("Entre com os dados das contas: ")
    titular_nome = input("Nome do titular: ")
    entra_saldo = float(input("Saldo na conta: "))

    account1 = BankAccount(titular_nome, entra_saldo)
    account1.printSaldo()

    titular_nome = input("Nome do titular: ")
    entra_saldo = float(input("Saldo na conta: "))

    account2 = BankAccount(titular_nome, entra_saldo)
    account2.printSaldo()

    action(account1, account2)

    print("\n")
    account1.history()
    account2.history()
    print("\n")
    print("Fechando aplicativo")

    
main()