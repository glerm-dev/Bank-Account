class BankAccount:
    def __init__(self, titular, saldo):
        self.titular = titular
        self.saldo = saldo
        self.extrato = []

    def printSaldo(self):
        print(f"Saldo atual: R${self.saldo}")

    def deposit(self, depositValue):
        self.extrato.append("+R$ " + str(depositValue) + " depositado")

        self.saldo += depositValue
        print(f"+R${depositValue} foram depositados na conta")
        self.printSaldo() 

    def cashout(self, cashoutValue):
        tax = 0.05
        
        if(cashoutValue > self.saldo):
            print("Valor de saque execede o valor do saldo")
        elif(cashoutValue <= self.saldo):
            if(cashoutValue > 500):
                self.extrato.append("-R$ " + str(cashoutValue * tax) + " retirado")
                self.saldo -= cashoutValue + (cashoutValue * tax)
                print(f"-R${cashoutValue}, -R${cashoutValue * tax} de taxa retirados da conta")
                self.printSaldo()
            else:
                self.extrato.append("-R$ " + str(cashoutValue) + " retirado")
                self.saldo -= cashoutValue 
                print(f"-R${cashoutValue} retirados da conta")
                self.printSaldo()

    def transfer(self, transfer_value, target_account):
        self.saldo -= transfer_value
        target_account.deposit(transfer_value)
        print("Transferência realizada")
        self.extrato.append("-R$ " + str(transfer_value) + ' transferidos')

    def history(self):
        print(f"Historico da conta - {self.titular}: ")
        for i in self.extrato:
            print(i)
