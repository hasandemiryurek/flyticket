class Account:
    country = "TR"
    def __init__(self, pw, iban, amount=0):
        self.password = pw
        self.iban = iban
        self.accountNo = iban[-5:]
        self.amount = amount

    def __str__(self):
        return self.accountNo + " " + str(self.amount)

    def depositAmount(self, depositedAmount):
        self.amount += depositedAmount
        return self.amount

    def withdrawAmount(self, withdrawnAmount):
        if self.amount >= withdrawnAmount:
            self.amount -= withdrawnAmount
            return self.amount
        else:
            return -1

class Customer:
    def __init__(self, name, tcNo, phoneNumber):
        self.name = name
        self.tcNo = tcNo
        self.phoneNumber = phoneNumber
        self.accounts = []

    def addAccount(self, account):
        self.accounts.append(account)

    def closeAccount(self, accountNo):
        for i in range(len(self.accounts)):
            if self.accounts[i].accountNo == accountNo:
                del self.accounts[i]
                return True
        return False

class Bank:
    def __init__(self, name):
        self.name = name
        self.customers = []

    def addCustomer(self, customer):
        self.customers.append(customer)

    def getTotalAsset(self):
        total = 0
        for c in self.customers:
            for a in c.accounts:
                total += a.amount
        return total


b = Bank("BarisBank")

c = Customer("Tugba Suzek", "1", "1")
c.addAccount(Account("1", "1", 100))
b.addCustomer(c)


c = Customer("Baris Suzek", "1", "1")
c.addAccount(Account("1", "1", 10))
c.addAccount(Account("1", "1", 100))
b.addCustomer(c)


print(b.name)
print(c.accounts[0])
print(b.getTotalAsset())