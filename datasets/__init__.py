# -*- coding:utf-8 -*-
import os
import random

# datasets包的路径
__HERE = os.path.abspath(os.path.dirname(__file__))

# 常用的user-agent列表
with open(os.path.join(__HERE, "user_agents.txt")) as f:
    USER_AGENTS = [i.strip() for i in f.readlines()]


def get_random_user_agent():
    return random.choice(USER_AGENTS)
