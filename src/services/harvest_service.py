from utils.data_handler import save_harvest, load_harvests 
from models.harvest import Harvest 
from models.crop import Crop 
from models.livestock import Livestock 


class HarvestService:
    @staticmethod 
    def add_harvest(farmer_id, product_type, name, quantity, price, extra_info, harvest_date):
        """Create and save a new harvest for a farmer."""

        if product_type.capitalize() == "Crop":
            product = Crop(name, quantity, price, extra_info["variety"], extra_info["season"])
        elif product_type.capitalize() == "Livestock":
            product = Livestock(name, quantity, price, extra_info["variety"])
        else:
            raise ValueError("Invalid product type: must be Crop or Livestock")
        
        harvest = Harvest(farmer_id, product, harvest_date)
        save_harvest(harvest.to_dict())
        return harvest 
    
    @staticmethod 
    def list_farmer_harvest(farmer_id):
        """List all harvests for a specific farmer."""
        harvests = load_harvests()
        return [h for h in harvests if h["farmer_id"] == farmer_id]
    
    @staticmethod 
    def list_all_harvests():
        """Return all harvests in the system (for buyers or admin)"""
        return load_harvests()

    @staticmethod 
    def filter_harvests(product_type = None, crop = None, livestock = None):
        harvests = load_harvests()
        filtered = harvests

        if product_type:
            filtered = [h for h in filtered if h["product_type"].capitalize() == product_type.capitalize()]

        if crop:
            filtered = [h for h in filtered if h.get("crop", "").capitalize() == crop.capitalize()]

        if livestock:
            filtered = [h for h in filtered if h.get("livestock", "").capitalize() == livestock.capitalize()]
        
        return filtered