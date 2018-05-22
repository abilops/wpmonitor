#Webpage Monitor

Monitors the webpage the given url points to.

Has a lot of things up its sleeve to tell alert you when the webpage changes.
It will notify you, play a sound endlessly, open the browser to that page
or even send you an email.

Does not work:
- With cookies
- With logins
- Time displays on webpages
- on Windows

Working on that (except the Windows part).

##Installation guide
It's nothing. Just download the zip or clone the repo and then run
```
./wpmon http://www.example.com
```
For default help from `argparser`,
```
./wpmon -h
```
You'll have to set up a Mailgun or some other email provider and enter the API keys and stuff
in the `wpmon.conf`. Don't forget to rename `wpmon.sample.conf` as `wpmon.conf`.

Oh, and all the sounds are under Creative Commons license, downloaded from `commons.wikimedia.org`.
Hope it is helpful.

Abilops.
