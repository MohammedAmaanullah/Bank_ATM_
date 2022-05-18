class Atm():
    def __init__(self,card_number,pin_number):
        self.card_number=card_number
        self.pin_number=pin_number

    def EnterPin_Number(self):
        input("Enter your pin: ")

    def SelectAccountType():
        account= input("Choose either 'savings' or 'current': ")
        print("You have selected: "+account)

    def CashWithdrawl(self):
        amount=input("Enter how much cash you want to withdraw: ")
        print("You have withdrawed:"+amount)
    

    def BalanceEnquiry(self):
        print("You have $100000 in your account")

sbi=Atm("1234","5678")
print(sbi.card_number)
print(sbi.CashWithdrawl())