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

def REQUEST(URL):
    global TIMEOUT
    VALID_REQUEST = False
    HEADERS = {
        "User-Agent": "Mozilla/5.0 (iPod; U; CPU iPhone OS 2_2 like Mac OS X; en-us) AppleWebKit/525.18.1 (KHTML, like Gecko) Version/3.1.1 Mobile/5G77a Safari/525.20",
    }
    try:
        RESPONCE = requests.post(URL, headers=HEADERS, allow_redirects=False)
        VALID_REQUEST = True
    except:
        WARNING_WRITE("Error at sending and receiving an HTTP(s) response, adding timeout of 1 second...")
        TIMEOUT = TIMEOUT + 1
        RESPONCE = ""
        pass
    if VALID_REQUEST == True:
        RAW_HEADERS = RESPONCE.headers
        VALID_SERVER = False
        VALID_POWERED_BY = False
        try:
            d = RAW_HEADERS['Server']
            VALID_SERVER = True
        except:
            VALID_SERVER = False
        try:
            d = RAW_HEADERS['X-Powered-By']
            VALID_POWERED_BY = True
        except:
            VALID_POWERED_BY = False
        if VALID_SERVER == True:
            GOOD_WRITE("Server: "+RAW_HEADERS['Server'])
        else:
            GOOD_WRITE("Server: Cannot Be Checked / Unknown")
        if VALID_POWERED_BY == True:
            GOOD_WRITE("Powered By: "+RAW_HEADERS['X-Powered-By'])
        else:
            GOOD_WRITE("Powered By: Cannot Be Checked / Unknown")
    return 200

def GetInfo(WEBSITE_TO_SCAN):
    URL = ""
    DOMAIN = urlparse(WEBSITE_TO_SCAN)
    if DOMAIN.scheme == "https":
        URL = "https://"+DOMAIN.netloc
    elif DOMAIN.scheme == "http":
        URL = "http://"+DOMAIN.netloc
    REQUEST(URL)