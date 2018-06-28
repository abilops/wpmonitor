import re
import time
import datetime
import os
import sys
import webbrowser
import urllib
import webbrowser
import ssl
import json
import requests

from colours import *
from argsconfig import *

def log(text):
    if args.quiet == 0 or text.startswith(red):
        printDate()
        print(text)

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
#        for d in args.delta.split(','):
         d = args.delta
         t = re.sub(d, 'Stupid Delta', t)
    return t

# returns HTML text of URL
def opn(url):
    try:
        ctx = ssl.create_default_context()
        if args.insecure == True:
            ctx.check_hostname = False
            ctx.verify_mode = ssl.CERT_NONE
        req = urllib.request.Request(
            url,
            headers={'User-Agent': args.useragent})
        with urllib.request.urlopen(req, context=ctx) as page:
            pageText = page.read().decode('utf-8')
        log(lblue + "Page Downloaded")
        return pageText # <--- Removed str if decode is applied
    except Exception as e:
        log(red + "Cannot open URL. Are you connected to the internet? " + str(e) +  white)
        time.sleep(args.interval/4)
        return '-1'

# is RESPONSIBLE for returning HTML
def getHTML(url):
    pageText = '-1'
    while pageText == '-1':
        pageText = opn(url)
    return stripStupidDeltas(pageText)

def wait(interval):
    if args.quiet != 0:
        print("Waiting for {} more seconds...".format(interval), flush=True)
        time.sleep(interval)
    else:
        for x in range(interval, 0, -1):
            print(clearline + "Waiting for {} more seconds...".format(x), end='', flush=True)
            time.sleep(1)
        print(clearline, end='')

def printHeader(interval, fname):
    if args.quiet != 0:
        return
    os.system('/usr/bin/clear')
    print("%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%")
    print(green + "WEBPAGE MONITOR v1.0" + white)
    print(green + "Not refreshing any more!!" + white)
    print("URL: " + lblue + args.url + white)
    print("Interval: " + lblue + str(interval) + " seconds" + white)
    print("File: " + lblue + fname + white)
    print("%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%")

def getAttentionAndBrowser(url):
    if args.headless == False:
        # Turn on the screen
        os.system("/usr/bin/xset dpms force on")        
        os.system("/usr/bin/espeak 'Alert! Webpage has changed.' &")
        notify('Webpage Monitor', args.url + ' has changed. Opening in new browser tab.\nFingers crossed!')
        webbrowser.open_new_tab(args.url)
