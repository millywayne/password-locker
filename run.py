from typing import Counter
from user import user
from passlocker import passlocker
import random


def create_user(fname, lname, email,):
    """
    new user function
    """
    new_user = user(fname, lname, email)  
    return new_user


def create_passlocker(username, userpasslock, email):
     """
    create new user passlock
    """
     new_passlocker = passlocker(username, userpasslock, email)
   

def save_user(user):
     """
    saving user
    """
     user.save_user_details()


def save_pass(passlocker):
    """
    saving user passlocker
    """
    passlocker.save_passlocker()


def del_user(user):
    """
    deleting user
    """
    user.delete_user()


def del_pass(passlocker):
    """
    deleting all user passlocks
    """
    passlocker.delete_passlocker()    


def display_user():
    """
     displaying saved user
     """
    return user.display_user()


def  display_pass():
    """
    returning saved user passlocks
    """
    return passlocker.display_passlocker()


def main():

        print("Welcome to your passlock locker, choose your path from the list of allowed actions")

while True:
        print("Allowed Action: \n ad - create new user account with user-defined passlock\n ag - create a new user account with an auto-generated passlock\n da - display all user account \n ex -exit the contact list \n")

        short_code = input().lower()

        if short_code == '1':
            print("New User")
            print("-" * 20)
            print("Create account")
            account = input()

            print("Hi! welcome to {account} we love having you here!")

            print("First Name...")
            f_name = input()

            print ("Last Name...")
            l_name = input()

            print("Email Adress...")
            e_adress = input()

            print("Please Enter username...")
            user_name = input()

            print("Please Enter your passlock...")
            plock = input()

            save_user(create_user(f_name, l_name, e_adress))
            save_pass(create_passlocker(user_name, plock, e_adress))
            print('\n')
            print(f" Your new {account} by {f_name} {l_name} has been succesfully created" )
            print(f" Your username is {user_name} and the passlock is {plock}")
            print('\n')

        elif short_code == '2':
           
            print("New User")
            print("-" * 20)
            print("Hi!Please Enter the name of the account you would like to create thank you.")
            account = input()
            print(f" Welcome to {account} and Enjoy!!!")

            print("First Name...")
            f_name = input()

            print("Last Name...")
            l_name = input()

            print("Email Adress...")
            e_adress = input()

            print("Enter username... Hint: Generating a secure passlock")
            user_name = input()

            s = "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789abcdefghijklmnopqrstvuwxyz"
            plock = "".join(random.sample(s, 8))

            save_user(create_user(f_name, l_name, e_adress))
            save_pass(create_passlocker(user_name, plock, e_adress))
            print('\n')
            print(f" Your New {account} by {f_name} {l_name} has been created successfully")
            print(f" Your username is {user_name}")
            print(f" Your passlock is {plock}")
            print('\n')

        
        elif short_code == '3':

         if display_user():
            print("Below is a list of all your user accounts")
            print('\n')

        for user in display_user():
            print(f" {user.first_name} {user.last_name} account name {Counter}")

            print('\n')
        else:
            print('\n')
            print("You don't have an existing account")
            print('\n')

        if short_code == '4':
  
         print(":/ Bye! Have a lovely day!!!")
        break
else:
        print("Invalid passlock!") 
print("Aborting!!!") 

            
if __name__ == '__main__':
           main()             