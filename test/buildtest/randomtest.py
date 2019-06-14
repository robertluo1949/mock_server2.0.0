#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/4/9 上午10:57
# @Author  : Robert
# @File    : randomtest.py
# Title    :


import requests

def build_reposit():
    response = requests.post(url='http://10.10.23.155:8099/vbox/v1/repositories',
                             data={"name": "test123"})
    # assert response.status_code==200
    print(response.status_code)
    print(response.content)


build_reposit()