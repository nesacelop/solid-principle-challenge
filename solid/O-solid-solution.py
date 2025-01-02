from abc import ABC, abstractmethod

class FeeCalculatorInterface(ABC):
    def __init__(self,amount):
        self.amount = amount

    @abstractmethod
    def calculate_fee(self):
        pass

class CreditCard(FeeCalculatorInterface):
    def calculate_fee(self):
        return self.amount*0.03
class Paypal(FeeCalculatorInterface):
    def calculate_fee(self):
        return self.amount*0.05
class BankTransfer(FeeCalculatorInterface):
    def calculate_fee(self):
        return self.amount*2.50



calculation1 = CreditCard(100)
print(float(calculation1.calculate_fee()))
