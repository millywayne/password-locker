import  pyperclip
class   passlockers:
    '''
class that creates user account
'''
pass_list =[]

# assign property to list

def _init_(self, account, email, password):

   self.account = account
   self.email = email
   self.password = password

#    save passlock

def save_pass(self):
    '''
    self passlockers in pass_list
    '''
    passlockers.pass_list.apend(self)

    # delete passlock

def delete_pass(self):
    '''
    delete passlockers
    '''
    passlockers.pass_list.remove(self)

    # search passlock

    @classmethod
    def find_account(cls, account):
        '''
        search  accounts
        '''
        for pass in cls.pass_list:
            if pass.account == account:
                return pass

                # confirm passlock

@classmethod
def pass_exist(cls, account):
    '''
    confirm if class exists
    '''
    for pass in cls.pass_list:
        if Pass.account == account:
            return True
            return False
             
                
        # display passlock

@classmethod
def display_pass(cls):
    '''
    method that returns all credentials
    '''
    return cls.pass_list

    # copy password

    @classmethod
    def copy_password(cls, passlock):
        find_account = passlockers.find_account(passlock)
        pyperclip.copy(find_account.password)





