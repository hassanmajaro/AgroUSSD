import json 
from pathlib import Path 

data_dir = Path("data")
data_dir.mkdir(exist_ok=True)

user_file = data_dir / "users.json"
harvest_file = data_dir / "harvests.json"

def load_data(file_path):
    if not file_path.exists():
        return []
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            return json.load(f)
    except json.JSONDecodeError:
        return []
    
def save_data(file_path, data):
    with open(file_path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=5)

#users
def load_users():
    return load_data(user_file)

def save_user(user_dict):
    users = load_users()
    users.append(user_dict)
    save_data(user_file, users)

def login_user(name, password, role):
    """Check if user exists with correct role."""
    users = load_users()
    for user in users:
        if user["name"] == name and user["password"] == password and user["role"] == role:
            return True 
        return False


#harvests
def load_harvests():
    return load_data(harvest_file)

def save_harvest(harvest_dict):
    harvests = load_harvests()

    updated = False 
    for h in harvests:
        if h["farmer_id"] == harvest_dict["farmer_id"] and h["product"]["name"].capitalize() == harvest_dict["product"]["name"].capitalize():
            h["product"]["quantity"] += harvest_dict["product"]["quantity"]
            updated = True 
            break 

    if not updated:
        harvests.append(harvest_dict)

    with open(harvest_file, "w", encoding="utf-8") as f:
        json.dump(harvests, f, indent=5)