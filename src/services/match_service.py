from utils.data_handler import load_users, load_harvests

class MatchService:
    @staticmethod
    def match_harvest_to_buyer(product_type = None, product_name = None):
        """Return harvest that match buyer's search"""
        harvests = load_harvests()
        users = load_users()

        # filter harvests 
        matches = []
        for h in harvests:
            if product_type and h["product"]["type"].capitalize() != product_type.capitalize():
                continue 
            if product_name and h["product"]["name"].capitalize() != product_name.capitalize():
                continue 

            # Get farmer's information for the harvest
            farmer = next((u for u in users if u["user_id"] == h["farmer_id"]), None)
            if farmer:
                matches.append({
                    "harvest": h,
                    "farmer": farmer
                })
        return matches