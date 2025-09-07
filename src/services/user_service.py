from utils.data_handler import load_users, save_user 
from models.farmer import Farmer 
from models.buyer import Buyer 

class UserService:
    @staticmethod 
    def register_user(role, name, phone, location, pin):
        """Register a new Farmer or Buyer and save to file"""
        if role.capitalize() == "Farmer":
            user = Farmer(name, phone, location, pin)
        elif role.capitalize() == "Buyer":
            user = Buyer(name, phone, location, pin)
        else:
            raise ValueError("Role must be 'Farmer' or 'Buyer'")
        
        save_user(user.to_dict())
        return user 
    
    @staticmethod 
    def authenticate(phone, pin):
        """Check if the user exists and if their pin matches"""
        users = load_users()
        for u in users:
            if u["phone"] == phone and u["pin"] == pin:
                if u["role"] == "Farmer":
                    return Farmer(u["name"], u["phone"], u["location"], u["pin"])
                elif u["role"] == "Buyer":
                    return Buyer(u["name"], u["phone"], u["location"], u["pin"])
        return None 
    
    @staticmethod
    def list_users(role):
        """"List all users, according to their role."""
        users = load_users()
        if role:
            return [u for u in users if u["role"].capitalize() == role.capitalize()]
        return users 
