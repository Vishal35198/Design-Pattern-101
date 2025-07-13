from abc import ABC, abstractmethod
from typing import List, Dict
from enum import Enum


class SubscriptionModel(Enum):
    """Subscription Model for the User """
    FREE = 1
    PAID = 2

# (Investor and Stock classes remain the same as in your original code)
class Investor(ABC):
    """
    Summary
    	This is an abstract method update which is part of the Investor class, it is intended to be implemented by subclasses to update the investor's state based on the given price, the method does not have a return value and is expected to be overridden in any concrete subclass of Investor
    Arguments
    	price: float or int: the current price that the investor's state should be updated with
    Returns
    	None: this method does not return any value, its purpose is to update the investor's state in-place
    """
    @abstractmethod
    def update(self, price):
        raise NotImplementedError
    


class Stock: 
    """
    Summary
    	This class represents a Stock with its symbol, price, and a list of investors. It provides methods to add, remove, and notify investors when the stock price is updated.
    Arguments
    	symbol (str): the symbol of the stock
    	investor (Investor): the investor to be added or removed
    	price (float): the new price of the stock
    Returns
    	None: the class methods do not return any value, they modify the object state or notify investors
    """
    def __init__(self, symbol):
        self._symbol = symbol
        self._price = 0.0
        self._investors: List[Investor] = []
    
    def add_investors(self, investor: Investor):
        if isinstance(investor, Investor):
            self._investors.append(investor)
        
    def remove_investor(self, investor: Investor):
        if isinstance(investor, Investor):
            self._investors.remove(investor)
        
    def notify_investor(self):
        for investor in self._investors:
            investor.update(self._price)
            
    def update_price(self, price):
        self._price = price
        self.notify_investor()

class RupayStocksAPI(Investor):
    """
    Summary
    	This class represents a Rupay Stocks API, which is a subclass of Investor. It is used to track and update stock prices, and calculate the average price. The class has an initializer method to set up an empty list to store prices, and an update method to add new prices to the list and print the current and average prices.
    Arguments
    	price (float): the new price to be added to the list
    Returns
    	None: the function does not return any value, it prints the current and average prices instead
    """
    def __init__(self):
        self._prices = []
        
    def update(self, price):
        self._prices.append(price)
        print(f"Current Price upgraded {price} for and average price is {sum(self._prices)/len(self._prices)} {self.__class__.__name__}")
        
class GrowStocksAPI(Investor):
    def __init__(self):
        self._prices = []
        
    def update(self, price):
        self._prices.append(price)
        print(f"Current Price upgraded for stock {price} for and average price is {sum(self._prices)/len(self._prices)} {self.__class__.__name__}")

class FivePaisa(Investor):
    def __init__(self):
        self._prices = []
        
    def update(self, price):
        """AI is creating summary for update

        Args:
            price ([type]): [description]
        """
        self._prices.append(price)
        print(f"Current Price upgraded {price} for and average price is {sum(self._prices)/len(self._prices)} {self.__class__.__name__}")
        

class StockManager:
    def __init__(self):
        self._stocks: Dict[str, Stock] = {}
        self._default_investors: List[Investor] = []

    def register_default_investor(self, investor: Investor):
        self._default_investors.append(investor)

    def create_stock(self, symbol: str) -> Stock:
        if symbol in self._stocks:
            print(f"Stock with symbol {symbol} already exists. Returning existing instance.")
            return self._stocks[symbol]
        
        stock = Stock(symbol)
        for investor in self._default_investors:
            stock.add_investors(investor)
        self._stocks[symbol] = stock
        return stock

    def get_stock(self, symbol: str) -> Stock:
        if symbol not in self._stocks:
            raise KeyError(f"Stock with symbol '{symbol}' does not exist.")
        return self._stocks[symbol]

    def add_investor_to_all_stocks(self, investor: Investor):
        for stock in self._stocks.values():
            stock.add_investors(investor)

if __name__ == '__main__':
    stock_manager = StockManager()

    # Register default investors with the manager
    stock_manager.register_default_investor(GrowStocksAPI())
    stock_manager.register_default_investor(FivePaisa())

    # Create stocks using the manager, which automatically adds default investors
    apple_stock = stock_manager.create_stock("APPLE")
    google_stock = stock_manager.create_stock("GOOGL")
    
    print("\n--- Apple Stock Updates ---")
    apple_stock.update_price(200.0)
    apple_stock.update_price(300.0)
    
    print("\n--- Google Stock Updates ---")
    google_stock.update_price(1500.0)
    google_stock.update_price(1550.0)

    # Add a new investor and apply it to all *existing* stocks
    rupay_api = RupayStocksAPI()
    stock_manager.add_investor_to_all_stocks(rupay_api)
    
    print("\n--- Apple Stock Updates (after adding Rupay to all) ---")
    apple_stock.update_price(450.0) # Rupay will now also be notified

    print("\n--- Google Stock Updates (after adding Rupay to all) ---")
    google_stock.update_price(1600.0) # Rupay will now also be notified

    # Create a new stock after Rupay was added to all
    tesla_stock = stock_manager.create_stock("TSLA") # Tesla will also get Grow, FivePaisa and Rupay
    print("\n--- Tesla Stock Updates ---")
    tesla_stock.update_price(800.0)