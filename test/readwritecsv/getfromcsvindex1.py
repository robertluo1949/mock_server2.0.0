#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/4/19 下午3:25
# @Author  : Robert
# @File    : getfromcsvindex1.py
# @Title    :


import pandas
import random
import os,sys


sys.path.append(os.getcwd())
from appbox import data_md5person

filepath =data_md5person.hjdz_listcsv
pd =pandas.read_csv(filepath)


# print(pd)
pdlen =len(pd.values)
print(pdlen)

randomindex = random.randrange(1,pdlen)
print(pd.values[randomindex])

print(pd.values[randomindex][1]+pd.values[randomindex][0])


print("某行某列×××××××")
print(pd.values[1][0])