#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/4/9 下午10:14
# @Author  : Robert
# @File    : readcsv.py
# Title    :



import pandas as pd
import numpy as np


article_read = pd.read_csv\
    ('new.csv',delimiter=';',
    names = ['my_datetime', 'event', 'country', 'user_id', 'source', 'topic'])

print(article_read)

