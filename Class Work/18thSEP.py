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

#class Restaurant():
    # def __init__(self,item,quantity): 
    #     self.item = item
    #     self.quantity = quantity
    #     self.menu={"Menu":[
    #         ("rice":30),
    #         ("chicken":100),
    #     ]}

    # def findCost(self):
    #     total=0
    #     total=self.quantity*self.menu[self.item]
    #     print(self.name,self.quantity,total )

#order=Restaurant("rice",4)
#order.findCost()

#order=Restaurant("chicken",3)
#order.findCost()

#Define a class expense tracker that stores the expenses 
#and income in a dictionary 
#implement the method to 
# - store the transaction
# - view transaction
# - calculate the total expense

class expenseTracker():
    def __init__(self): 
        self.transactions = {
            "Details": []
        }
    
    def storeTransaction(self):
        file=open("Expense_Income_Tracker.csv","w+")
        file.write("Type,Expense Category,Amount,Description,Date\n")
        for i in self.transactions["details"]:
            date=str(i["date"]).strip()
            file.write(i["type"]+","+i["category"]+","+i["amount"]+","+i["description"]+","+date+"\n")
        file.close()
    
    def retrieveTransactions(self):
        for i in open("Expense_Income_Tracker.csv","r+").readlines():
            line=i.split(",")
            if line[1]!="Expense Category":
                transaction={"type":line[0],"category":line[1],"amount":line[2],"description":line[3],"date":line[4]}
                self.transactions["details"].append(transaction)
    


    def calculateTotal(self):
        totalIncome=0
        totalExpense=0
        for i in self.transactions["details"]:
            if i["type"]=="Income":
                totalIncome+=int(i["amount"])
            else:
                totalExpense+=int(i["amount"])
        return totalIncome,totalExpense
    
    def addTransaction(self,type,category,amount,description,date):
        transaction={"type":type,"category":category,"amount":amount,"description":description,"date":date}
        self.transactions["Details"].append(transaction)

 

order=expenseTracker()
order.retrieveTransactions()


while True:
    print("1.Add new Transaction details.")
    print("2. Calculate the Total Income.")
    print("3. Exit.")
    choice=input("Enter the Sl.no of your choice: ")
    if choice=='1':
        type=input("Enter the type of transaction (Income/Expense):")
        category=input("Enter the category:")
        amount=input("Enter the amount:")
        description=input("Enter the description of the transaction:")
        date=input("Enter the date in MM/DD/YYYY format:")
        order.addTransaction(type,category,amount,description,date)
    elif choice=='2':
        totalIncome,totalExpense=order.calculateTotal()
        print("Total Income=",totalIncome,"\nTotal Expense=",totalExpense)
        order.storeTransaction()
    elif choice=='3':
        order.storeTransaction()
        exit()
        

  