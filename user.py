from os import uname
from passlocker import passlocker


class user:
     """
     generating new instances
     """
     user_list = []

     def _init_(self, uname, passlocker, email):
      """
      saving objects for user_list
       """
      self.username = uname
      self.userpasslock = passlocker
  

     def save_user(self):
         """
     save user account
     """
         user.user_list.append(self)

       
     def delete_user(self):
         """
      delete user account
      """
         user.user_list.remove(self)
         @classmethod
     
     
         def find_user(cls, uname):
          """
       using search to find users
        """
     for user in cls.user_list:
      if user.username == uname:
       return user   