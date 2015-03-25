from scrapy import signals
from scrapy.exceptions import NotConfigured
from scrapy.mail import MailSender
from craigscrap import settings
from pymongo import MongoClient
import pdb


class SendCraigsEmail(object):

    def __init__(self):
        connection = MongoClient(settings.MONGODB_URL)
        self.db = connection[settings.MONGODB_DB]
        self.new_items = self.db[settings.MONGODB_COLLECTION_TEMP]
        self.mailer = MailSender(settings.MAIL_HOST,
                                 settings.MAIL_FROM,
                                 settings.MAIL_USER,
                                 settings.MAIL_PASS,
                                 settings.MAIL_PORT,
                                 settings.MAIL_TLS,
                                 settings.MAIL_SSL
                                 )
        self.to = ['wrufesh@gmail.com']
        # pdb.set_trace()

    @classmethod
    def from_crawler(cls, crawler):
        if not crawler.settings.getbool('MYEXT_ENABLED'):
            raise NotConfigured

        ext = cls()
        crawler.signals.connect(ext.send_mail, signal=signals.spider_closed)
        return ext

    def send_mail(self, spider):
        # pdb.set_trace()
        # self.get_body_msg()
        self.mailer.send(to=self.to,
                         subject="New Car And Trucks From California",
                         body=self.get_body_msg(),
                         cc=["another@example.com"],
                         mimetype='html/html'
                         )
        spider.log("Mail Send to registered users")
        self.db.drop_collection(settings.MONGODB_COLLECTION_TEMP)
        spider.log("New Items Dropped")

    def get_body_msg(self):
        msg = '<h1>New Cars And Trucks from California </h1></br>'
        for i in self.new_items.find():
            time = i['post_datetime'].strftime('%d<sup>th</sup> of %B,%Y - %H:%M')
            post_title = i['post_title']
            location = i['location']
            price = i['price']
            link = i['post_detail_link']
            # pdb.set_trace()
            msg = msg + '<ul><li>' + time + '</li><li><a href="' + link + '"><b>' + post_title + '</b></a></li><li>' + location + '</li><li>' + price + '</li></ul><hr>'

            # pdb.set_trace()
        return msg
