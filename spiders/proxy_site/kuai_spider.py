from lxml import etree
from spiders import BaseSpider
from utils import exception_logging


class KuaiSpider(BaseSpider):
    """ 快代理爬虫 """
    def __init__(self):
        self._base_url = 'https://www.kuaidaili.com/free/inha/'


    @exception_logging(list())
    def parse(self, page=1):
        url = self._base_url + str(page)
        text = self._request(url)
        root = etree.HTML(text)
        rows = root.xpath('//*[@id="list"]/table/tbody/tr')

        proxies = []
        for row in rows:
            ip = row.xpath('td[1]')[0].text
            port = row.xpath('td[2]')[0].text
            protocol = row.xpath('td[4]')[0].text
            address = row.xpath('td[5]')[0].text
            proxy = {
                'ip': ip,
                'port': port,
                'protocol': protocol,
                'address': address
            }
            proxies.append(proxy)

        return proxies
