import scrapy
import datetime
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


# def get_paginated_url(string_data, url):
#     url_list = []
#     x = string_data.split(' ')
#     if len(x) == 5:
#         total_items = int(x[4])
#         total_loop = total_items/100
#         for i in range(0, total_loop):
#             v = str(i * 100)
#             url_list.append(url + '&s=' + v)
#     else:
#         url_list.append(url)
#     return url_list


def to_datetime_object(date_str):
    return datetime.datetime.strptime(date_str, "%Y-%m-%d %H:%M")


class CraigSpider(scrapy.Spider):
    name = 'craigs'
    allowed_domains = ['craigslist.org']
    start_urls = ['http://geo.craigslist.org/iso/us/ca']

    def parse(self, response):
        sel = response.xpath('//div[@id="postingbody"]/blockquote/blockquote/ul/li/a/@href').extract()
        item_urls = make_url_list(sel)
        for item_url in item_urls:
            # pdb.set_trace()
            yield scrapy.Request(item_url, self.parse_item)
            # yield scrapy.Request(item_url, callback=self.pagination_check)

    # in middle in case of many pages
    # def pagination_check(self, response):
    #     url = response.url
    #     # from scrapy.shell import inspect_response
    #     # inspect_response(response)
    #     range_data = response.xpath('//div[@class="toc_legend"]//span[@class="range"]/text()').extract()[0]
    #     p_urls = get_paginated_url(range_data, url)
    #     for p_url in p_urls:
    #         scrapy.log.msg(p_url)
    #         yield scrapy.Request(p_url, callback=self.parse_item)

    def parse_item(self, response):
        # from scrapy.shell import inspect_response
        # inspect_response(response)
        item = Advertisement()
        location = response.url.split('/')[2].split('.')[0]
        detail_link_prefix = 'http://' + response.url.split('/')[2]
        selectors = response.xpath('//span[@class="pl"]')
        # pdb.set_trace()
        for sel in selectors:
            date_str = sel.xpath('//span[@class="pl"]/time/@datetime').extract()[0]
            item['post_datetime'] = to_datetime_object(date_str)
            item['post_title'] = sel.xpath('a/text()').extract()[0]
            extracted_link = sel.xpath('a/@href').extract()[0]

            # Check whether the url is absolute or relative as it varies
            # pdb.set_trace()
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
            yield item
            # yield scrapy.Request(detail_link, self.parse_item_details, meta={'item': item})

    # def parse_item_details(self, response):
    #     # from scrapy.shell import inspect_response
    #     # inspect_response(response)
    #     item = response.meta['item']
    #     item['model_year'] = response.xpath('//p[@class="attrgroup"]/span')[0].xpath('b/text()').extract()[0]
    #     return item