#Inheritance: 
'''
Attributes are defined in constructor method.
- Has parent class
'''
# ============================================================
# PARENT CLASS — contains shared attributes and methods
# that ALL bags have in common
# ============================================================
class Bag:
    category = "Accessory"  # Class attribute (shared by all bags)

    #constructor, defines attributes
    def __init__(self, name, brand, color, material, price, weight_kg, has_zipper):
        self.name = name
        self.brand = brand #attributes
        self.color = color
        self.material = material
        self.price = price
        self.weight_kg = weight_kg
        self.has_zipper = has_zipper

    #BEHAVIORS
    def description(self): #instance method
        zipper_info = "with a zipper" if self.has_zipper else "without a zipper"
        return (
            f"[{self.brand}] {self.name} — {self.color} {self.material}, "
            f"${self.price:.2f}, {self.weight_kg}kg, {zipper_info}"
        )

    def is_affordable(self, budget):
        if self.price <= budget:
            return f"Yehey! The {self.name} by {self.brand} is within your ${budget} budget!"
        else:
            return f"Aww... The {self.name} by {self.brand} exceeds your ${budget} budget."


# ============================================================
# CHILD CLASS 1 — LuxuryBag inherits from Bag
# It gets all of Bag's attributes and methods, but adds its own:
#   - extra attribute: limited_edition
#   - overrides: description() to add a luxury label
#   - new method:  authenticity_note()
# ============================================================
class LuxuryBag(Bag):  # <-- "LuxuryBag IS-A Bag" (inheritance)

    def __init__(self, name, brand, color, material, price, weight_kg, has_zipper, limited_edition=False):
        # super().__init__() calls the PARENT's constructor so we don't repeat ourselves
        super().__init__(name, brand, color, material, price, weight_kg, has_zipper)
        self.limited_edition = limited_edition  # extra attribute only luxury bags have

    # METHOD OVERRIDING — replaces the parent's description() with a fancier version
    def description(self):
        base = super().description()  # reuse the parent's description text
        edition = " [Limited Edition]" if self.limited_edition else ""
        return f"✨ LUXURY{edition} | {base}"

    # NEW METHOD — only exists in LuxuryBag, not in the parent Bag
    def authenticity_note(self):
        return f"The {self.name} by {self.brand} comes with a certificate of authenticity."


# ============================================================
# CHILD CLASS 2 — AffordableBag inherits from Bag
# It also gets everything from Bag, but adds its own twist:
#   - overrides: description() to add a budget-friendly label
#   - new method:  value_rating() unique to affordable bags
# ============================================================
class AffordableBag(Bag):  # <-- "AffordableBag IS-A Bag" (inheritance)

    def __init__(self, name, brand, color, material, price, weight_kg, has_zipper):
        super().__init__(name, brand, color, material, price, weight_kg, has_zipper)

    # METHOD OVERRIDING — adds a budget label to the parent's description
    def description(self):
        base = super().description()  # still reuses parent logic
        return f"💰 BUDGET-FRIENDLY | {base}"

    # NEW METHOD — calculates a simple value-for-money score
                    #object reference
    def value_rating(self):
        score = round(10 - (self.price / 20), 1)  # cheaper = higher score
        score = max(0, min(score, 10))             # clamp between 0 and 10
        return f"Value Rating for {self.name}: {score}/10"


# ============================================================
# OBJECTS — now using the appropriate child class
# LuxuryBag and AffordableBag both inherited description() and
# is_affordable() from Bag, but override description() their own way
# ============================================================

# LuxuryBag instances (some marked as limited edition)
# references the child - instantiation
#instantiate the method
bag1 = LuxuryBag("Satchel",      "Louis Vuitton", "Brown", "Leather",         1500.00, 0.4, True)
bag2 = LuxuryBag("Backpack",     "Guess",         "Black", "Vegan Leather",    850.00, 0.5, True)
bag3 = LuxuryBag("Crossbody Bag","Coach",         "Red",   "Leather",          950.00, 0.4, True)
bag4 = LuxuryBag("Clutch",       "Gucci",         "Gold",  "Satin",            890.00, 0.2, True)
bag5 = LuxuryBag("Birkin Bag",   "Hermes",        "Black", "Ostrich Leather", 11160.00, 1.0, False, limited_edition=True)
bag6 = LuxuryBag("Bucket Bag",   "Prada",         "Beige", "Leather",         1200.00, 0.5, False)

# AffordableBag instances
bag7  = AffordableBag("Sling Bag",      "Jansport",    "Green", "Polyester",  40.00, 0.3, True)
bag8  = AffordableBag("Messenger Bag",  "Herschel",    "Gray",  "Canvas",     75.00, 0.6, False)
bag9  = AffordableBag("Gym Bag",        "Under Armour","White", "Nylon",      55.00, 0.7, True)
bag10 = AffordableBag("Mini Backpack",  "Fjallraven",  "Blue",  "Canvas",    100.00, 0.4, True)

luxury_bags   = [bag1, bag2, bag3, bag4, bag5, bag6]
affordable_bags = [bag7, bag8, bag9, bag10]
all_bags = luxury_bags + affordable_bags


# ============================================================
# OUTPUT
# ============================================================
print("=" * 65)
print("              Category: Accessories")
print("=" * 65)

print("\n--- All Bags (description inherited + overridden) ---")
for bag in all_bags:
    #instance method
    #defines behavior
                        #no parameter
    print(bag.description())  # each class runs its OWN version of description()

print("\n--- Authenticity Notes (LuxuryBag-only method) ---")
for bag in luxury_bags:
    #obejct then method
    print(bag.authenticity_note())  # only LuxuryBag has this

print("\n--- Value Ratings (AffordableBag-only method) ---")
for bag in affordable_bags:
    print(bag.value_rating())  # only AffordableBag has this

print("\n--- Budget Check (Budget: $100) --- inherited from Bag ---")
for bag in all_bags:
    print(bag.is_affordable(100))  # inherited directly from parent, no override needed

# ============================================================
# isinstance() — proves inheritance is working
# A LuxuryBag IS-A Bag, and an AffordableBag IS-A Bag
# ============================================================
print("\n--- isinstance() checks ---")
print(f"Is bag1 a LuxuryBag?   {isinstance(bag1, LuxuryBag)}")   # True
print(f"Is bag1 a Bag?         {isinstance(bag1, Bag)}")          # True  ← inheritance!
print(f"Is bag7 an AffordableBag? {isinstance(bag7, AffordableBag)}")  # True
print(f"Is bag7 a Bag?         {isinstance(bag7, Bag)}")          # True  ← inheritance!

