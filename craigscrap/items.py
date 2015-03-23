# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class Advertisement(scrapy.Item):
    post_datetime = scrapy.Field()
    post_title = scrapy.Field()
    post_detail_link = scrapy.Field()
    model_year = scrapy.Field()