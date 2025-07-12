from abc import ABC, abstractmethod


class Computer:
    def __init__(self):
        self.ram = None
        self.cpu = None
        self.gpu = None
        self.storage = None
        self.os = None

    def __str__(self):
        return f"Computer: RAM={self.ram}, CPU={self.cpu}, GPU={self.gpu}, Storage={self.storage}, OS={self.os}"
    

class ComputerBuilder(ABC):
    @abstractmethod
    def set_ram(self, ram: str):
        pass

    @abstractmethod
    def set_cpu(self, cpu: str):
        pass

    @abstractmethod
    def set_gpu(self, gpu: str):
        pass

    @abstractmethod
    def set_storage(self, storage: str):
        pass

    @abstractmethod
    def set_os(self, os: str):
        pass

    @abstractmethod
    def get_computer(self) -> Computer:
        pass


class ConcreteComputerBuilder(ComputerBuilder):
    def __init__(self):
        self.computer = Computer()

    def set_ram(self, ram: str):
        self.computer.ram = ram
        return self  # Enables method chaining

    def set_cpu(self, cpu: str):
        self.computer.cpu = cpu
        return self

    def set_gpu(self, gpu: str):
        self.computer.gpu = gpu
        return self

    def set_storage(self, storage: str):
        self.computer.storage = storage
        return self

    def set_os(self, os: str):
        self.computer.os = os
        return self

    def get_computer(self) -> Computer:
        return self.computer


class ComputerDirector:
    def build_gaming_pc(self, builder: ComputerBuilder):
        return (builder
                .set_ram("32GB")
                .set_cpu("Intel i9")
                .set_gpu("RTX 4090")
                .set_storage("2TB SSD")
                .set_os("Windows 11")
                .get_computer())

    def build_office_pc(self, builder: ComputerBuilder):
        return (builder
                .set_ram("16GB")
                .set_cpu("Intel i5")
                .set_storage("512GB SSD")
                .set_os("Ubuntu")
                .get_computer())


# Using Builder directly
builder = ConcreteComputerBuilder()
custom_pc = (builder
             .set_ram("64GB")
             .set_cpu("AMD Ryzen 9")
             .get_computer())
print(custom_pc)

# Using Director
director = ComputerDirector()
gaming_pc = director.build_gaming_pc(ConcreteComputerBuilder())
office_pc = director.build_office_pc(ConcreteComputerBuilder())

print("\nGaming PC:", gaming_pc)
print("Office PC:", office_pc)
