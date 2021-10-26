import os
import pyperclip
import random
import string

# global userAccountsInfo

class User:
    """
    Class that generates new instances of user account
    """
    user_holder =[]

    def __init__(self,username,password):
        '''
        __init__ method that helps us define properties for our objects.

        Args:
            user_username: New user username.
            user_password: New user password.
        '''
        self.user_username = username
        self.user_password = password
        self.save_user(self.user_username, self.user_password)
        
    def save_user(self, usrname, pwd):
        '''
        save_user method saves user objects into user_holder
        '''
        User.user_holder.append(usrname)
        User.user_holder.append(pwd)
        return self.user_holder
    
class Credential:
    
    credential_holder = dict()
    def __init__(self, accountname, username, password):
        self.acc = accountname
        self.uname = username
        self.pwd = password
        self.save_credentials(self.acc, self.uname, self.pwd)
        
    def save_credentials(self, acc, uname, pwd):
        list_credentials = []
        # list_credentials.append(acc)
        list_credentials.append(uname)
        list_credentials.append(pwd)
        Credential.credential_holder.update([(acc, list_credentials)])
        print("Credentials created successfully")
        
    @classmethod    
    def generate_password(size=8, char=string.ascii_uppercase+string.ascii_lowercase+string.digits):
        '''
        Function to generate an 8 character password for a credential
        '''
        gen_pass=''.join(random.choice(char) for _ in range(size))
        return gen_pass
    
    @classmethod
    def delete_credentials(cls, Credentialacc):
        holedkey = ""
        cle = input("enter credential\n")
        for key in Credentialacc.keys():
            if(key == cle):
                # del dic[key]
                holedkey = key
        del Credentialacc[holedkey]
        print(Credentialacc)
        
    @classmethod
    def find_by_site_name(cls, site_name):
        '''
        Method that takes in a site_name and returns a credential that matches that site_name.
        '''
        for credential in Credential.credential_holder.keys():
            # print(credential)
            if credential == site_name:
                return credential

    @classmethod
    def copy_credential(cls,site_name):
        '''
        Class method that copies a credential's info after the credential's site name is entered
        '''
        find_credential = Credential.find_by_site_name(site_name)
        return pyperclip.copy(cls.credential_holder[find_credential][0])

        
        



