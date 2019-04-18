import os
import sys
import time
import requests
from urllib.parse import urlparse

global TIMEOUT
TIMEOUT = 0

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

def REQUEST(URL, PATH):
    global TIMEOUT
    VALID_REQUEST = False
    HEADERS = {
        "User-Agent": "Mozilla/5.0 (iPod; U; CPU iPhone OS 2_2 like Mac OS X; en-us) AppleWebKit/525.18.1 (KHTML, like Gecko) Version/3.1.1 Mobile/5G77a Safari/525.20",
    }
    try:
        RESPONCE = requests.post(URL+PATH, headers=HEADERS, allow_redirects=False)
        VALID_REQUEST = True
    except:
        WARNING_WRITE("Error at sending and receiving an HTTP(s) response, adding timeout of 1 second...")
        TIMEOUT = TIMEOUT + 1
        RESPONCE = ""
        pass
    if VALID_REQUEST == True:
        RAW_CODE = RESPONCE.status_code
        if RAW_CODE == 200:
            GOOD_WRITE(PATH+" - 200")
            return 0
        else:
            WARNING_WRITE(PATH+" - "+str(RAW_CODE))
    return 200

def ScanDirs(WEBSITE_TO_SCAN):
    WP_DIR = ['/robots.txt','/wp-admin/','/wp-includes/','/wp-content/','/wp-content/plugins/','/wp-content/themes/','/wp-content/uploads', '/wp-login.php','/xmlrpc.php','/wp-config.php']
    URL = ""
    DOMAIN = urlparse(WEBSITE_TO_SCAN)
    if DOMAIN.scheme == "https":
        URL = "https://"+DOMAIN.netloc
    elif DOMAIN.scheme == "http":
        URL = "http://"+DOMAIN.netloc
    INFO_WRITE("Common HTTP Code List & Description:")
    print("       200       - OK          - The request was successful!")
    print("       302 / 301 - REDIRECTION - The request was redirected to another URL.")
    print("       404       - NOT FOUND   - Path don't exist on the remote host.")
    print("       403       - FORBIDDEN   - Authentication is needed such as Admin or User.")
    print("       Need More? Check that out: https://flaviocopes.com/http-status-codes/\n")
    INFO_WRITE("PATH - HTTP STATUS CODE")
    for ToCheck in WP_DIR:
        REQUEST(URL, ToCheck)