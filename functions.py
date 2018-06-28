import re
import datetime
import time
import os
import sys
import webbrowser
from argsconfig import *

def printDate():
    print(str(datetime.datetime.now()), end='-')


def checkEmail(email):
    if email != None:
        if re.search('^[a-zA-Z0-9_\.]+@[A-Za-z0-9]+\.[a-z]{2,3}$', email) == None:
            log(red + "Invalid email address. Retry" + white)
#           exit()

def readFile(path):
    try:
        with open(path, 'rb') as f:
            return f.read().decode('utf-8')
    except:
        return None

def writeFile(path, content):
    try:
        with open(path, 'w') as f:
            f.write(content)
            return 0
    except:
        return None

def stripStupidDeltas(t):
    if args.delta != None:
        for d in args.delta:
#        t = re.sub("<div>[\S\s]*.*quotes.*</div>", 'Stupid Quote', t)
            t = re.sub(d, 'Stupid Delta', t)
    return t

