from models.user import User
import random

class Buyer(User):
    """Buyer class inherits from User"""
    def __init__(self, name, phone, location, pin):
        super().__init__(name, phone, location, pin)
        self.user_id = f"AgB{random.randint(1, 9999)}"

    def get_role(self): 
        return "Buyer"
    
    @classmethod 
    def from_dict(cls, data):
        buyer = cls(
            name = data["name"],
            phone = data["phone"],
            location = data["locationi"],
            pin = data["pin"]
        )
        buyer.user_id = data["user_id"]
        return buyer