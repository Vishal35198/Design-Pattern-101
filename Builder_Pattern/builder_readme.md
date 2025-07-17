# **Builder Design Pattern in Python**  
*(Next in the Creational Patterns series after Abstract Factory)*  

## **1. What is the Builder Pattern?**  
The **Builder** pattern separates the construction of a complex object from its representation, allowing:  
✅ **Step-by-step construction**  
✅ **Different representations** from the same construction process  
✅ **Immutable objects** when needed  

**Real-world analogy**: Think of building a pizza (crust, sauce, toppings) where the same process can create different pizza types.  

---

## **2. When to Use Builder?**  
- When an object requires **many optional parameters** (avoid telescoping constructors)  
- When you need **different representations** of the same construction process  
- When object creation should be **immutable** after construction  

---

## **3. Classic Implementation Example: Building a Computer**  

### **Problem**  
A `Computer` has:  
- Required: `RAM`, `CPU`  
- Optional: `GPU`, `Storage`, `OS`  

Without Builder, you'd need a constructor with many parameters:  
```python
# ❌ Anti-pattern: Telescoping constructor
computer = Computer("32GB", "Intel i9", "RTX 4090", "2TB SSD", "Windows 11")
```

### **Solution with Builder**  

#### **Step 1: Product Class**  
```python
class Computer:
    def __init__(self):
        self.ram = None
        self.cpu = None
        self.gpu = None
        self.storage = None
        self.os = None

    def __str__(self):
        return f"Computer: RAM={self.ram}, CPU={self.cpu}, GPU={self.gpu}, Storage={self.storage}, OS={self.os}"
```

#### **Step 2: Abstract Builder**  
```python
from abc import ABC, abstractmethod

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
```

#### **Step 3: Concrete Builder**  
```python
class GamingComputerBuilder(ComputerBuilder):
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
```

#### **Step 4: Director (Optional)**  
```python
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
```

#### **Step 5: Client Code**  
```python
# Using Builder directly
builder = GamingComputerBuilder()
custom_pc = (builder
             .set_ram("64GB")
             .set_cpu("AMD Ryzen 9")
             .get_computer())
print(custom_pc)

# Using Director
director = ComputerDirector()
gaming_pc = director.build_gaming_pc(GamingComputerBuilder())
office_pc = director.build_office_pc(GamingComputerBuilder())
print("\nGaming PC:", gaming_pc)
print("Office PC:", office_pc)
```

**Output**:  
```
Computer: RAM=64GB, CPU=AMD Ryzen 9, GPU=None, Storage=None, OS=None

Gaming PC: Computer: RAM=32GB, CPU=Intel i9, GPU=RTX 4090, Storage=2TB SSD, OS=Windows 11
Office PC: Computer: RAM=16GB, CPU=Intel i5, GPU=None, Storage=512GB SSD, OS=Ubuntu
```

---

## **4. Builder Pattern Variations**  
### **Fluent Builder**  
Method chaining (as shown above) for readability:  
```python
builder.set_ram("16GB").set_cpu("i5")...
```

### **Static Inner Builder**  
Useful in Java/C# (less common in Python).  

### **Composite Builder**  
Builds complex object hierarchies.  

---

## **5. Assignment: Pizza Builder**  

### **Task**  
Implement a `PizzaBuilder` to create pizzas with:  
- Required: `size` (S/M/L)  
- Optional: `cheese`, `pepperoni`, `mushrooms`, `onions`  

#### **Requirements**  
1. Create `Pizza` class with attributes.  
2. Create `PizzaBuilder` with fluent interface.  
3. Add a `Director` with pre-defined recipes:  
   - `Margherita`: Medium, Cheese, Onions  
   - `PepperoniFeast`: Large, Cheese, Pepperoni, Mushrooms  
4. Demonstrate building:  
   - A custom pizza (Small, Cheese, Mushrooms)  
   - Both director recipes  

#### **Starter Code**  
```python
class Pizza:
    def __init__(self):
        self.size = None
        self.cheese = False
        self.pepperoni = False
        self.mushrooms = False
        self.onions = False

    def __str__(self):
        return f"Pizza: Size={self.size}, Cheese={self.cheese}, Pepperoni={self.pepperoni}, Mushrooms={self.mushrooms}, Onions={self.onions}"

# Your PizzaBuilder and Director implementation here
```

---

## **Key Takeaways**  
- Builder **simplifies complex object creation**  
- Avoids **telescoping constructors**  
- Enables **immutable objects**  
- **Director** encapsulates construction logic  

Ready to implement the Pizza Builder? 🍕 Let me know if you'd like the solution!