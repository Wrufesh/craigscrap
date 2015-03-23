import scrapy
import re
from craigscrap.items import Advertisement


def make_url_list(raw_urls):
    new_urls = []
    for url in raw_urls:
        splitted_url = re.split('/', url)
        splitted_name = re.split('.', splitted_url[2])
        place_name = splitted_name[0]
        new_url = 'http://' + place_name + '.craigslist.org/search/cto?autoMakeModel=ford+ranger&autoMinYear=2005'
        new_urls.append(new_url)  
    return new_urls


class CraigSpider(scrapy.Spider):
    name = 'craigs'
    allowed_domains = ['craigslist.org']
    start_urls = ['http://geo.craigslist.org/iso/us/ca']

    def parse(self, response):
        sel = response.xpath('//div[@id="postingbody"]/blockquote/blockquote/ul/li/a/@href').extract()
        # from scrapy.shell import inspect_response
        # inspect_response(response)
        
        pass


   