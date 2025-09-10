from models.farmer import Farmer 
from models.buyer import Buyer 
from utils.data_handler import (save_user, save_harvest, load_users)
from services.user_service import UserService
from models.crop import Crop 
from models.livestock import Livestock 
from models.harvest import Harvest 
from services.harvest_service import HarvestService



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

            elif u["role"] == "Buyer":
                print("Buyer Menu")           
                print("1. View all harvests")
                print("2. Filter harvests")
                choice = input("Choose option (1/2): ")

                if choice == "1":
                    print("\nAvailable Harvests")
                    harvests = HarvestService.list_all_harvests()
                    if harvests:
                        for h in harvests:
                            print(h)
                    else:
                        print("No harvests available at the moment.")

                elif choice == "2":
                    print("\n Filter Harvests")
                    p_type = input("Enter producty type to filter (Crop/Livestock): ")
                    crop = None
                    livestock = None 

                    if p_type.capitalize() == "Crop":
                        crop = input("Enter crop name to filter: ").capitalize()
                    elif p_type.capitalize() == "Livestock":
                        livestock = input("Enter livestock type to filter: ").capitalize()

                    results = HarvestService.filter_harvests(
                        product_type = p_type if p_type else None,
                        crop = crop if crop else None,
                        livestock = livestock if livestock else None
                    )

                    if results:
                        print("Filtered Harvests")
                        for r in results:
                            print(r)
                    else:
                        print("No harvests match your filter")

            return print("Invalid credentials. Please Try again")
        
    print("Invalid Login Credentials. Try Again")
    return None
    
def add_harvest(farmer_id):
    print("Add harvest")

    product_type = input("Enter product type (Crop/Livestock): ").capitalize()
    name = input("Enter product name: ").capitalize()
    quantity = int(input("Enter quantity: "))
    price = float(input("Enter price: "))

    extra_info = {}
    if product_type == "Crop":
        extra_info["variety"] = input("Enter crop variety: ").capitalize()
        extra_info["variety"] = input("Enter season: ").capitalize()
    elif product_type == "Livestock":
        extra_info["variety"] = input("Enter livestock breed: ").capitalize()
    else:
        print("Invalid product type. Must be crop or Livestock")
        return None 

    harvest_date = input("Enter harvest date (YYYY-MM-DD): ")

    #use service
    harvest = HarvestService.add_harvest(farmer_id, product_type, name, quantity, price, extra_info, harvest_date)
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