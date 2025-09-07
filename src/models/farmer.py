from models.user import User 
import random

class Farmer(User):
    """Farmer class inherits from user"""
    def __init__(self, name, phone, location, pin):
        super().__init__(name, phone, location, pin)
        self.user_id = f"AgF{random.randint(1, 9999)}"

    def get_role(self):
        return "Farmer"
    
    @classmethod 
    def from_dict(cls, data):
        farmer = cls(
            name = data["name"],
            phone = data["phone"],
            location = data["locationi"],
            pin = data["pin"]
        )
        farmer.user_id = data["user_id"]
        return Farmer 
    
