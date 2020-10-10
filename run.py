from passlocker import passlocker
from user import user
import random

def create_useraccount(username, userpasslock):
    """
     creates account
    """
    new_user = user(username, userpasslock)
    return new_user

    # saving users

def save_user(user):
    """
    method save user
    """
    user.save_user()

    def save_passlocker(passlocker):

     """
    save account
     """
     passlocker.save_passlocker

    #  user search

def find_user(username)
     """
    find users using user name
     """
    return user.find_user(username)

    # creating passlocker

    def create_passlocker(account, email, password):
        """
        creating passlocker
        """

        new_pass = passlocker(account, email, password)
        return new_pass

        saving passlocker

    def save_pass(pass):
        """
        save passlocker
        """
        pass.save_pass()


       

       




   
