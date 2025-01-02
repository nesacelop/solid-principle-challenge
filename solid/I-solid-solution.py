from abc import ABC, abstractmethod

class IPay(ABC):
    @abstractmethod
    def pay(self, amount: float) -> None:
        pass
    
class IRefund(ABC):
    @abstractmethod
    def refund(self, amount: float) -> None:
        pass

class IDispute(ABC):
    @abstractmethod
    def handle_dispute(self, dispute_id: str) -> None:
        pass
    
class BasicGiftCard(IPay):
    def pay(self, amount: float) -> None:
        print(f"Gift card used to pay {amount}.")
        
class RefundGC(IRefund):
    def refund(self, amount: float) -> None:
        print("Gift cards do not support refunds.")
 
class DisputeGiftCard(IDispute):
    def handle_dispute(self, dispute_id: str) -> None:
        print(f"Gift cards with dispute id {dispute_id} do not be supported")