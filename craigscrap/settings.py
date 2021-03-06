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


MONGODB_SERVER = "localhost"
MONGODB_PORT = 27017
MONGODB_DB = "craigslist"
MONGODB_COLLECTION = "craig"

EXTENSIONS = {
    'craigscrap.email_extension.SendEmail': 1000,
}

# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'craigscrap (+http://www.yourdomain.com)'
