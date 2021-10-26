import pyperclip
import random
import string

from user_credentials import User, Credential

def generate_password(size=8, char=string.ascii_uppercase+string.ascii_lowercase+string.digits):
		'''
		Function to generate an 8 character password for a credential
		'''
		gen_pass=''.join(random.choice(char) for _ in range(size))
		return gen_pass


while True:
    print("Welcome, please SignUp by providing the Username and Password\n")
    uname = input("username: \n")
    pwd = ""
    print("Do you want the system to generate a password for you? Y/N \n")
    ans = input().lower()
    if(ans == "y"):
        print("you can choose the size of the password you want by entering the number of characters \n")
        pchar = input("do you what to choose characters? Y/N: ").lower()
        if(pchar == "y"):
            size = int(input("Enter the size you want your password to have: "))
            pwd = generate_password(size)
        else:
            pwd = generate_password()
        print("your password is: ")
        print(pwd)
    else:
        pwd = input("password: \n")
    nuser = User(uname, pwd)
    
    print("\n")
    
    logIn = input("Enter your Password to logIn into the System: \n")
    if(logIn == nuser.user_holder[1]):
        print(f"Welcome {nuser.user_holder[0]} you are in what do you want to do(use short code)?")
        while True:
                print("Use these short codes : cc - create new credential account, dc - display credentials, fc - find credential, del - to delete credential ex -exit the user list ")

                short_code = input().lower()

                if(short_code == "ex"):
                    break
               
                elif(short_code == "cc"):
                    print("Please provide account information\n")
                    accname = input("input account name\n")
                    username = input("input username\n")
                    password = input("input password\n")
                    new_crt = Credential(accname, username, password)
                    
                    new_crt.save_credentials
                    
                    print(new_crt.credential_holder)
                    
                    
                    
                elif(short_code == "del"):
                    print("Warning by contuning you will delete a credential informations,")
                    res = input("are you sure you want to processed? : Y/N ").lower()
                    if(res == "y"):
                        Credential.delete_credentials(Credential.credential_holder)
                       
                    elif(res == "n"):
                        pass
                elif(short_code == "dc"):
                    userAccountsInfo = dict()
                    userAccountsInfo.update([(f"{nuser.user_holder[1]}",f"{Credential.credential_holder}")])
                    print(userAccountsInfo)
                    # Credential
                elif(short_code == "fc"):
                    print("Enter the site name to copy to clipboard: \n")
                    sname = input()
                    rsult = Credential.find_by_site_name(sname)
                    Credential.copy_credential(rsult)

        
    else:
        print("wrong password please try again")
    break
