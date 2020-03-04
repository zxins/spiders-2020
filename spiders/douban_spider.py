from lxml import etree
from spiders import BaseSpider
from utils import exception_logging


class DoubanSpider(BaseSpider):
    """ 豆瓣Top250 """

    def __init__(self):
        self.base_url = 'https://movie.douban.com/top250'

    @exception_logging
    def parse(self, page=1):
        url = ''.join([self.base_url, '?start=', str(page)])
        text = self._request(url)
        root = etree.HTML(text)
        rows = root.xpath('//div[@class="item"]')

        movies = []
        # 下面这一坨写着真没意思，所以我选择豆瓣API ┓( ´∀` )┏
        for row in rows:
            img = row.xpath('div[1]/a/img/@src')[0]
            titles = row.xpath('div[2]/div/a/span')
            title = titles[0].text.strip()
            original_title = titles[1].text.replace('/', '').strip()

            try:
                other_titles = titles[2].text.strip().split('/')
                other_title = '/'.join([i.strip() for i in other_titles[1:]])
            except IndexError:
                other_title = ''

            star_info = row.xpath('div[2]/div[@class="bd"]/div/span')
            # 星级
            rating_num = star_info[1].text
            # 评价数
            eva_num = star_info[3].text

            p_list = row.xpath('div[2]/div[@class="bd"]/p')
            p1_text = p_list[0].xpath('string()').strip()
            # 导演 演员
            directors = p1_text.split('\n')[0].strip()
            # 类型
            genres = p1_text.split('\n')[1].strip('/').strip()

            inq = p_list[1].xpath('span')[0].text.strip()

            movie = {
                'img': img,
                'title': title,
                'original_title': original_title,
                'other_title': other_title,
                'rating_num': rating_num,
                'eva_num': eva_num,
                'directors': directors,
                'genres': genres,
                'inq': inq
            }
            movies.append(movie)

        return movies
