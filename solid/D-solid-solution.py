from abc import ABC, abstractmethod

class PayInterface(ABC):
    @abstractmethod
    def pay(self,amount: float):
        pass

class PayPalService(PayInterface):   
    def pay(self, amount: float):
        print(f"Paying {amount} using PayPal...")


class PaymentProcessor:
    def __init__(self,paypal_service: PayInterface):
        self.paypal_service = paypal_service

    def process_payment(self, amount: float):
        self.paypal_service.pay(amount)
        
paypal_service = PayPalService()
processor = PaymentProcessor(paypal_service)
processor.process_payment(150.0)