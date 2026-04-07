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