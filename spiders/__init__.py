# -*- coding:utf-8 -*-
import requests
from datasets import get_random_user_agent

class BaseSpider(object):

    def _request(self, url):
        headers = {
            'user-agent': get_random_user_agent()
        }
        rep = requests.get(url, headers=headers)
        if rep.ok and rep.status_code == 200:
            return rep.text
        return None
