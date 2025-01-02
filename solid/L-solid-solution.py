from abc import ABC, abstractmethod
class PaymentMethod:
    def __init__(self, balance: float):
        self.balance = balance
    @abstractmethod    
    def transaction(self):
        pass

class PayTransaction(PaymentMethod):
    def __init__(self, amount):
        self.amount= amount
        
    def transaction(self):
        if self.amount > self.balance:
            raise ValueError("Not enough balance.")
        self.balance -= self.amount
        print(f"[PaymentMethod] Paid {self.amount}. New balance: {self.balance}")
    
class RefundTransaction(PaymentMethod):
    def __init__(self, amount):
        self.amount= amount
        
    def transaction(self):
        self.balance += self.amount
        print(f"[PaymentMethod] Refunded {self.amount}. New balance: {self.balance}")
   
class NonRefundableGiftCard(PaymentMethod):
    def transaction(self):
        print("This GiftCard does not support refunds")