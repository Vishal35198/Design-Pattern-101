
from abc import abstractmethod,ABC

class Coffee(ABC):
    @abstractmethod
    def cost(self) -> float:
        pass

    @abstractmethod
    def description(self) -> str:
        pass
    

# Concrete Objects 
class Espresso(Coffee):
    def cost(self):
        return 1.99

    def description(self):
        return "Espresso"


class Latte(Coffee):
    
    def cost(self):
        return 1.96
    
    def description(self):
        return "Latte"
    
class Capuccino(Coffee):
    
    def cost(self):
        return 2.03
    def description(self):
        return "Capuccino"
    
# Base Decorator 

class CoffeDecorator(Coffee):
    def __init__(self,coffe_decorator : Coffee):
        self._component = coffe_decorator
    
    def cost(self):
        return self._component.cost()
    
    def description(self):
        return self._component.description()
    
# Decorators

class Milk(CoffeDecorator):
    def cost(self):
        return self._component.cost()+0.1
    
    def description(self):
        return f"""
    --------------------------------------
    MILK
    ----------------------------------------
     {self._component.description()} 
    ----------------------------------------
    MILK
    """
    
class Sugar(CoffeDecorator):
    def cost(self):
        return self._component.cost()+0.01
    
    def description(self):
        return f"""
    --------------------------------------
    SUGAR
    ----------------------------------------
     {self._component.description()} 
    ----------------------------------------
    SUGAR
    """
        
if __name__ == "__main__":
    espresso = Espresso()
    latte = Latte()
    # Apply decorators dynamically
    espresso_milk = Milk(espresso)
    latte_milk = Milk(latte) 
    latte_sugar_milk = Sugar(Milk(latte))

    print("Original espresso: ", espresso.description())
    print("Escpresson Milk: ", espresso_milk.description())
    print("Latte Milk : ", latte_milk.description())
    print("Latte Sugar Milk: ", latte_sugar_milk.description())
    