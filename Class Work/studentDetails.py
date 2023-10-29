#menu-driven program
#details of students in class
# {
#     Name:
#     Reg. No:
#     Phone:
#     Email:
# }

#Search Reg no & print all the details
#check if the reg no exists, if exists replace all the details with the new one.
newList=[]
def storeDetails():
    name=input("Enter the name of the student.").strip().title()
    reg=input("Enter the registration number of the student.")
    phone=input("Enter the mobile number of the student.")
    email=input("Enter the email id of the student.")
    student={
        "name":name,
        "reg. no":reg,
        "phone":phone,
        "email":email,
    }
    newList.append(student)
    done=("The details have been stored successfully")
    return done

storeDetails()

def displayDetails():


def searchDetails():

