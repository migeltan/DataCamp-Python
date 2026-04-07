#Multilevel Inheritance
class Grandfather:
    grandfathername = ""
    def grandfather(self):
        print(self.grandfathername)

class Father(Grandfather):
    fathername = ""
    def father(self):
        print(self.fathername)

class Son(Father): #3rd level
    sonname = ""
    def family(self):
        print("Grandfather:", self.grandfathername)
        print("Father:", self.fathername)
        print("Son: ", self.sonname)

s1 = Son()
s1.grandfathername = "RINO TAN"
s1.fathername = "MICHAEL TAN"
s1.sonname = "MIGEL TAN"
s1.family()


# Hierarchical Inheritance
class Parent:
    parentname = ""
    def parent(self):
        print(self.parentname)

class Son(Parent): #derived from parent
    def details(self):
        print("Son's Parent:", self.parentname)
        
class Daughter(Parent): #derived from parent
    def details(self):
        print("Daughter's Parent:", self.parentname)

s1 = Son()
s1.parentname = "ANGELICA TAN & MICHAEL TAN"
s1.details()

d1 = Daughter()
d1.parentname = "ANGELICA TAN & MICHAEL TAN"
d1.details()


#Hybrid Inheritance
class Grandfather:
    grandfathername = ""
    def grandfather(self):
        print(self.grandfathername)

class Father(Grandfather):
    fathername = ""
    def father(self):
        print(self.fathername)
class Mother(Grandfather):
    mothername = ""
    def mother(self):
        print(self.mothername)

class Son(Father, Mother): 
    def family(self):
        print("Grandfather:", self.grandfathername)
        print("Father:", self.fathername)
        print("Mother:", self.mothername)

s1 = Son()
s1.grandfathername = "RINO TAN"
s1.fathername = "MICHAEL TAN"
s1.mothername = "ANGELICA TAN"

s1.family()