import unittest
from user import user
class Testuser(unittest.TestCase):

 def setup(self):

        """
        running method before test
        """
        self.user = user("millywayne", "myspacetrue2") 
 def test__init(self):
         """
        prevent errors
         """
        
        
         user.user__list = []

 def test__init(self):
         """
        checking initialization
         """
               
         self.assertEqual(self.new__user.username, "millywayne")
         self.assertEqual(self.new__user.passlock, "myspacetrue2")
                 
 def test__save_user():
         """
        saving user information in the user__list
         """
         self.new__user.save__user()
         self.assertEqual(len(user.user__list), 1)

       
 def test__save__multiple__user(self):
         """
        storing multiple users
         """
         self.new__user.save__multiple__user()
         test__user = user("test", "userpasslock")
         test__user.save__user()
         self.assertEqual(len(user.user__list), 2)

  
 def test__delete__user(self):
         """
        checking if users can be deleted
         """
         self.new__user.save__user()
         test__user = ("test", "userpasslock")
         test__user.save__user()
         self.new__user.delete__user()
         self.assertEqual(len(user.user__list), 1)


   
 def test_find_user(self):
         """
        finding users using user name
         """
         self.new__user.save__user()
         test__user = user("test", "userpasslock")
         test__user.save__user()
         found__user = user.find__user("millywayne")
         self.assertEqual(found__user.username, self.new__user.username)
         
   if __name__ == '__main__':
         unittest.main()