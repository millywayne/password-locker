class  passlocker:
      """
     class that creates user account
     """
      pass_list = []
    
    
      def __init__(self, account, email, password, ):
    
       self.account = account
       self.email = email
       self.password = password

   
def save_pass(self):
    """
    save passlocker in pass_list
    """
    passlocker.pass_list.append(self)

    
def delete_pass(self):
    """
    delete passlocker
    """
    passlocker.pass_list.remove(self)
    """
    method that returns all passlock
     """
    return cls.pass_list

   
@classmethod
def copy_password(cls, passlock):
          find_account = passlocker.find_account(passlock)         