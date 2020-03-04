from lxml import etree
from spiders import BaseSpider
from utils import exception_logging


class XiCiSpider(BaseSpider):
    """ 西刺代理爬虫 """

    def __init__(self):
        self._base_url = 'http://www.xicidaili.com/nn/'

    @exception_logging(list())
    def parse(self, page=1):
        url = self._base_url + str(page)
        text = self._request(url)
        root = etree.HTML(text)
        rows = root.xpath('//*[@id="ip_list"]/tr[position()>1]')

        proxies = []
        for row in rows:
            ip = row.xpath('td[2]')[0].text
            port = row.xpath('td[3]')[0].text
            try:
                address = row.xpath('td[4]/a')[0].text
            except IndexError:
                address = ''

            protocol = row.xpath('td[6]')[0].text.lower()
            proxy = {
                'ip': ip,
                'port': port,
                'protocol': protocol,
                'address': address
            }
            proxies.append(proxy)

        return proxies
