# Bank Account;

# Classes
class BankAccount:
    def __init__(self, titular, saldo):
        self.titular = titular
        self.saldo = saldo

    def printSaldo(self):
        print(f"Saldo atual: R${self.saldo}")

    def deposit(self, depositValue):
        self.saldo += depositValue
        print(f"R${depositValue} foram depositados na conta")
        self.printSaldo() 

    def cashout(self, cashoutValue):
        if(cashoutValue > self.saldo):
            print("Valor de saque execede o valor do saldo")
        elif(cashoutValue <= self.saldo):
            self.saldo -= cashoutValue
            print(f"R${cashoutValue} retirados da conta")
            self.printSaldo()

# Funções
def action():
    quit = 0
    while(quit != 'q'):
        opition = input("d - depositar | s - sacar: ")
        if(opition == 'd'):
            depositValue = float(input("Quantidade a ser depositada: "))
            account1.deposit(depositValue)
        elif(opition == 's'):
            cashoutValue = float(input("Quantidade a ser retirada: "))
            account1.cashout(cashoutValue)
        
        quit = input("Sair(q) | Continuar(n): ")

# Main
print("Entre com os dados da conta: ")
titular_nome = input("Nome do titular: ")
entra_saldo = float(input("Saldo na conta: "))

account1 = BankAccount(titular_nome, entra_saldo)

account1.printSaldo()

action()

print("Fechando aplicativo")