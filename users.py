class user:
    
    """
    generating new instances

    """
    user_list = []
    def _init_(self, user_name, user_passlock)

     """
     saving objects for user_list

     """
     self.username = user_name
     self.userpasslock = userpasslock

       #  multiple users

       def save_user(self):
           user.user_list.append(self)

        #    delete

        def delete_user(self):
            
            """
            delete user account

            """
            user.user_list.remove(self)

            # locate user

            @classmethod
            def find_user(cls, username):

                """
                using search to find users

                """
                for user in cls.user_list:
                    if user.username == username:
                        return user
