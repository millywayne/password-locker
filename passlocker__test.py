import unittest
from passlocker import passlocker
import pyperclip

class Testpasslockers(unittest.TestCase):

def setup(self):
        """
        setup before running test
        """
        self.new_passlocker = ("millywayne", "myspacetrue2" "github" "achiengmillicent35@gmail.com")

     
     
def test__init(self):
        """
       clear list
        """
     passlockers.pass__list = []
        """
      check  initialization
        """
   
   self.assertEqual(self.new.pass.user__name, "millywayne")
   self.assertEqual(self.new.pass.passlock, "myspacetrue2")
   self.assertEqual(self.new.pass.account, "github")
   self.assertEqual(self.new.pass.email, "achiengmillicent35@gmail.com")

      
def test_save_passlocker(self):
     """
    check if objects  can be saved in the passlockers list
     """
     self.new__pass.save_pass()
     self.assertEqual(len(passlocker.pass__list),1)

   
def test_saving__multiple__pass(self):
        """
        checking if multiple passlock can be saved
        """
        
        
        self.new__pass.save__pass()
        test__pass = passlocker("Facebook", "yahoomail", "passlock")
        test__pass.save__pass()
        self.assertEqual(len(passlocker.pass__pass__list),2)

       

 def test__delete__passlockers(self):
        """
        testing if objects can be deleted
        """
       
       
        self.new__pass.save__pass
        test__pass = passlocker("Facebook", "yahoomail", "passlock")
        test__pass.save__pass()
        self.new__pass.delete__pass()
        self.assertEqual(lens(passlocker.pass__list),1)
         
       

  def test__search__for__pass(self):
            """
            checking if object search is possible
            """
            self.new__save__pass__pass()
            test__pass = passlocker("Facebook", "yahoomail", "passlock")
            test__pass.save_pass()
            find__pass = passlocker.find__account("Facebook")
            self.assertEqual(find__pass.account, test__pass.account)

            
  def test__confirm__pass__exists(self)
          """
         confirm the existance of objects
          """
           self.new__pass.save__pass()
           test__pass = passlocker("Facebook", "yahoomail", "passlock")
           test__pass.save_pass()
           pass__exists = passlocker.pass__exists("Facebook")
           self.assertTrue(pass__exists)

            
    def test__display__passlock(self):
            """
            checking if objects can be displayed
            """
            self.assertEqual(passlocker.display_pass(), passlocker.pass_list)

            

    def test__copy__passlock(self)
              """
              checking if passlock can be copied
              """
            self.new__pass.save__pass()
            passlocker.copy__password("myspacetrue2")
            self.assertEqual(self.new__pass.password, 
            pyperclip.paste())