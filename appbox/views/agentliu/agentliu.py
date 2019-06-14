#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/4/9 下午5:57
# @Author  : Robert
# @File    : agentliu.py
# Title    :

from appbox.modules.loger import logger
from appbox.modules.callrequest import callrequest
from appbox import data_body
import json,time
import requests
import importlib

class AgentLiuMockOutput():
    '''
    流代理的模拟器
    '''
    def __init__(self):
        pass

    def recevieblacklist(self):
        '''
        :return: jsonbody
        '''
        return data_body.AgentLiu_OUTPUT[0]