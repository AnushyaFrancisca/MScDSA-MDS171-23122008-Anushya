class sportMart:
    def __init__(self):
        self.inventory = {}
        self.orders={}

    def createInventory(self,ProductID,Items,Quantity,Price):
        temp = {
            "Product id": ProductID,
            "ProductName":Items,
            "Quantity":Quantity,
            "Price":Price
        }

        self.inventory[ProductID]=temp
    
    def createOrder(self,OrderID,ItemName,Quantity,Price):
        temp = {
            'orderid':OrderID,
            'productid':ItemName,
            'quantity':Quantity,
            'Price':Price
        }
        self.orders[OrderID]=temp

    def printOrders(self):
        print(self.orders)

    def printInventory(self):
        print(self.inventory)


trinity = sportMart()
orders=open("orders.csv","r")
o_header=orders.readline()
o_data=orders.readlines()
for data in o_data:
    tmp=data.strip().split(',')
    trinity.createOrder(tmp[0],tmp[1],tmp[2],tmp[3])

trinity.printOrders()

trinity = sportMart()
inventory=open("inventory.csv","r")
i_header=inventory.readline()
i_data=inventory.readlines()
for data in i_data:
    tmp=data.strip().split(',')
    trinity.createInventory(tmp[0],tmp[1],tmp[2],tmp[3])

trinity.printInventory()