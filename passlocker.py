import  pyperclip
class   passlocker:
    """
class that creates user account
"""
pass_list =[]

# assign property to list

def _init_(self, account, email, password):

   self.account = account
   self.email = email
   self.password = password

#    save passlock

def save_pass(self):
    """
    self passlocker in pass_list
    """
    passlocker.pass_list.apend(self)

    # delete passlock

def delete_pass(self):
    """
    delete passlocker
    """
    passlocker.pass_list.remove(self)

    # search passlock

    @classmethod
    def find_account(cls, account):
        """
        search  accounts
        
        """
      for pass in cls.pass_list:
        if pass.account == account:
            return Pass

                # confirm passlock

 @classmethod
 def pass_exist(cls, account):
    """
    confirm if class exists
    """
    for pass in cls.pas_list:
        if pass.account == account:
            return True
            return False
             
                
        # display passlock

@classmethod
def display_pass(cls):
    """
    method that returns all passlock
    """
    return cls.pass_list

    # copy password

    @classmethod
    def copy_password(cls, passlock):
        find_account = passlocker.find_account(password)
        pyperclip.copy(find_account.password)





