# Develop a contact management program where users can add, edit, delete, 
# and search contact details using a dictionary. The menu options would facilitate these actions.

Contact=[]
def addContact():
    name=input("Enter the name of the individual.").strip().title()
    phone=input("Enter the contact details of the individual.").strip()
    email=input("Enter the Email ID of the individual.").strip()
    contact={
        "Name":name,
        "Mobile No.":phone,
        "Email ID":email
    }
    Contact.append(contact)
    return "The contact details have been added successfully."

def editContact():
    print("Edit options are listed below:")
    print("1. Name")
    print("2. Mobile number")
    print("3. Email ID")
    print("4. Exit")
    edit=input("Enter the serial number of the category that you would like to edit.")
    if edit=='1':
        oldname=input("Enter the name you would like to change: ").strip().title()
        newname=input("Enter the new name:").strip().title()
        flag=False
        for i in Contact:
            if i["Name"]==oldname:
                flag=True
                i["Name"]=newname
                print("The new details are:",i)
        if flag==False:    
            print("The mentioned name is not found.")
    elif edit=='2':
        oldnumber=input("Enter the number you would like to change: ").strip()
        newnumber=input("Enter the new number:").strip()
        flag=False
        for i in Contact:
            if i["Mobile No."]==oldnumber:
                flag=True
                i["Mobile No."]=newnumber
                print("The new details are:",i)
        if flag==False:
            print("The mentioned name is not found.")
    elif edit=='3':
        oldID=input("Enter the Email ID you would like to change: ").strip().lower()
        newID=input("Enter the new Email ID: ").strip().lower()
        flag=False
        for i in Contact:
            if i["Email ID"]==oldID:
                flag=True
                i["Email ID"]=newID
                print("The new details are:",i)
        if flag==False:
            print("The mentioned name is not found.")
    elif edit=='4':
        print("You have chosen to exit.")
        exit()
    else:
        print("Invalid input.")

def searchContact():
    search=input("Enter the Name of the individual whose contact details is to be found:").strip().title()
    flag=False
    for i in Contact:
        if i["Name"]==search:
            flag=True
            print(i)
    if flag==False:
        print("Name not found.")
    choice=input("Enter 'Y' if you would like to edit the details of the individual displayed else enter 'N'.").strip().upper()
    if choice=='Y':
        editContact()
    else:
        print("You have chosen to not make any changes.")

def deleteContact():
    delete=input("Enter the name of the individual whose contact you would like to delete.").strip().title()
    flag=False
    for i in Contact:
        if i["Name"]==delete:
            flag=True
            Contact.remove(i)
            print("The contact has been deleted successfully. Current details available are: ",Contact)
    if flag==False:
        print("Name not found.")

while True:
    print("-"*30)
    print("The options facilitated by the Contact Management System is mentioned below:")
    print("1. Add the contact details of an individual.")
    print("2. Edit the contact details of an individual.")
    print("3. Search for the contact details of a particular indivudal.")
    print("4. Delete the contact details of a particular individual.")
    print("5. Exit.")
    print("-"*30)
    

    choose=input("Enter your choice")
    print("You have entered the choice",choose)
    
    if (choose)=='1':
        addContact()
        print(Contact)
    elif (choose)=='2':
        editContact()
    elif (choose)=='3':
        searchContact()
    elif (choose)=='4':
        deleteContact()
    elif (choose)=='5':
        print("You have chosen to exit.")
        exit()
    else:
        print("Invalid input")
        break