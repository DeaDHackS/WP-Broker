import os
import sys

class color:
    PURPLE = '\033[95m'
    CYAN = '\033[96m'
    DARKCYAN = '\033[36m'
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    END = '\033[0m'

def GOOD_WRITE(TEXT):
    print(color.GREEN+"    [+] "+color.END+TEXT)

def INFO_WRITE(TEXT):
    print(color.BLUE+"    [i] "+color.END+TEXT)

def ERROR_WRITE(TEXT):
    print(color.RED+"    [-] "+color.END+TEXT)

def WARNING_WRITE(TEXT):
    print(color.YELLOW+"    [!] "+color.END+TEXT)

def ReadDB():
    ACC_CRACK_FILE = open("database/cracked_accounts.txt", "r")
    ACCOUNTS = []
    INDEX = 0
    for ACCOUNT in ACC_CRACK_FILE.readlines():
        ACCOUNTS.append(ACCOUNT)
    if len(ACCOUNTS) == 0:
        ERROR_WRITE("Database is empty.")
    else:
        for ACCOUNT in ACCOUNTS:
            INDEX = INDEX + 1
            print("    " + str(INDEX) + ". " + ACCOUNT)

def ClearDB():
    os.remove("database/cracked_accounts.txt")
    DB_FILE = open("database/cracked_accounts.txt", "w+")
    DB_FILE.write("")
    DB_FILE.close()
    GOOD_WRITE("Database is cleared!")