# -*- coding:utf-8 -*-
import random
from datasets import USER_AGENTS
from flask import Flask, request

app = Flask(__name__)


@app.route('/')
def index():
    print("服务器收到的UA: {}".format(request.headers['user-agent']))
    return "hello world"


if __name__ == '__main__':
    headers = {
        'user-agent': random.choice(USER_AGENTS)
    }

    print("request的UA: {}".format(headers['user-agent']))

    with app.test_client() as c:
        c.get('/', headers=headers)
