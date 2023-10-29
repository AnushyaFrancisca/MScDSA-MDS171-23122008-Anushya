nameList=[] #globally declaring the variable

def storeName():
    name=input("Enter the name to be saved")
    name=name.strip().title()
    nameList.append(name)
    return name

def listNames():
    print("*"*30)
    print("Names in the list")
    print("*"*30)
    for name in nameList:
        print(name)
    print("*"*30)

def searchName(search):
    search=search.strip().title()
    found=False
    for name in nameList:
        if name==search:
            found=True
            break
    if found == True:
        print("Name exists in the list")
    else:
        print(("Name does not exist"))

    


while True:
    print("*"*30)
    print("1. Enter a Name")
    print("2. List the Names")
    print("3. Search for a Name")
    print("4. Exit")
    print("*"*30)
    

    choice=input("Enter your choice")
    print("You have entered the choice",choice)
    
    if int(choice)==1:
        name=storeName()
        print("Name {} added successfully".format(name))
    elif int(choice)==2:
        listNames()
    elif int(choice)==3:
        name=input("Enter a name to be searched")
        searchName(name)
    elif int(choice)==4:
        break
    else:
        print("Invalid")


