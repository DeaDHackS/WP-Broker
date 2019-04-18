import os
import sys
import requests
from urllib.parse import urlparse
import time

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
    GOT_CODE = False
    VALID_CODE = False
    HEADERS = {
        'User-Agent': '''"Mozilla/5.0 (iPod; U; CPU iPhone OS 2_2 like Mac OS X; en-us) AppleWebKit/525.18.1 (KHTML, like Gecko) Version/3.1.1 Mobile/5G77a Safari/525.20"''',
    }
    try:
        RESPONCE = requests.get(URL, headers=HEADERS)
        VALID_REQUEST = True
    except:
        WARNING_WRITE("Error at sending and receiving an HTTP(s) response, adding timeout of 1 second...")
        TIMEOUT = TIMEOUT + 1
        RESPONCE = ""
        pass
    if VALID_REQUEST == True:
        if RESPONCE.status_code == 200 and VALID_REQUEST and GOT_CODE == False:
            VALID_CODE = True
            GOT_CODE = True
            return 0
        elif "/xmlrpc.php" in URL:
            if "XML-RPC server accepts" in RESPONCE.content.decode():
                return 10
        elif RESPONCE.status_code == 403 and VALID_REQUEST == True and GOT_CODE == False:
            GOT_CODE = True
            return 1
        elif RESPONCE.status_code == 404 and VALID_REQUEST == True and GOT_CODE == False:
            GOT_CODE = True
            return 2
        elif VALID_REQUEST == True and GOT_CODE == False:
            return 100
    else:
        return 200

def IsItWP(WEBSITE_TO_SCAN):
    global TIMEOUT
    WP_DIR_LIST = ['/wp-admin/', '/wp-content/', '/wp-includes/', '/wp-config.php', '/wp-login.php', '/wp-settings.php', '/wp-load.php', '/xmlrpc.php']
    DOMAIN = urlparse(WEBSITE_TO_SCAN)
    CONFIDENCE_PERCENTAGE = 0
    if DOMAIN.scheme == "https":
        WEBSITE_TO_SCAN = "https://"+DOMAIN.netloc
    else:
        WEBSITE_TO_SCAN = "http://"+DOMAIN.netloc
    INFO_WRITE("Checking if '{DMN.netloc}' is running WordPress ...".format(DMN=DOMAIN))
    for URL_PATH in WP_DIR_LIST:
        time.sleep(TIMEOUT)
        REQ = REQUEST(WEBSITE_TO_SCAN+URL_PATH)
        if REQ == 0 or REQ == 10:
            CONFIDENCE_PERCENTAGE = CONFIDENCE_PERCENTAGE + 15
        elif REQ == 1:
            CONFIDENCE_PERCENTAGE = CONFIDENCE_PERCENTAGE + 5
        elif REQ == 2:
            CONFIDENCE_PERCENTAGE = CONFIDENCE_PERCENTAGE - 5
    if CONFIDENCE_PERCENTAGE >= 100 or CONFIDENCE_PERCENTAGE >= 70:
        GOOD_WRITE("Confidence: 100% / WordPress confirmed!")
    elif CONFIDENCE_PERCENTAGE >= 40:
        WARNING_WRITE("Confidence: "+str(CONFIDENCE_PERCENTAGE)+"%")
    elif not CONFIDENCE_PERCENTAGE == 0:
        ERROR_WRITE("Confidence: 0%")
    else:
        ERROR_WRITE("Confidence: "+str(CONFIDENCE_PERCENTAGE)+"%")