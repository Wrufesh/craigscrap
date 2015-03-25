# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

from scrapy.exceptions import DropItem
from craigscrap import settings
from scrapy import log
import pdb
# For old version
# import pymongo  
# for pymongo==3.0
from pymongo import MongoClient


class DuplicatesPipeline(object):

    def __init__(self):
        # self.post_detail_links_seen = set()
        # # For older version of pymongo
        # connection = pymongo.Connection(
        #     settings['MONGODB_SERVER'],
        #     settings['MONGODB_PORT']
        # )

        # For pymongo==3.0
        connection = MongoClient(settings.MONGODB_URL)
        db = connection[settings.MONGODB_DB]
        self.collection = db[settings.MONGODB_COLLECTION_MAIN]
        self.new_items = db[settings.MONGODB_COLLECTION_TEMP]

    def process_item(self, item, spider):
        query = self.collection.find({'post_detail_link': item['post_detail_link']})
        if query.count() != 0:
            # if item['post_detail_link'] in self.post_detail_links_seen:
            raise DropItem("Duplicate item found: %s" % item)
        # Only new item
        else:
            # self.post_detail_links_seen.add(item['post_detail_link'])
            self.collection.insert_one(dict(item))
            self.new_items.insert_one(dict(item))
            # pdb.set_trace()
            log.msg("Item added to MongoDB database!",
                    level=log.DEBUG, spider=spider)

            return item
