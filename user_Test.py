import unittest
from user import user
class Testuser(unittest.TestCase):

 def setup(self):

        """
        running method before test
        """
        self.user = user("millywayne", "myspacetrue2") 
 def test_init(self):
         """
        prevent errors
         """
        
        
         user.user_list = []

 def test_init(self):
         """
        checking initialization
         """
               
         self.assertEqual(self.new_user.username, "millywayne")
         self.assertEqual(self.new_user.passlock, "myspacetrue2")
                 
 def test_save_user():
         """
        saving user information in the user_list
         """
         self.new_user.save_user()
         self.assertEqual(len(user.user_list), 1)

        #    multiple users

 def test_save_multiple_user(self):
         """
        storing multiple users
         """
         self.new_user.save_multiple_user()
         test_user = user("test", "userpasslock")
         test_user.save_user()
         self.assertEqual(len(user.user_list), 2)

    #    deleting user

 def test_delete_user(self):
         """
        checking if users can be deleted
         """
         self.new_user.save_user()
         test_user = ("test", "userpasslock")
         test_user.save_user()
         self.new_user.delete_user()
         self.assertEqual(len(user.user_list), 1)


    #    searching for users

 def test_find_user(self):
         """
        finding users using user name
         """
         
         self.new_user.save_user()
         test_user = user("test", "userpasslock")
         test_user.save_user()
         found_user = user.find_user("millywayne")
         self.assertEqual(found_user.username, self.new_user.username)
  
        
         
         
        if _name_ == '_main_':
         unittest.main()
            
                       
        
         

