from scrapy import signals
from scrapy.exceptions import NotConfigured
from scrapy.mail import MailSender
from craigscrap import settings
import pdb


class SendCraigsEmail(object):

    def __init__(self):
    	pdb.set_trace()
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
        pdb.set_trace()
        self.mailer.send(to=self.to,
                         subject="New Car And Trucks From California",
                         body="Here will be the list",
                         cc=["another@example.com"])
        spider.log("Mail Send to registered users")


