#march 30, 2026
#inheritance

# class Employee: #prototype of object
#     empCount = 0
    
#     def __init__(seld, name, saslary, gender):
#         self.name = name
#         self.salary = saslary
#         self.gender = gender
#         Employee.empcount += 1
        
#     def displayCount (self):
#         print "total employee %d" % Employee.empCount
        
#     def displayEmployee (self):
#         print "Name: ", self.name, ", Salary: ", self.salary
        

# class Parent:        # define parent class
#    parentAttr = 100
#    def __init__(self):
#       print ("Calling parent constructor")
 
#    def parentMethod(self):
#       print ('Calling parent method')
 
#    def setAttr(self, attr):
#       Parent.parentAttr = attr
 
#    def getAttr(self):
#       print ("Parent attribute :", Parent.parentAttr)
 
# class Child(Parent): # define child class
#    def __init__(self):
#       print ("Calling child constructor")
 
#    def childMethod(self):
#       print ('Calling child method')
 
# c = Parent()          # instance of child
# #c.childMethod()      # child calls its method
# c.parentMethod()     # calls parent's method
# c.setAttr(200)       # again call parent's method
# c.getAttr()          # again call parent's method

#====TYPES OF INHERITANCE====
#Single inheritance - a derived class inherits properties from a
#single parent class or the base class/super class.
# refers to the child class

#base class
#can have no constructor method, called DEFAULT CONSTRUCTOR METHOD
# class Parent:
#     def func1(self):
#         print("This function is in the parent class")

# #Derived
# class Child(Parent):
#     def func2(self):
#         print("This function is in child class")
        
# #Drivers code:
# object = Child()
# object.func1()
# object.func2()

#Multiple inheritance - can be derived from more than one base class.
# all the features of the base classes are inherited into the derived class.
class Mother:
    mothername = ""
    def mother(self):
        print(self.mothername)
 
# Base class2
class Father:
    fathername = ""
    def father(self):
        print(self.fathername)
 
# Derived class
class Son(Mother, Father):
    def parents(self):
        print("Father :", self.fathername)
        print("Mother :", self.mothername)
 
# Driver's code
s1 = Son()
s1.fathername = "RAM"
s1.mothername = "SITA"
 
s1.parents()

''''
single inheritance
hernandez, tambo, tan, arjona, caranyagan, nuesca, ignacio, panes,
villegaz, aran, garcia, bautista, de oro, rayo, magtira, cortas, welan,
concepcion, sandoval, anosa, sabio, lim, nacubuan, baquing, isidro, avelino,
mauring, eugenio, escanillas, lim jimmy, miciano, valdez, clerigo, domingo,
dizon, orate

multiple inheritance
tambo, hernandez, anosa, sandoval, isidro, caranyagan, mauring, garcia
tan, arjona, nuesca, rayo, bautista, magtira, ignacio, baquing, cortas,
sabio, eugenio, de oro, miciano, periodica, nacubuan, lim jc, lim jimmy,
villegas, aran, valdez, panes, domingo, escnillas, avelino, welan, dizon

'''