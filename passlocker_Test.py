import unittest
from passlockers import passlockers
import pyperclip

class Testpasslockers(unittest.TestCase):

    def setup(self):
        """
        setup before running test
        """
        self.new_passlockers = ("millywayne", "myspacetrue2" "github" "achiengmillicent35@gmail.com")

      # initialize
 def test-init(self):
        """
       clear list
       """
passlockers.pass_list = []

   """
   check if initialization
   
   """
   self.assertEqual(self.new.pass.user_name, "millywayne")
   self.assertEqual(self.new.pass.passlock, "myspacetrue2")
   self.assertEqual(self.new.pass.account, "github")
   self.assertEqual(self.new.pass.email, "achiengmillicent35@gmail.com")

      # more tests
def test_save_passlockers(self):

      """
    check if objects  can be saved in the passlockers list

     """
     self.new_pass.save_pass()
     self.assertEqual(len(credentials.pass_list)1)
     

    
    






