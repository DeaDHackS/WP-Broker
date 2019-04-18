import os
import sys
from urllib.parse import urlparse

# Scanners
import scan_dirs
import xmlrpc_scanner

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

def SCANNER_MAIN_MENU(WEBSITE_TO_SCAN):
    BANNER()
    print("    Target => {DMN.netloc}".format(DMN=urlparse(WEBSITE_TO_SCAN)))
    while True:
        print("\n    [1]: Scan For Sensitive Directories / Files")
        print("    [2]: Scan xmlrpc.php For Methods")
        print("\n    [98]: Go back")
        print("    [99]: Exit WP-Broker\n")
        BRUTEFORCE_MENU_CHOICE = input("    [WP-Broker@Scanners]~[Root] #> ")
        if BRUTEFORCE_MENU_CHOICE == "1":
            scan_dirs.ScanDirs(WEBSITE_TO_SCAN)
        if BRUTEFORCE_MENU_CHOICE == "2":
            xmlrpc_scanner.ScanXmlrpc(WEBSITE_TO_SCAN)
        elif BRUTEFORCE_MENU_CHOICE == "98":
            break
        elif BRUTEFORCE_MENU_CHOICE == "99":
            sys.exit()

