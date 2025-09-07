from abc import ABC, abstractmethod 

class Product(ABC):
    """Abstract Product Class. All products inherits from this"""

    def __init__(self, name, quantity, price):
        self.name = name
        self.quantity = quantity 
        self.price = price 

    @abstractmethod 
    def get_type(self):
        return {
            "name": self.name,
            "quantity": self.quantity, 
            "price": self.price,
            "type": self.get_type()
        }
    
    @classmethod 
    def from_dict(cls, data):
        pass 

    def __str__(self):
        return f"{self.get_type()}({self.name}, Qty={self.quantity}, Price={self.price})"