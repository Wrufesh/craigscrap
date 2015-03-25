# craigscrap
craiglist scrapper

# Requirements
Scrapy==0.24.5
Twisted==15.0.0
pymongo==3.0
scrapyd==1.0.1

# Install Craigscrap
pip install git+https://github.com/Wrufesh/craigscrap.git@clean1

# Database Setting
In craigscrap/settings.py
MONGODB_URL = 'mongodb://localhost:27017/'      # Database url
MONGODB_DB = "craigslist"                       # DB name
MONGODB_COLLECTION_MAIN = "craig"               # MongoDB collection Name
MONGODB_COLLECTION_TEMP = "new_craig"           # MongoDB collection Name

# Email Settings
In craigscrap/settings.py
MAIL_FROM = 'wrufesh@gmail.com'                 # Email from whom?
MAIL_HOST = 'smtp.mandrillapp.com'              # smtp host
MAIL_PORT = 587                                 # smpt port 
MAIL_USER = 'wrufesh@gmail.com'                 # smtp username
MAIL_PASS = '9VUdXY_pRBSJ9bEQtDZdyg'            # smtp password
MAIL_TLS = False                                # Required by some smtp servers
MAIL_SSL = False                                # Required by some smtp servers
# List of recipient
EMAIL_TO = ['wrufesh@gmail.com'

# Run the spider by the following command
scrapy crawl craigs

# Deployment
Configure scrapyd
  Scrapyd searches for configuration files in the following locations, and parses them in order with the latest one taking more priority:

    /etc/scrapyd/scrapyd.conf (Unix)
    c:\scrapyd\scrapyd.conf (Windows)
    /etc/scrapyd/conf.d/* (in alphabetical order, Unix)
    scrapyd.conf
    ~/.scrapyd.conf (users home directory)
    
    In configuration file set  
    poll_interval = 1800     # 1800 sec = 3o min, Default is 5(in sec)


Setup deployment sever
  In scrapy.cfg
  
  [settings]
  default = craigscrap.settings

  [deploy:<somename>]
  #url = http://localhost:6800/     # Deployment Server address
  project = craigscrap              # project name
  username = john
  password = secret
  version = HG
  
  Now run the following command:
  scrapyd deploy <somename>
  
Run and control spider.
  scrapyd provides nice JSON API to run and control spiders.
  
Run the following command to run the spider from remote
http://localhost:6800/schedule.json -d project=craigscap -d spider=craigs
assuming
project name = craigscrap
spider name = craigs
and server is localhost:6800

For more controls from JSON API get through following:
http://scrapyd.readthedocs.org/en/latest/api.html






