from os import uname
from passlocker import passlocker


class user:
     """
     generating new instances
     """
     user__list = []

     def __init__(self, uname, passlock, email):
      """
      saving objects for user_list
       """
     self.username = uname
     self.userpasslock = passlocker
  

     def save__user(self):
         """
     save user account
     """
         user.user__list.append(self)

       
     def delete__user(self):
         """
      delete user account
      """
         user.user__list.remove(self)
         @classmethod
     
     
         def find__user(cls, uname):
          """
       using search to find users
        """

     for user in cls.user__list:
      if user.username == uname:
       return user 