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
In settings.py
MONGODB_URL = 'mongodb://localhost:27017/'      # Database url
MONGODB_DB = "craigslist"                       # DB name
MONGODB_COLLECTION_MAIN = "craig"               # MongoDB collection Name
MONGODB_COLLECTION_TEMP = "new_craig"           # MongoDB collection Name

# Email Settings
In settings.py
MAIL_FROM = 'wrufesh@gmail.com'                 # Email from whom?
MAIL_HOST = 'smtp.mandrillapp.com'              # smtp host
MAIL_PORT = 587                                 # smpt port 
MAIL_USER = 'wrufesh@gmail.com'                 # smtp username
MAIL_PASS = '9VUdXY_pRBSJ9bEQtDZdyg'            # smtp password
MAIL_TLS = False                                # Required by some smtp servers
MAIL_SSL = False                                # Required by some smtp servers
# List of recipient
EMAIL_TO = ['wrufesh@gmail.com'

# To run the spider
scrapy crawl craigs

# Deployment


