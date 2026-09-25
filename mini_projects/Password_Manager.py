# password manager - organise and store your passwords

import os
from cryptography.fernet import Fernet # pip install cryptography

# key + password + text to encrypt = random text
# random text + key + password = text to encrypt

# ----------- 1st funstion to create a key
def write_key ():
    key = Fernet.generate_key()
    with open ("key.key", "wb") as key_file: # write in bytes special file format
        key_file.write(key)

# FIX: write_key() was commented out, so on a fresh computer key.key didn't exist and
# load_key() crashed with FileNotFoundError. Now we create the key only if it's missing -
# never overwrite an existing key, or every saved password becomes unreadable.
if not os.path.exists("key.key"):
    write_key()

# 2nd function to store a key
def load_key():
    with open ("key.key" , "rb") as file: # read in bytes; `with` closes the file for us
        key = file.read()
    return key

# master_pwd = input ("What is the Master Password?: ") # not validate , it is to encrpyt the stored pwds and allow of stop access.
key = load_key() # + master_pwd.encode
fer = Fernet (key)

def  view (): # function is an excutable, reuseable block of a code.
    # FIX: choosing "view" before any password was added crashed with FileNotFoundError
    if not os.path.exists("passwords.txt"):
        print("No passwords saved yet.")
        return
    with open("passwords.txt" , "r") as f:  # "f" is just a short variable name for the open file - any name works
        for line in f.readlines():
            data = line. rstrip() # rstrip() removes the "\n" (and spaces) from the END of the line
            user, passw = data.split(" | ") # split cuts the line into a list at every " | " -> [name, encrypted_password]
            # FIX: split on " | " (with spaces) to match what add() writes, so names don't carry a trailing space
            # print ("User: " , user, " | Password: ", passw) # what is this?
            print ("User: " , user, " | Password: ", fer.decrypt(passw.encode()).decode())

def add():
    name = input("Account Name: ")
    pwd = input ("Password: ")

    with open("passwords.txt" , "a") as f: # using "with" will automatically close the file at the end. 
        # we can use file = open() but then it has to be manyally closed file()
        # a mode - pen mode add something at the end of the file if exists already otherwise creates one if one does not exist already
        # w mode - overwrite or create but will remove old file
        # r mode - read only 
        f.write (name + " | " + fer.encrypt(pwd.encode()).decode() + "\n")
        # why "f" ?
        # "\n" is for - line break

while True:

    mode = input ("Would you like to add a new password or view existing ones (view, add), press Q to quit: " ).lower() # to convert text in lower caps
    if mode == "q":
        break #  quit the programme
        
    if mode == "view":
        view() # calling view function
        
    elif mode == "add":
        add() # calling add function
    else:
        print("Invalid entry.")
        continue
