import re

def strongPWDetection():

    Length=re.compile(r'[0-9a-zA-Z]{8,}')
    CW=re.compile(r'[A-Z]')
    SW=re.compile(r'[a-z]')
    Num=re.compile(r'[0-9]')
    loop=True
    while(loop):
        print('Enter your new Password:')
        PassWord=input()
        if Length.search(PassWord) and CW.search(PassWord) and SW.search(PassWord) and Num.search(PassWord):
            print('Password Accepted')
            loop=False
        else:
            print('Password is too weak')
    return None

strongPWDetection()
