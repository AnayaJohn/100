class Atm:
    def __init__(self, card_number, pin):
        self.card_number=card_number
        self.pin=pin
        self.balance=5000

    def check_balance(self):
        print("Your Current Balance is ", self.balance)
    
    def withdrawal(self,amount):
        self.balance= self.balance - amount
        print("Your New Balance is $", self.balance)

new_user= Atm("12345", "54321")

print("Choose your option")
print("Press 1 to check your balance and Press 2 for Withdrawal")
option=int(input("Enter your option: "))

if option==1:
    new_user.check_balance()

elif option==2:
    amount=int(input("Enter the amount: "))

    if amount>new_user.balance:
        print("Your withdrawal is higher than your current balance")
    
    else:
        new_user.withdrawal(amount)

else:
    print("Invalid option")

