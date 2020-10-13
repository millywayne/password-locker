class user:
    """
    generating new instances
    """
    user__list = []
    def __init__(self, user__name, user__passlock)

     """
     saving objects for user_list
     """
     self.username = user__name
     self.userpasslock = userpasslock

      
def save__user(self):
    user.user__list.append(self)

       
def delete__user(self):
     """
     delete user account
     """
    user.user__list.remove(self)

          
@classmethod
def find__user(cls, username):
     """
     using search to find users
     """
 
 for user in cls.user__list:
 if user.username == username:
     return user