# class Student():

#     #data members
#     # name, email, phone
    
#     #member function - a function that the class is performing
#     def __init__(self): #initialising the data members of the class #__init__(self) is a constructor
#         self.name="Anushya" #here we are creating variables and assigning values to that variable
#         self.email="anushya@gmail.com"
#         self.phone=12342423423

#     def printStudent(self):
#         print("Name : {},\nEmail : {},\nPhone: {}".format(
#             self.name,self.email,self.phone
#         ))

#     def __str__(self):
#         pass

# Anushya=Student()
# Anushya.printStudent()

# class Student:
#     def __init__(self,a,b):
#         self.name = a
#         self.stu_class = b

# abc = Student("Anushya","MSc") #creating an object. Note: indentation
# print(abc.name,abc.stu_class)
# print(abc)
# print(type(abc))
# # int, str, float are all classes

# create a class restuarant that accepts iten name and quantity as input 
# inside your calss you are having the item and its price as a dictionary
# create a function calculate cost that prints the itemname, quantity and price

class Restaurant():
    def __init__(self,item,quantity):
        self.item = item
        self.quantity = quantity
        self.menu={"Menu":[
            ("rice":30),
            ("chicken":100),
        ]}

def findCost(self):
    total=0

    print(self.name,self.quantity,total )