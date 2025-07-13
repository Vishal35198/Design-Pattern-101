# **Singleton Design Pattern in Python**  
*(Next in the Creational Patterns series after Builder)*  

## **1. What is the Singleton Pattern?**  
The **Singleton** pattern ensures that a class has **only one instance** and provides a **global access point** to it.  

✅ **Use Cases**:  
- Database connections  
- Logging systems  
- Configuration managers  
- Hardware interface access  

---

## **2. Key Characteristics**  
- **Private constructor**: Prevents direct instantiation.  
- **Static instance access**: Provides a global access method (e.g., `get_instance()`).  
- **Thread safety** (in multi-threaded environments).  

---

## **3. Classic Python Implementation**  

### **Method 1: Base Implementation**  
```python
class Singleton:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.init_singleton()
        return cls._instance

    def init_singleton(self):
        """Initialize singleton resources."""
        self.value = "Initialized"

# Usage
s1 = Singleton()
s2 = Singleton()
print(s1 is s2)  # Output: True
```

### **Method 2: Decorator (Pythonic Approach)**  
```python
def singleton(cls):
    instances = {}
    def wrapper(*args, **kwargs):
        if cls not in instances:
            instances[cls] = cls(*args, **kwargs)
        return instances[cls]
    return wrapper

@singleton
class Logger:
    def __init__(self):
        self.log_file = "app.log"

# Usage
logger1 = Logger()
logger2 = Logger()
print(logger1 is logger2)  # Output: True
```

### **Method 3: Metaclass (Advanced)**  
```python
class SingletonMeta(type):
    _instances = {}
    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super().__call__(*args, **kwargs)
        return cls._instances[cls]

class Database(metaclass=SingletonMeta):
    def __init__(self):
        self.connection = "Established"

# Usage
db1 = Database()
db2 = Database()
print(db1 is db2)  # Output: True
```

---

## **4. Thread-Safe Singleton (For Multi-Threading)**  
```python
from threading import Lock

class ThreadSafeSingleton:
    _instance = None
    _lock = Lock()

    def __new__(cls):
        with cls._lock:
            if cls._instance is None:
                cls._instance = super().__new__(cls)
        return cls._instance

# Usage
singleton = ThreadSafeSingleton()
```

---

## **5. Assignment: Global Configuration Manager**  

### **Task**  
Implement a **thread-safe** `ConfigManager` singleton that:  
1. Loads configuration from a JSON file (`config.json`) on first access.  
2. Provides read-only access to settings.  
3. Logs warnings if the config file is missing.  

#### **Requirements**  
1. Use **any Singleton implementation method** (decorator/metaclass/`__new__`).  
2. Add thread safety if using `__new__`.  
3. Handle missing config files gracefully.  

#### **Starter Code**  
```python
import json
import logging

class ConfigManager:
    # Your implementation here
    pass

# Test Cases
def test_config_manager():
    config1 = ConfigManager()
    config2 = ConfigManager()
    assert config1 is config2
    print("ConfigManager test passed!")

test_config_manager()
```

#### **Example `config.json`**  
```json
{
    "app_name": "SingletonDemo",
    "debug_mode": false,
    "max_connections": 10
}
```

---

## **6. Key Takeaways**  
- **Pros**:  
  - Controlled access to a single instance.  
  - Lazy initialization (creates instance only when needed).  
- **Cons**:  
  - Can introduce global state (use judiciously).  
  - Hard to unit test (mocking becomes challenging).  

---

## **Bonus Challenges**  
1. **Add Hot Reloading**: Watch the config file for changes and reload automatically.  
2. **Multi-Instance Variant**: Extend to allow a fixed number of instances (e.g., connection pool).  

Ready to implement? 🚀 Let me know if you'd like the solution or a deeper dive into thread safety!