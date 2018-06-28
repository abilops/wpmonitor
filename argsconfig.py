import argparse
import configparser

def getOptions():
    config = configparser.ConfigParser()
    config.read('defaults.conf')
    config.read('wpmon.conf')

    parser = argparse.ArgumentParser(description='Monitor a webpage by repeatedly checking URL after intervals')
    parser.add_argument('-c', '--section', help='Use preset section from configuration file `wpmon.conf`', required=False, default='DEFAULT')
    args = parser.parse_known_args()
    sec = config[args[0].section]
    if (sec.get( 'url', None) != None):
    	url_req = False
    else:
        parser.add_argument('url', help='URL to page that will be monitored')
    parser.add_argument('-u', '--url', help='URL to page that will be monitored', required=url_req)
    parser.add_argument('-i', '--interval', default=60, help='Seconds to wait between successive checks', type=int, required=False)
    parser.add_argument('-f', '--filename', help='Name of the file to store the downloaded template webpage (first one). Default is URL', required=False, default=None)
    parser.add_argument('-s', '--sound', help='Location of sound file to be played', default='sounds/Smoke_alarm.wav', required=False)
    parser.add_argument('-q', '--quiet', help='Supress non-red output', type=int, default=0, required=False)
    parser.add_argument('-m', '--email', help='Send an email as alert instead of sound, browser, nextscript and colour', default=None, required=False)
    parser.add_argument('-n', '--next', help='Script file to run after webpage has changed', default=None, required=False)
    parser.add_argument('-k', '--insecure', help="Don't check website certificates. Good for indian gov websites", required=False, action='store_true')
    parser.add_argument('-M', '--trymail', help="Don't send actual email. Just simulate", required=False, action='store_true')
    parser.add_argument('-H', '--headless', help="Headless mode", required=False, default=False, action='store_true')
    parser.set_defaults(**config[args[0].section])
    return parser.parse_args()
