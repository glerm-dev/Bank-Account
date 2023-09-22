# Bank Account;

from bank_account import *

# Funções
def action(account1):
    while(True):
        opition = input("d - depositar | s - sacar: ")
        if(opition == 'd'):
            depositValue = float(input("Quantidade a ser depositada: "))
            account1.deposit(depositValue)
        elif(opition == 's'):
            cashoutValue = float(input("Quantidade a ser retirada: "))
            account1.cashout(cashoutValue)
        
        quit = input("Sair(q) | Continuar(n): ")
        if(quit == 'q'):
            break

# Main
def main():

    print("Entre com os dados da conta: ")
    titular_nome = input("Nome do titular: ")
    entra_saldo = float(input("Saldo na conta: "))

    account1 = BankAccount(titular_nome, entra_saldo)
    account1.printSaldo()

    action(account1)
    
    print("\n")
    account1.history()
    print("\n")
    print("Fechando aplicativo")

main()