class store:
    def __init__(self):
        self.orders={}
        self.inventory={'PID001':{"Product id": 'PID001', "ProductName": 'APPLE',"Quantity":'40',"Price": '15'},
                        'PID002':{"Product id": 'PID002', "ProductName": 'JUICE',"Quantity":'100',"Price": '10'},
                        'PID003':{"Product id": 'PID003', "ProductName": 'CHCOLATE',"Quantity":'200',"Price": '20'},
                        'PID004':{"Product id": 'PID004', "ProductName": 'BREAD',"Quantity":'30',"Price": '30'},
                        'PID005':{"Product id": 'PID005', "ProductName": 'MILK',"Quantity":'60',"Price": '28'},
                        'PID006':{"Product id": 'PID006', "ProductName": 'ONIONS',"Quantity":'250',"Price": '39'}
                        }

    def createOrder(self,Orderid, productID, productName, Quantity, Total):
        temp={
            'OrderID':Orderid,
            'ProductID':productID,
            'ProductName':productName,
            'Quantity':Quantity,
            'Total':Total
        }

        self.orders[Orderid]=temp
        self.updateInventory(productID,productName,Quantity)

    def updateInventory(self, productID, productName, Quantity):
        temp=int(self.inventory[productID]['Quantity'])
        if Quantity>temp:
            print("The quantity of order placed exceeds the quantity present in the inventory.")
        else:
            new=temp-Quantity
            self.inventory[productID]['Quantity']=new

    
        
