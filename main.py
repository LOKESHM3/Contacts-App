'''Phone Book using Python
Author: Malireddy Lokesh
'''
import sys
def prepare_directory():
    rows=int(input('Please specify number of contacts to be added:'))
    directory=[]

    for i in range(rows):
        directory= add_contact(directory)
    return directory

def menu():
    print("****CONTACT DIRECTORY*******")
    print("\n Please provide input according to the options given below (Press 0 to exit):")
    print("1. Add a new contact")
    print("2. Delete a contact")
    print("3. Search for a contact")
    print("4. Delete all the existing contacts")
    print("5. Display all the existing contacts")
    print("6. Update an existing contact")
    print("0. Exit")
    
    option= int(input("Please enter your choice:"))
    return option

def add_contact(direc):
    contact=[]
    name= input("Enter name: ")
    if name=='' or name.isspace():
        sys.exit("Name is mandatory")
    contact.append(name)

    city= input("Enter City: ")
    contact.append(city)

    phNumber= input("Enter phone number: ")
    if (phNumber.isnumeric()):
        contact.append(int(phNumber))
    else:
        sys.exit("Please enter a valid number")

    email=input("Enter email address: ")
    contact.append(email)
    direc.append(contact)
    return direc

def remove_contact(direc):
    name= input("Please enter the name you would like to remove: ")

    flag= False
    for c in range(len(direc)):
        if direc[c][0]==name:
            flag= True
            print(direc.pop(c))
            print("The contact has been removed from the directory.")
            return direc
    if flag== False:
        print("Contact not found. Please check again")
    return direc

def search_contact(direc):
    name= input("Please enter the name you would like to search: ")
    flag= False
    for c in range(len(direc)):
        if direc[c][0]==name:
            flag= True           
            print("\nThe contact details are: \n")
            print(direc[c])
            return direc
    if flag== False:
        print("Contact not found. Please check again") 
    return direc

def delete_all(direc):
    inp= input("Are you sure to delete the entire data? Press 1 to continue.")
    if inp=="1":
        direc.clear()
        direc=[]
        print("All data has been deleted.")
    
    return direc

def display_all(direc):
    if len(direc)>0:
        for i in range(len(direc)):
            print("Contact Details of ", i+1, " person:")
            print("Name: ", direc[i][0])
            print("City: ", direc[i][1])
            print("Phone: ", direc[i][2])
            print("Email: ", direc[i][3])
            print()
    else:
        print("No Contacts to be displayed")

    return direc

def update_contact(direc):
    name= input("Please enter the name for the contact you would like to update: ")
    
    flag= False
    for c in range(len(direc)):
        if direc[c][0]==name:
            flag= True      
            print("Please specify the field you would like to change: \n")     
            print("1. Change Name")
            print("2. Change City")
            print("3. Change Phone Number")
            print("4. Change Email")

            inp= int(input("Please enter your choice: "))
            
            if inp==1:
                name=input("Enter new name: ")
                direc[c][0]= name
            elif inp==2:
                city=input("Enter the new city:")
                direc[c][1]= city
            elif inp==3:
                num=input("Enter the new number:")
                direc[c][2]= num
            elif inp==2:
                email=input("Enter the new email:")
                direc[c][3]= email
            else:
                print("Please provide a valid input")  
            print(direc)
            return direc
    if flag== False:
        print("Contact not found. Please check again") 
    return direc

direc =  prepare_directory()
print(direc)
while True:
    option = menu()
    if option== 1:
        direc= add_contact(direc)
        print(direc)
    elif option==2:
        direc= remove_contact(direc)
    elif option==3:
        direc= search_contact(direc)
    elif option==4:
        direc=delete_all(direc)
    elif option==5:
        direc= display_all(direc)
    elif option==6:
        direc= update_contact(direc)
    elif option==0:
        break
    else:
        print("Please provide a valid input.")