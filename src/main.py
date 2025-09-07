from models.farmer import Farmer 
from models.buyer import Buyer 
from utils.data_handler import (save_user, save_harvest, load_users)
from services.user_service import UserService
from models.crop import Crop 
from models.livestock import Livestock 
from models.harvest import Harvest 



def register_user():
    print("===AgroUSSD User Registration===")
    role = input("Enter role (Farmer/Buyer): ").capitalize()
    name = input("Enter name: ").capitalize()
    phone = input("Enter phone: ")
    location = input("Enter location: ").capitalize()
    pin = input("Set a 6-digit PIN: ")

    try:
        user = UserService.register_user(role, name, phone, location, pin)
        print(f"\n{role} created successfully!")
        print(f"User ID: {user.user_id}")
        print(f"Name: {user.name}")
        print(f"Phone: {user.phone}")
        print(f"Location: {user.location}")
        print(f"Role: {user.get_role()}")

        return user 
    
    except ValueError as ve:
        print("Error:", ve)
        return None 
    
def login_user():
    print("\nLogin")
    phone = input("Enter phone: ")
    pin = input("Enter PIN: ")

    users = load_users()
    for u in users:
        if u["phone"] == phone and u["pin"] == pin:
            print(f"\n Welcome back, {u['name']} ({u['role']})")
            if u["role"] == "Farmer":
                option = input("\nDo you want to add harvest? (Yes/No): ").capitalize()
                if option == "Yes":
                    add_harvest(u["user_id"])
            return u
        
    print("Invalid Login Credentials. Try Again")
    return None
    
def add_harvest(farmer_id):
    print("\n===Add Harvest===")
    product_type = input("Enter product type (Crop/Livestock): ").capitalize()

    name = input("Enter product name: ")
    quantity = int(input("Enter quantity: "))
    price = float(input("Enter price: "))

    if product_type == "Crop":
        variety = input("Enter crop variety: ").capitalize()
        season = input("Enter season: ").capitalize()
        product = Crop(name, quantity, price, variety, season)

    elif product_type == "Livestock":
        breed = input("Enter breed: ")
        product = Livestock(name, quantity, price, breed)
    else:
        print("Invalid product type. Must either be Crop or Livestock")
        return None 
    
    harvest_date = input("Enter harvest date (YYYY-MM-DD): ")
    harvest = Harvest(farmer_id, product, harvest_date)

    save_harvest(harvest.to_dict())

    print("\nHarvest added successfully")
    print(harvest)
    return harvest 


def main():
    while True:
        print("\nAgro USSD System")
        print("1. Register")
        print("2. Login")
        print("3. Quit")

        choice = input("Enter choice: ")

        if choice == "1":
            register_user()
        elif choice == "2":
            login_user()
        elif choice == "3":
            print("Thanks for using Agro Service. Goodbye!")
            break 
        else:
            print("Invalid choice. Try again")



if __name__ == "__main__":
    main()