# ============================================================
#  INHERITANCE PILLAR — 3 Levels Deep
#  Animal  →  Dog  →  GoldenRetriever
#  (Grandparent) (Parent) (Child)
#
#  Think of it like real life:
#  A Golden Retriever IS-A Dog, and a Dog IS-A Animal.
#  Traits get passed DOWN the chain automatically.
# ============================================================


# ============================================================
# LEVEL 1 — GRANDPARENT CLASS
# The most general class. Every living animal has these.
# ============================================================
class Animal:
    kingdom = "Animalia"  # class attribute — all animals share this

    def __init__(self, name, age, sound):
        self.name = name
        self.age = age
        self.sound = sound

    def speak(self):
        return f"{self.name} says: {self.sound}!"

    def breathe(self):  # every animal breathes — defined once here, inherited by all
        return f"{self.name} is breathing."

    def info(self):
        return f"[Animal] Name: {self.name}, Age: {self.age}"


# ============================================================
# LEVEL 2 — PARENT CLASS
# Inherits everything from Animal, then adds dog-specific stuff.
# A Dog IS-A Animal → so it gets speak(), breathe(), info() for free.
# ============================================================
class Dog(Animal):  # Dog inherits from Animal

    def __init__(self, name, age, breed, is_trained):
        # Pass shared attributes UP to Animal's constructor
        super().__init__(name, age, sound="Woof")  # dogs always say Woof
        self.breed = breed
        self.is_trained = is_trained  # new attribute only dogs have

    # METHOD OVERRIDING — Dog has a more specific version of info()
    def info(self):
        base = super().info()  # reuse Animal's info, then extend it
        trained = "trained" if self.is_trained else "not trained"
        return f"{base}, Breed: {self.breed}, {trained}"

    # NEW METHOD — unique to Dog, Animal doesn't have this
    def fetch(self):
        return f"{self.name} fetches the ball! 🎾"


# ============================================================
# LEVEL 3 — CHILD CLASS
# Inherits from Dog (which already inherited from Animal).
# So GoldenRetriever gets EVERYTHING from both levels above.
# A Golden Retriever IS-A Dog AND IS-A Animal.
# ============================================================
class GoldenRetriever(Dog):  # GoldenRetriever inherits from Dog

    def __init__(self, name, age, is_trained, is_therapy_dog):
        # Pass up to Dog's constructor (which passes up to Animal's)
        super().__init__(name, age, breed="Golden Retriever", is_trained=is_trained)
        self.is_therapy_dog = is_therapy_dog  # unique to this specific breed class

    # METHOD OVERRIDING — GoldenRetriever has its own version of info()
    def info(self):
        base = super().info()  # reuse Dog's info (which already reused Animal's)
        therapy = "therapy dog 🐾" if self.is_therapy_dog else "regular pet"
        return f"{base}, Role: {therapy}"

    # NEW METHOD — only Golden Retrievers do this (in our model)
    def swim(self):
        return f"{self.name} loves swimming! 🌊"

    # NEW METHOD — therapy-specific behavior
    def comfort(self, person_name):
        if self.is_therapy_dog:
            return f"{self.name} gently comforts {person_name}. 🧡"
        else:
            return f"{self.name} wags their tail at {person_name}!"


# ============================================================
# OBJECTS
# ============================================================
generic_animal = Animal("Leo the Lion", 5, "Roarr")

rex = Dog("Rex", 3, "German Shepherd", is_trained=True)

buddy = GoldenRetriever("Buddy", 4, is_trained=True, is_therapy_dog=True)
sunny = GoldenRetriever("Sunny", 2, is_trained=False, is_therapy_dog=False)


# ============================================================
# OUTPUT — showing what each level inherited vs added
# ============================================================
print("=" * 60)
print("       INHERITANCE CHAIN: Animal → Dog → GoldenRetriever")
print("=" * 60)

print("\n--- LEVEL 1: Animal (Grandparent) ---")
print(generic_animal.info())            # Animal's own info()
print(generic_animal.speak())           # Animal's own speak()
print(generic_animal.breathe())         # Animal's own breathe()

print("\n--- LEVEL 2: Dog (Parent) ---")
print(rex.info())                       # OVERRIDDEN info() from Dog
print(rex.speak())                      # INHERITED speak() from Animal ✅
print(rex.breathe())                    # INHERITED breathe() from Animal ✅
print(rex.fetch())                      # NEW method from Dog

print("\n--- LEVEL 3: GoldenRetriever (Child) ---")
print(buddy.info())                     # OVERRIDDEN info() from GoldenRetriever
print(buddy.speak())                    # INHERITED speak() from Animal ✅ (2 levels up!)
print(buddy.breathe())                  # INHERITED breathe() from Animal ✅ (2 levels up!)
print(buddy.fetch())                    # INHERITED fetch() from Dog ✅ (1 level up!)
print(buddy.swim())                     # NEW method from GoldenRetriever
print(buddy.comfort("Maria"))           # NEW method from GoldenRetriever

print("\n--- Sunny (not a therapy dog) ---")
print(sunny.info())
print(sunny.comfort("Jose"))            # same method, different output based on attribute

# ============================================================
# isinstance() — proves the full chain
# GoldenRetriever IS-A Dog IS-A Animal
# ============================================================
print("\n--- isinstance() — the IS-A chain ---")
print(f"buddy is a GoldenRetriever? {isinstance(buddy, GoldenRetriever)}")  # True
print(f"buddy is a Dog?             {isinstance(buddy, Dog)}")               # True  ← inherited!
print(f"buddy is an Animal?         {isinstance(buddy, Animal)}")            # True  ← inherited 2 levels up!
print(f"rex is a GoldenRetriever?   {isinstance(rex, GoldenRetriever)}")    # False — parent doesn't know child