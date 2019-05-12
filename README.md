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

## SystemD integration
To start `wpmon` at system startup, copy the service file into /etc/systemd/system/ and change the path of wpmon
inside it to point to your wpmon directory.

Now, in `wpmon.conf`, add a section with a small name (no spaces please), like `[FOO]` and add options underneath.
All options that are given in the help section are valid (without the leading dashes of course-- for example, `--url`
as a command line argument can be written as `url = https://example.com` in the `config` file. Omitted options (except `url`
are okay, but make sure you have a `[DEFAULT]` section too, so that you can change the built-in defaults to your own.

Now that you have defined your section in `wpmon.conf`, try running it with
```
./wpmon -c FOO
```
or
```
./wpmon --section FOO
```
and check wether it works.

Once you have tuned the options to your liking, just run the following (with `sudo`)
```
systemctl enable wpmonitord@FOO
```
replacing `FOO` with the name of your section.
Now, `systemd` will start this process at startup.
Replacing `enable` with `status`, `start`, `disable` and `stop` will do what they say. Don`t hesitate to explore.
That`s it, maybe I should make a MakeFile or something. But this is not that hard.


Oh, and all the sounds are under Creative Commons license, downloaded from `commons.wikimedia.org`.
Hope it is helpful.

Abilops.
