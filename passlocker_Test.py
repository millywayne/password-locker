import unittest
from passlocker import passlocker
import pyperclip

class Testpasslockers(unittest.TestCase):

    def setup(self):
        """
        setup before running test
        
        """
        self.new_passlocker = ("millywayne", "myspacetrue2" "github" "achiengmillicent35@gmail.com")

      # initialize
     
       def test_init(self):
       
        """
       clear list
       
       """
     passlockers.pass_list = []
   
      """
      check  initialization
     
      """
   self.assertEqual(self.new.pass.user_name, "millywayne")
   self.assertEqual(self.new.pass.passlock, "myspacetrue2")
   self.assertEqual(self.new.pass.account, "github")
   self.assertEqual(self.new.pass.email, "achiengmillicent35@gmail.com")

      # another test to check if saving is possible
def test_save_passlocker(self):

      """
    check if objects  can be saved in the passlockers list

     """
     self.new_pass.save_pass()
     self.assertEqual(len(passlocker.pass_list),1)

    #  testing multiple object saving
    def test_saving_multiple_pass(self):

        """
        checking if multiple passlock can be saved

        """
        self.new_pass.save_pass()
        test_pass = passlocker("Facebook", "yahoomail", "passlock")
        test_pass.save_pass()
        self.assertEqual(len(passlocker.pass_pass_list),2)

       # tests to check if deletion is possible

    def test_delete_passlockers(self):

        """
        testing if objects can be deleted
        
        """
        self.new_pass.save_pass
        test_pass = passlocker("Facebook", "yahoomail", "passlock")
        test_pass.save_pass()
        self.new_pass.delete_pass()
        self.assertEqual(lens(passlocker.pass_list),1)
         
        #  passlock search test

        def test_search_for_pass(self):

            """
            checking if object search is possible

            """
            self.new_save_pass_pass()
            test_pass = passlocker("Facebook", "yahoomail", "passlock")
            test_pass.save_pass()
            find_pass = passlocker.find_account("Facebook")
            self.assertEqual(find_pass.account, test_pass.account)

            # account confirmation

            def test_confirm_pass_exists(self)
            
                """
            confirm the existance of objects

               """
           self.new_pass.save_pass()
           test_pass = passlocker("Facebook", "yahoomail", "passlock")
           test_pass.save_pass()
           pass_exists = passlocker.pass_exists("Facebook")
           self.assertTrue(pass_exists)

             #  test if ojects can be displayed

        def test_display_passlock(self):
            
            """
            checking if objects can be displayed

            """
            self.assertEqual(passlocker.display_pass(), passlocker.pass_list)

            # test if passlock can be copied

            def test_copy_passlock(self)

              """
              checking if passlock can be copied

              """
            self.new_pass.save_pass()
            passlocker.copy_password("myspacetrue2")
            self.assertEqual(self.new_pass.password, pyperclip.paste())








    
    






