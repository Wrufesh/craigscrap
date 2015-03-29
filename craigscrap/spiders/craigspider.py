import datetime
from craigscrap.items import Advertisement
from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors import LinkExtractor


def modify_url(raw_url):
    splitted_url = raw_url.split('/')
    splitted_name = splitted_url[2].split('.')
    place_name = splitted_name[0]
    new_url = 'http://' + place_name + '.craigslist.org/search/cto?autoMakeModel=ford+ranger&autoMinYear=2005'
    return new_url


def to_datetime_object(date_str):
    return datetime.datetime.strptime(date_str, "%Y-%m-%d %H:%M")


class CraigSpider(CrawlSpider):
    name = 'craigs'
    allowed_domains = ['craigslist.org']
    start_urls = ['http://geo.craigslist.org/iso/us/ca']
    download_delay = 3
    rules = (
           Rule(LinkExtractor(restrict_xpaths=('//div[@id="postingbody"]/blockquote/blockquote/ul/li/a',),
                              process_value=modify_url,
                              ),
                callback='parse_item',
                follow=True
                ),
           Rule(LinkExtractor(restrict_xpaths=('//a[@class="button next"]',),
                              # process_value=modify_u,
                              ),
                callback='parse_item',
                follow=True
                ),
           )

    def parse_item(self, response):
        # from scrapy.shell import inspect_response
        # inspect_response(response)
        location = response.url.split('/')[2].split('.')[0]
        detail_link_prefix = 'http://' + response.url.split('/')[2]
        selectors = response.xpath('//span[@class="pl"]')
        items = []
        for sel in selectors:
            item = Advertisement()
            date_str = sel.xpath('//span[@class="pl"]/time/@datetime').extract()[0]
            item['post_datetime'] = to_datetime_object(date_str)
            item['post_title'] = sel.xpath('a/text()').extract()[0]
            extracted_link = sel.xpath('a/@href').extract()[0]

            # Check whether the url is absolute or relative as it varies
            if extracted_link.split('/')[0] == u'http:':
                detail_link = extracted_link
            else:
                detail_link = detail_link_prefix + extracted_link

            item['post_detail_link'] = detail_link
            price = sel.xpath('following-sibling::*/span[@class="price"]/text()').extract()
            if len(price) != 0:
                item['price'] = price[0]
            else:
                item['price'] = 'Not Mentioned'
            item['location'] = location
            items.append(item)
        return items
