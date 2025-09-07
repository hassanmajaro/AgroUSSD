import random 

class Harvest:
    """Harvest links farmer to their products"""

    def __init__(self, farmer_id, product, harvest_date):
        self.harvest_id = f"H{random.randint(1000, 9999)}"
        self.farmer_id = farmer_id 
        self.product = product 
        self.harvest_date = harvest_date 


    def to_dict(self):
        return {
            "harvest_id": self.harvest_id,
            "farmer_id": self.farmer_id,
            "product": {
                "name": self.product.name,
                "quantity":self.product.quantity,
                "price": self.product.price,
                "type": self.product.get_type()
            },
            "harvest_date": self.harvest_date
        }
    
    @classmethod 
    def from_dict(cls, data, product_cls):
        product = product_cls(
            name = data["product"]["name"],
            quantity = data["product"]["quantity"],
            price = data["product"]["price"],
        )

        return cls(data["farmer_id"], product, data["harvest_date"])
    
    def __str__(self):
        return (
            f"Harvest (Farmer = {self.farmer_id}, "
            f"Product = {self.product.name}, "
            f"Qty = {self.product.quantity}, "
            f"Price = {self.product.price}, "
            f"Type = {self.product.get_type()}, "
            f"Date = {self.harvest_date}"
        )