class  passlocker:
      """
     class that creates user account
     """
      pass__list = []
    
    
      def __init__(self, account, email, password):
    
       self.account = account
       self.email = email
       self.password = password

   
def save__pass(self):
    """
    save passlocker in pass__list
    """
    passlocker.pass__list.append(self)

    
def delete__pass(self):
    """
    delete passlocker
    """
    passlocker.pass__list.remove(self)
    """
    method that returns all passlock
     """
    return cls.pass__list

   
@classmethod
def copy__password(cls, passlock):
          find__account = passlocker.find__account(passlock)         