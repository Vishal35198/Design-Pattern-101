from abc import ABC, abstractmethod

# Strategy Pattern Code Copyrights 2025 by Vishal Chaurasiya


class PaymentProcessor(ABC):
    """
    Base Class for all Payment Processors.
    Defines the interface for processing payments.
    """

    @abstractmethod
    def process_payment(self, amount: float) -> str:
        """
        Abstract method to process a payment.
        Must be implemented by concrete payment processor classes.

        Args:
            amount (float): The amount to be processed.

        Returns:
            str: A string indicating the payment processing status or details.
        """
        raise NotImplementedError


class PaytmProcessor(PaymentProcessor):
    """
    A concrete implementation of PaymentProcessor for Paytm services.
    """

    def __init__(self):
        # No specific initialization needed for this simple example,
        # but good to keep if future state is added.
        pass

    def process_payment(self, amount: float) -> str:
        """
        Processes a payment using Paytm services.

        Args:
            amount (float): The amount to be processed.

        Returns:
            str: A message confirming the Paytm payment processing.
        """
        return f"Processing payment via Paytm for {amount:.2f}"


class GooglePayProcessor(PaymentProcessor):
    """
    Another concrete implementation for Google Pay.
    Demonstrates extensibility.
    """

    def process_payment(self, amount: float) -> str:
        """
        Processes a payment using Google Pay services.
        """
        return f"Processing payment via Google Pay for {amount:.2f}"


class PaymentStrategy:
    """
    Strategy to invoke payment processing based on the chosen payment processor.
    This class acts as the context for the Strategy design pattern.
    """

    def __init__(self):
        # In a real-world scenario, you might have a dictionary
        # mapping payment types (e.g., 'paytm', 'googlepay') to processor instances.
        pass

    def initiate_payment(
        self, payment_processor: PaymentProcessor, amount: float
    ) -> str:
        """
        Initiates a payment using the provided payment processor.

        Args:
            payment_processor (PaymentProcessor): An instance of a concrete
                                                  payment processor (e.g., PaytmProcessor).
            amount (float): The amount to be paid.

        Returns:
            str: The result message from the payment processor.
        """
        if not isinstance(payment_processor, PaymentProcessor):
            raise TypeError(
                "payment_processor must be an instance of PaymentProcessor or its subclass."
            )

        return payment_processor.process_payment(amount)


# Client Code

paytm = PaytmProcessor()
gpay = GooglePayProcessor()
payment_strategy = PaymentStrategy()
payment_strategy.initiate_payment(payment_processor=paytm, amount=299)
