import scrapy
from craigscrap.items import Advertisement


def make_url_list(raw_urls):
    new_urls = []
    for url in raw_urls:
        splitted_url = url.split('/')
        splitted_name = splitted_url[2].split('.')
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
        item_urls = make_url_list(sel)
        for item_url in item_urls:
            yield scrapy.Request(item_url, self.parse_item)

    # in middle in case of many pages

    def parse_item(self, response):
        # from scrapy.shell import inspect_response
        # inspect_response(response)
        item = Advertisement()
        detail_link_prefix = 'http://' + response.url.split('/')[2]
        selectors = response.xpath('//div[@class="content"]/p[@class="row"]')
        for sel in selectors:
            item['post_datetime'] = sel.xpath('//span[@class="pl"]/time/@datetime').extract()[0]
            item['post_title'] = sel.xpath('//span[@class="pl"]/a/text()').extract()[0]
            detail_link = detail_link_prefix + sel.xpath('//span[@class="pl"]/a/@href').extract()[0]
            item['post_detail_link'] = detail_link
            item['price'] = sel.xpath('//span[@class="l2"]/span[@class="price"]/text()').extract()[0]
            # yield item
            yield scrapy.Request(detail_link, self.parse_item_details, meta={'item': item})

    def parse_item_details(self, response):
        # from scrapy.shell import inspect_response
        # inspect_response(response)
        item = response.meta['item']
        item['model_year'] = response.xpath('//p[@class="attrgroup"]/span')[0].xpath('b/text()').extract()[0]
        return item