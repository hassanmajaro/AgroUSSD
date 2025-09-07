from models.product import Product 

class Crop(Product):
    """Crop Product"""

    def __init__(self, name, quantity, price, variety, season):
        super().__init__(name, quantity, price)
        self.variety = variety 
        self.season = season 

    def get_type(self):
        return "Crop"
    
    @classmethod 
    def from_dict(cls, data):
        return cls(
            name = data["name"],
            quantity = data["quantity"],
            price = data["price"],
            variety = data.get("variety", ""),
            season = data.get("season", "")
        )
    
    def __str__(self):
        return f"Crop({self.name}, Variety={self.variety}, Season={self.season}, Qty={self.quantity}, Price={self.price})"