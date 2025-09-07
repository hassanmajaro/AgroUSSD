from models.product import Product 

class Livestock(Product):
    """Livestock inherits from Product"""

    def __init__(self, name, quantity, price, breed):
        super().__init__(name, quantity, price)
        self.breed = breed 

    def get_type(self):
        return "Livestock"
    
    @classmethod 
    def from_dict(cls, data):
        return cls(
            name = data["name"],
            quantity = data["quantity"],
            price = data["price"],
            breed = data.get("breed", "")
        )
    
    def __str__(self):
        return f"Livestock({self.name}, Breed={self.breed}, Qty={self.quantity}, Price={self.price})"