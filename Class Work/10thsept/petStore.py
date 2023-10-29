class petstore:
    def __init__(self):
        self.petDetails={
        }

    def storeDetails(self):
        category=input("Enter the category of the pet").strip().upper()
        name=input("Enter the name of the pet").strip().upper()
        age=input("Enter the age of the pet").strip().upper()
        gender=input("Enter the gender of the pet").strip().upper()
        price=input("Enter the price of the pet").strip().upper()
        pet={
            'Category': category,
            'Name': name,
            'Age': age,
            'Gender': gender,
            'Price': price
        }
        self.petDetails.update(pet)
        print(self.petDetails)

    