# Bank Account;

class BankAccount:
    def __init__(self, titular, saldo):
        self.titular = titular
        self.saldo = saldo

    def printSaldo(self):
        print(f"Saldo atual: R${self.saldo}")

    def deposit(self, depositValue):
        self.saldo += depositValue
        print(f"R${depositValue} depositados na conta")
        self.printSaldo() 

    def cashout(self, cashoutValue):
        if(cashoutValue > self.saldo):
            print("Valor de saque execede o valor do saldo")
        elif(cashoutValue <= self.saldo):
            self.saldo -= cashoutValue
            print(f"R${cashoutValue} retirados da conta")
            self.printSaldo()

account1 = BankAccount("sergio", 500)
account1.deposit(60)
account1.cashout(500)