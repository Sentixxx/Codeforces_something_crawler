import os
import getpass
import json
   
CF_ACCOUNT = 'CF_ACCOUNT'
CF_PASSWORD = 'CF_PASSWORD'
   
def make_account():
    account = input("Account: ")
    
    while True:
        password = getpass.getpass("Password: ")
        confirmed_password = getpass.getpass("Confirm password: ")

        if password == confirmed_password:
            break
        else:
            print("password dismatch!")
   
    os.system(f"export {CF_ACCOUNT}='{account}'")
    os.system(f"export {CF_PASSWORD}='{password}")

def delete():
    os.system(f"unset {CF_ACCOUNT}")
    os.system(f"unset {CF_PASSWORD}")
    
def check():
    username = os.environ.get('CF_USERNAME')
    print(username)
    password = os.environ.get('CF_PASSWORD')
    print(password)
    
def main():
    # delete()
    check()
    # make_account()
    pass


if __name__ == "__main__":
    main()