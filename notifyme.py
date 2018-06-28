import os

def notify(title, text):
    os.system("/usr/bin/notify-send '" + re.escape(title) + "' '"+ re.escape(text) + "'")

def send_message(towhom, subject, text, html):
    if args.trymail == True:
        return writeFile('mail{}'.format(datetime.datetime.now()),towhom[0]+subject)
    return requests.post(
        config.get('DEFAULT','email_posturl'),
        auth=(config.get('DEFAULT', 'email_auth_username'), config.get('DEFAULT', 'email_auth_key')),
        data={"from": config.get('DEFAULT', 'email_from'),
              "to": towhom,
              "subject": subject,
              "text": text,
              "html": html})

def sendPush(text):
   hdr = {'Authorization': config.get('DEFAULT','push_token'), 'Content-Type': 'application/json'}
   payload = {'body':text, 'message_type': 'text/plain'}
   url = config.get('DEFAULT', 'push_url')
   r = requests.post(url, headers=hdr, data=json.dumps(payload))
   return r.text

