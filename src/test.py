import os

def main():
    account = os.environ.get('CF_ACCOUNT')
    
    print(account)

if __name__ == '__main__':
    main()