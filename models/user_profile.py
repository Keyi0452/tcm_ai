class UserProfile:
    def __init__(self):
        self.user_id = None
        self.age = None
        self.gender = None
        self.location = None
        self.main_constitution = None
        self.secondary_constitution = None
        self.health_goals = []
        self.allergies = []
        self.preferences = {
            "exercise_preference": [],
            "food_preference": [],
            "tea_preference": []
        }
        self.seasonal_info = {
            "current_season": None,
            "local_climate": None
        }