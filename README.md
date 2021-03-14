##   FORK AT YOUR OWN RISK

#    Deploy


[![Deploy To Heroku](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy?template=https://github.com/B-Lac/B-Lac-Userbot)


#   String Session


[![Run on Repl.it](https://repl.it/badge/github/STARKGANG/friday)](https://repl.it/@pawanjatt/B-Lacuserbot#main.py)


##   The Normal Way
   Simply clone the repository and run the main file:

# The Normal Way

Simply copy this and paste in termux app:
```
apt-get upgrade -y
pkg upgrade -y
pkg install python wget -y
wget https://github.com/B-Lac/B-Lac-Userbot/blob/master/telesetup.py
pip install telethon
python telesetup.py
```

class Development(Var):
  APP_ID = 1215061
  API_HASH = "eb06d4abfb49dc3eeb1aeb98ae0f581e"



Heroku Configuration
Simply just leave the Config as it is.


Local Configuration
Fortunately there are no Mandatory vars for the UniBorg Support Config.

# Mandatory Vars
```
[+] Only two of the environment variables are mandatory.

[+] This is because of telethon.errors.rpc_error_list.ApiIdPublishedFloodError

    [-] APP_ID:   You can get this value from https://my.telegram.org
    [-] API_HASH :   You can get this value from https://my.telegram.org
    
[+] The b lac will not work without setting the mandatory vars.
```
