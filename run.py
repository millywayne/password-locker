from user import user
from passlocker import passlocker
import random



def create__user(fname, lname, email):
    """
    new user function
    """
    new__user = user(fname, lname, email):
    return new__user


def create__passlocker(username, userpasslock, email)
"""
create new user passlock
"""
new__passlocker = passlocker(username, userpassword, email)
return new__passlocker


def save__user(user):
    """
    saving user
    """
    user.save__user__details()


def save__pass(passlocker):
    """
    saving user passlocker
    """
    passlocker.save__passlocker()


def del__user(user):
    """
    deleting user
    """
    user.delete__user()


def del__pass(passlocker):
    """
    deleting all user passlocks
    """
    passlockers.delete__passlocker()    


def display__user():
    """
    displaying saved users
    """
    return User.display__user()


def  display__pass():
    """
    returning saved user passlocks
    """
    return Passlocker.display__passlocker()


    def main():

        print("Welcome to your passlock locker, choose your path from the list of allowed actions")

while True:
        print("Allowed Action: \n ad - create new user account with user-defined passlock\n ag - create a new user account with an auto-generated passlock\n da - display all user account \n ex -exit the contact list \n")

        short__code = input().lower()

        if short__code == '1':
            print("New User")
            print("-" * 20)
            print("Create account")
            account = input()

            print("Hi! welcome to {account} we love having you here!")

            print("First Name...")
            f__name = input()

            print ("Last Name...")
            l__name = input()

            print("Email Adress...")
            e__adress = input()

            print("Please Enter username...")
            user__name = input()

            print("Please Enter your passlock...")
            plock = input()

            save__user(create __user(f__name, l__name, e__adress))
            save__pass(create__passlocker(user__name, p__lock, e__adress))
            print('\n')
            print(f" Your new {account} by {f__name} {l__name} has been succesfully created" )
            print(f" Your username is {user__name} and the passlock is {plock}")
            print('\n')

      elif short__code =='2':
           print("New User")
           print("-" * 20)
           print("Hi!Please Enter the name of the account you would like to create thank you.")
           account = input()
           print(f" Welcome to {account} and Enjoy!!!")

           print("First Name...")
           f__name = input()

           print("Last Name...")
           l__name = input()

           print("Email Adress...")
           e__adress = input()

           print("Enter username... Hint: Generating a secure passlock")
           user__name = input()

           s = "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789abcdefghijklmnopqrstvuwxyz"
           plock = "".join(random.sample(s, 8))

           save__user(create__user(f__name, l__name, e__adress))
           save__pass(create__passlocker(user__name, p__lock, e__adress))
           print('\n')
           print(f" Your New {account} by {f__name} {l__name} has been created successfully")
           print(f" Your username is {user__name}")
           print(f" Your passlock is {p__lock}")
           print('\n')

       elif short__code == '3':

           if display__user():
               print("Below is a list of all your user accounts")
               print('\n')

               for user in display__user():
                   print(f" {user.first__name} {user.last__name} account name {account}")

                   print('\n')
              else:
                  print('\n')
                  print("You don't have an existing account")
                  print('\n')

             elif short__code == '4':
                 print(":/ Bye! Have a lovely day!!!")
                 break
             else:
                 print("Invalid passlock!") 
                 print("Aborting!!!") 

            
     if __name__ == '__main__':
         main()             