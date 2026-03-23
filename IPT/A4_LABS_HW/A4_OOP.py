class Bag:
    category = "Accessory" # Class attribute (shared by all bags)
    # Constructor / init method
    def __init__(self, name, brand, color, material, price, weight_kg, has_zipper):
        self.name = name
        self.brand = brand 
        self.color = color
        self.material = material 
        self.price = price 
        self.weight_kg  = weight_kg 
        self.has_zipper = has_zipper

    def description(self): # Description method
        zipper_info = "with a zipper" if self.has_zipper else "without a zipper"
        return (
            f"[{self.brand}] {self.name} — {self.color} {self.material}, "
            f"${self.price:.2f}, {self.weight_kg}kg, {zipper_info}"
        )

    def is_affordable(self, budget): # Extra instance method
        if self.price <= budget:
            return f"Yehey! The {self.name} by {self.brand} is within your ${budget} budget!"
        else:
            return f"Aww... The {self.name} by {self.brand} exceeds your ${budget} budget."

bag1 = Bag("Satchel", "Louis Vuitton", "Brown", "Leather", 1500.00, 0.4, True)
bag2 = Bag("Backpack", "Guess", "Black", "Vegan Leather", 850.00, 0.5,True)
bag3 = Bag("Crossbody Bag", "Coach", "Red", "Leather",   950.00, 0.4, True)
bag4 = Bag("Clutch", "Gucci", "Gold", "Satin", 890.00, 0.2, True)
bag5 = Bag("Birkin Bag", "Hermes", "Black", "Ostrich Leather", 11160.00, 1.0, False)
bag6 = Bag("Bucket Bag","Prada", "Beige", "Leather",  1200.00, 0.5,False)

#affordable
bag7 = Bag("Sling Bag", "Jansport", "Green", "Polyester", 40.00, 0.3,True)
bag8 = Bag("Messenger Bag", "Herschel", "Gray", "Canvas", 75.00, 0.6, False)
bag9 = Bag("Gym Bag", "Under Armour", "White", "Nylon", 55.00, 0.7, True)
bag10 = Bag("Mini Backpack", "Fjallraven", "Blue", "Canvas", 100.00, 0.4,True)

all_bags = [bag1, bag2, bag3, bag4, bag5, bag6, bag7, bag8, bag9, bag10]

#output
print("=" * 60)
print("                 Category: Accessories")
print("=" * 60)

for bag in all_bags:
    print(bag.description())

print("\nBudget Check (Budget: $100)")
for bag in all_bags:
    print(bag.is_affordable(100))
    
'''
TAWAG: LIM, BAUTISTA, DOMINGO, ARAN, MICIANO
VOLUNTEER: ORATE, ISIDRO
'''
