    def is_affordable(self, budget):
        if self.price <= budget:
            return f"Yehey! The {self.name} by {self.brand} is within your ${budget} budget!"
        else:
            return f"Aww... The {self.name} by {self.brand} exceeds your ${budget} budget."

bag1 = Bag("Satch