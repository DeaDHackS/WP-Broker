import os
import sys
import time
import requests
import urllib.request
from urllib.parse import urlparse

global TIMEOUT
global REQUEST_TYPE
TIMEOUT = 0
REQUEST_TYPE = "POST"

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
    global REQUEST_TYPE
    VALID_REQUEST = False
    INFO_WRITE("Checking if XML-RPC is running ...")
    HEADERS = {
        'User-Agent': '''"Mozilla/5.0 (iPod; U; CPU iPhone OS 2_2 like Mac OS X; en-us) AppleWebKit/525.18.1 (KHTML, like Gecko) Version/3.1.1 Mobile/5G77a Safari/525.20"''',
        'Content-Type': 'application/xml',
    }
    try:
        RESPONCE = requests.get(URL+"/xmlrpc.php", headers=HEADERS)
        VALID_REQUEST = True
    except:
        WARNING_WRITE("Error at sending and receiving an HTTP(s) response.")
        RESPONCE = ""
        pass
    if VALID_REQUEST == True:
        if "XML-RPC server accepts" in RESPONCE.content.decode():
            GOOD_WRITE("Getting required HTTP-Request Type ...")
            if "XML-RPC server accepts POST requests only." in RESPONCE.content.decode():
                REQUEST_TYPE = "POST"
            elif "XML-RPC server accepts GET requests only." in RESPONCE.content.decode():
                REQUEST_TYPE = "GET"
            else:
                WARNING_WRITE("Server did not send back HTTP-Request Type, we are assuming its GET.")
                REQUEST_TYPE = "GET"
            GOOD_WRITE("HTTP-Request Type: "+REQUEST_TYPE)
            INFO_WRITE("Grabbing methods ...")
            HEADERS = {
                'User-Agent': '''"Mozilla/5.0 (iPod; U; CPU iPhone OS 2_2 like Mac OS X; en-us) AppleWebKit/525.18.1 (KHTML, like Gecko) Version/3.1.1 Mobile/5G77a Safari/525.20"''',
                'Content-Type': 'application/xml',
            }
            try:
                data = """<?xml version="1.0"?><methodCall><methodName>system.listMethods</methodName><params></params></methodCall>""".encode()
                REQUEST = urllib.request.Request(URL + "/xmlrpc.php", data, headers=HEADERS)
                RESPONCE = urllib.request.urlopen(REQUEST)
                VALID_REQUEST = True
            except:
                WARNING_WRITE("Error at sending and receiving an HTTP(s) response.")
                RESPONCE = ""
                pass
            XML_RESULTS = RESPONCE.read().decode()
            ToReplace = ['<value>', '</value>', '<array>', '</array>', '<data>', '</data>', '<struct>', '</struct>',
                         '<member>', '</member>', '<name>', '</name>', '<boolean>', '</boolean>', '<methodResponse>',
                         '</methodResponse>', '<methodCall>', '</methodCall>', '<param>', '</param>', '<params>', '</params>',
                         '<string>', '</string>', '<?xml', 'version="1.0"', 'encoding', '=', '"UTF-8"', '?>', 'isAdmin1', 'isAdmin0']
            for Str in ToReplace:
                XML_RESULTS = XML_RESULTS.replace(Str, "")
            XML_RESULTS = XML_RESULTS.split()
            print("\n")
            GOOD_WRITE("Displaying all methods in 3 seconds ...")
            time.sleep(3)
            INDEX = 0
            for METHOD in XML_RESULTS:
                INDEX = INDEX + 1
                print("    ["+str(INDEX)+"]: "+METHOD)
            INFO_WRITE("Total Methods: "+str(INDEX))
            return 0
        else:
            return 1
    else:
        return 200

def ScanXmlrpc(WEBSITE_TO_SCAN):
    URL = ""
    DOMAIN = urlparse(WEBSITE_TO_SCAN)
    if DOMAIN.scheme == "https":
        URL = "https://"+DOMAIN.netloc
    elif DOMAIN.scheme == "http":
        URL = "http://"+DOMAIN.netloc
    REQUEST(URL)