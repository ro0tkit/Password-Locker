class User:
    """
    Class that generates new instances of a user
    """
    user_list = []
    def __init__(self,user_name,password):
        self.user_name = user_name
        self.password = password
    
    def save_user(self):
        """
        save user method savces new objects to the user_list
        """
        User.user_list.append(self) 

    def delete_user(self)
        """
        delete_user method deletes contact objectd from the user_list
        """ 
        User.user_list.remove(self)