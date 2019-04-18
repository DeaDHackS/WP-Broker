import os
import sys
from urllib.parse import urlparse

# Bruteforcers
import wp_login_bruteforcer
import xmlrpc_bruteforcer

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

print(color.BOLD)

def BANNER():
    banner = r''' __      _____     ___         _           
 \ \    / / _ \___| _ )_ _ ___| |_____ _ _ 
  \ \/\/ /|  _/___| _ \ '_/ _ \ / / -_) '_|
   \_/\_/ |_|     |___/_| \___/_\_\___|_|  
    |-WordPress Scanner & Exploiter-----|                           
    |-Coded By Ghosty / DeaDHackS Team--|'''+'\n'
    print(banner)

def BRUTEFORCE_MAIN_MENU(WEBSITE_TO_SCAN):
    BANNER()
    print("    Target => {DMN.netloc}".format(DMN=urlparse(WEBSITE_TO_SCAN)))
    WARNING_WRITE("All cracked logins are saved into the database and the logs! (Menu > 6)")
    while True:
        print("\n    [1]: Bruteforce wp-login.php")
        print("    [2]: Bruteforce xmlrpc.php")
        print("\n    [98]: Go back")
        print("    [99]: Exit WP-Broker\n")
        BRUTEFORCE_MENU_CHOICE = input("    [WP-Broker@Bruteforce]~[Root] #> ")
        if BRUTEFORCE_MENU_CHOICE == "1":
            USER_FILE = input("    [WP-Broker@Bruteforce] Username File #> ")
            PASS_ILE = input("    [WP-Broker@Bruteforce] Password File #> ")
            wp_login_bruteforcer.BruteforceWplogin(WEBSITE_TO_SCAN, USER_FILE, PASS_ILE)
        elif BRUTEFORCE_MENU_CHOICE == "2":
            USER_FILE = input("    [WP-Broker@Bruteforce] Username File #> ")
            PASS_ILE = input("    [WP-Broker@Bruteforce] Password File #> ")
            xmlrpc_bruteforcer.BruteforceXmlrpc(WEBSITE_TO_SCAN, USER_FILE, PASS_ILE)

        elif BRUTEFORCE_MENU_CHOICE == "98":
            break
        elif BRUTEFORCE_MENU_CHOICE == "99":
            sys.exit()

