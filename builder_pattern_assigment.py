from abc import ABC, abstractmethod


class Pizza:
    def __init__(self):
        self.size = None
        self.toppings = []
        self.extra_cheese = None

    def __str__(self):
        return f"Pizza size is {self.size}, toppings are {self.toppings} and chess {self.extra_cheese}"


class PizzaBuilder(ABC):
    @abstractmethod
    def set_size(self, size):
        pass

    @abstractmethod
    def set_toppings(self, toppings):
        pass

    @abstractmethod
    def set_extra_cheese(self, value):
        pass

    @abstractmethod
    def get_pizza(self):
        pass


class ConcretePizzaBuilder(PizzaBuilder):

    def __init__(self):
        self.pizza = Pizza()

    def set_size(self, size):
        self.pizza.size = size
        return self

    def set_toppings(self, toppings):
        self.pizza.toppings.append(toppings)
        return self

    def set_extra_cheese(self, value):
        self.pizza.extra_cheese = value
        return self

    def get_pizza(self) -> Pizza:
        return self.pizza


def client_code(builder: PizzaBuilder):
    pizza = (
        builder.set_size("M")
        .set_toppings("Corn")
        .set_extra_cheese(False)
        .get_pizza())
    print(pizza)


builder = ConcretePizzaBuilder()
client_code(builder)
