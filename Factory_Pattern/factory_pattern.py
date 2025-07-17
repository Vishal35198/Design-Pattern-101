
#Implement the Factory Method design pattern in Python to create a flexible system for handling different types of payment methods (e.g., Credit Card, PayPal, Bitcoin). #

from abc import ABC,abstractmethod

class PaymentProcessor(ABC):
    """ABC for the PaymentProccessors """
    @abstractmethod
    def process_payment(self,amount: float):
        raise NotImplementedError
    
    @abstractmethod
    def refund_payment(self,amount : float):
        raise NotImplementedError
    
class PaymentProcessorFactory(ABC):
    """ABC for Creating the Objects of the PaymentProccessor"""
    @abstractmethod
    def create_processor(self) -> PaymentProcessor:
        raise NotImplementedError
    
class CreditCardProcessor(PaymentProcessor):
    def __init__(self):
        pass
    
    def process_payment(self,amount):
        print (f"Using Credit Card for the amount {amount}")
    
    def refund_payment(self,amount):
        print(f"Using the credit card for the refund {amount}")
    


    
class CreditCardPaymentFactory(PaymentProcessorFactory):
    
    def __init__(self):
        pass
    
    def create_processor(self) -> PaymentProcessor:
        return CreditCardProcessor()
    
class BankTransferProcessor(PaymentProcessor):
    
    def process_payment(self, amount):
        print("Using the Bank")
        
    def refund_payment(self, amount):
        print("Refund from bank")
        
class BankTransferFactory(PaymentProcessorFactory):
    def create_processor(self):
        return BankTransferProcessor()
    

def client_code(paymentprocessorfactory : PaymentProcessorFactory,amount : float):
    # I am not suppling the PaymentProcessor I am creating its object 
    processor = paymentprocessorfactory.create_processor()
    processor.process_payment(amount)
    


creditcardfactory = CreditCardPaymentFactory()
bankfactory = BankTransferFactory()
client_code(paymentprocessorfactory=bankfactory,amount=200)