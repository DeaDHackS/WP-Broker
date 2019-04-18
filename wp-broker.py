import os
import sys
from urllib.parse import urlparse

# Bruteforcers
sys.path.insert(0, "bruteforcers")
import bruteforce_main

# Database
sys.path.insert(0, "database")
import database_main

# Exploits
sys.path.insert(0, "exploits")
import exploits_main

# Informations
sys.path.insert(0, "informations")
import informations_main

# Scanners
sys.path.insert(0, "scanners")
import wordpress_scanner
import scanners_main

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

print(color.BOLD)

def CLEAR():
    if "nt" in os.name:
        os.system("cls")
    else:
        os.system("clear")

def BANNER():
    banner = r''' __      _____     ___         _           
 \ \    / / _ \___| _ )_ _ ___| |_____ _ _ 
  \ \/\/ /|  _/___| _ \ '_/ _ \ / / -_) '_|
   \_/\_/ |_|     |___/_| \___/_\_\___|_| V.1  
    |-WordPress Scanner & Exploiter-----|                           
    |-Coded By Ghosty / DeaDHackS Team--|'''+'\n'
    print(banner)

def MAIN_MENU(WEBSITE_TO_SCAN):
    print("    Target => {DMN.netloc}".format(DMN=urlparse(WEBSITE_TO_SCAN)))
    while True:
        print("\n    [1]: Is It WordPress?")
        print("    [2]: Bruteforce Menu")
        print("    [3]: Exploitation Menu")
        print("    [4]: Information Menu")
        print("    [5]: Scanner Menu")
        print("    [6]: WP-Broker-Database Management Menu")
        print("\n    [99]: Exit WP-Broker\n")
        MAIN_MENU_CHOICE = input("    [WP-Broker]~[Root] #> ")
        if MAIN_MENU_CHOICE == "1":
            wordpress_scanner.IsItWP(WEBSITE_TO_SCAN)
        elif MAIN_MENU_CHOICE == "2":
            CLEAR()
            bruteforce_main.BRUTEFORCE_MAIN_MENU(WEBSITE_TO_SCAN)
            CLEAR()
            BANNER()
        elif MAIN_MENU_CHOICE == "3":
            CLEAR()
            exploits_main.EXPLOIT_MAIN_MENU(WEBSITE_TO_SCAN)
            CLEAR()
            BANNER()
        elif MAIN_MENU_CHOICE == "4":
            CLEAR()
            informations_main.INFORMATION_MAIN_MENU(WEBSITE_TO_SCAN)
            CLEAR()
            BANNER()
        elif MAIN_MENU_CHOICE == "5":
            CLEAR()
            scanners_main.SCANNER_MAIN_MENU(WEBSITE_TO_SCAN)
            CLEAR()
            BANNER()
        elif MAIN_MENU_CHOICE == "6":
            CLEAR()
            database_main.DATABASE_MAIN_MENU()
            CLEAR()
            BANNER()


def MAIN():
    BANNER()
    WEBSITE_TO_SCAN = input("[WP-Broker] Target URL #> ")
    CLEAR()
    BANNER()
    MAIN_MENU(WEBSITE_TO_SCAN)
MAIN()


