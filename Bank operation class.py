class bank:
    def __init__(self,amount,balance):
        self.amount=amount
        self.balance=balance
    def deposit(self):
        self.balance=self.amount+self.balance
        print("\n\t\t\t Amount to Deposits:",self.balance)
    def Withdraw(self):
        self.balance=self.amount-self.balance
        print("\n\t\t\t Amount in Withdraw : ",self.balance)
print("\n\n\n\t\t\t BANK OPERATION USING CLASS ")
print("\t\t\t -------------------------- ")

while True:
    balance1=int(input("\n\t\t\t Amount already in balance :"))
    amt=int(input("\n\t\t\t Amount to Withdraw or deposit: "))
    p1=bank(balance1,amt)
    print("\n\n\t\t\t MENU : ")
    print("\t\t\t ------ ")
    print("\n\t\t\t 1. Deposit \n\t\t\t 2. Withdrawal ")
    ch=input("\n\t\t\t Enter your choice :")
    if ch=="1":
        p1.deposit()
    elif ch=="2":
        p1.Withdraw()
    if input("\n\n\t\t\t Do you want to continue:")!='y':
       break 
   