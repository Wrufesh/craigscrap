# -*- coding: utf-8 -*-

# Scrapy settings for craigscrap project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#

BOT_NAME = 'craigscrap'

SPIDER_MODULES = ['craigscrap.spiders']
NEWSPIDER_MODULE = 'craigscrap.spiders'


ITEM_PIPELINES = {
    'craigscrap.pipelines.DuplicatesPipeline': 100,
    # 'craigscrap.pipelines.MongoDBPipeline':200,
    # 'myproject.pipelines.JsonWriterPipeline': 800,
}

# MongoDB setting
# MONGODB_SERVER = "localhost"
# MONGODB_PORT = 27017
MONGODB_URI = 'mongodb://localhost:27017/'
MONGODB_DB = "craigslist"
MONGODB_COLLECTION_MAIN = "craig"
MONGODB_COLLECTION_TEMP = "new_craig"

# For extensions
MYEXT_ENABLED = True
EXTENSIONS = {
    'craigscrap.email_extension.SendCraigsEmail': 60,
}

# This set of variables will try to prevent IP Block
DOWNLOAD_DELAY = 3
COOKIES_ENABLED = False

# Email settings
MAIL_FROM = 'wrufesh@gmail.com'
MAIL_HOST = 'smtp.mandrillapp.com'
MAIL_PORT = 587
MAIL_USER = 'wrufesh@gmail.com'
MAIL_PASS = '9VUdXY_pRBSJ9bEQtDZdyg'
MAIL_TLS = False
MAIL_SSL = False

# List of recipient.
EMAIL_TO = ['wrufesh@gmail.com']


# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'craigscrap (+http://www.yourdomain.com)'
