
from abc import ABC, abstractmethod

class Cname(ABC):
    @abstractmethod
    def mname(self):
        pass


class Cname1(Cname):
    def mname(self):
        print("Method implemented in Cname1")


class ATM(ABC):

    @abstractmethod
    def check_bal(self):
        pass

    @abstractmethod
    def deposit(self):
        pass

    @abstractmethod
    def withdraw(self):
        pass


class ATM_SBI(ATM):

    def __init__(self, name, pin):
        self.name = name
        self.pin = pin
        self.bal = 2000

    def check_bal(self):
        pin = int(input("Enter pin: "))
        if pin == self.pin:
            print(f"Available balance: Rs. {self.bal}")
        else:
            print("Invalid PIN")

    def deposit(self):
        pin = int(input("Enter pin: "))
        if pin == self.pin:
            amount = int(input("Enter amount to deposit: "))
            self.bal += amount
            print("Amount deposited successfully")
            print(f"Updated balance: Rs. {self.bal}")
        else:
            print("Invalid PIN")

    def withdraw(self):
        pin = int(input("Enter pin: "))
        if pin == self.pin:
            amount = int(input("Enter amount to withdraw: "))
            if amount <= self.bal:
                self.bal -= amount
                print("Please collect your cash")
                print(f"Remaining balance: Rs. {self.bal}")
            else:
                print("Insufficient balance")
        else:
            print("Invalid PIN")


user1 = ATM_SBI("devi", 1234)

user1.check_bal()
user1.deposit()
user1.withdraw()