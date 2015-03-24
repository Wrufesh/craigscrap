from scrapy import signals
from scrapy.exceptions import NotConfigured
from scrapy.mail import MailSender
import pdb


class SendEmail(object):

    pdb.set_trace()
    def __init__(self):
        self.frm = 'wrufesh@gmail.com'
        self.to = 'a@f.com, b@g.com'

    @classmethod
    def from_crawler(cls, crawler):
        if not crawler.settings.getbool('MYEXT_ENABLED'):
            raise NotConfigured

        ext = cls()

        # crawler.signals.connect(ext.spider_opened, signal=signals.spider_opened)
        crawler.signals.connect(ext.send_mail, signal=signals.spider_closed)

        return ext

    def send_mail(self, spider):
        spider.log("Are you getting the message?")

    def spider_opened(self, spider):
        spider.log("opened spider HAHAHAHAHA %s" % spider.name)
