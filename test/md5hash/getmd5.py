#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/4/8 下午8:17
# @Author  : Robert
# @File    : getmd5.py
# Title    :

import hashlib




def  create_md5(number):
    m =hashlib.md5()
    m.update(bytes(number,encoding='utf-8'))
    m.hexdigest()
    print("MD5 加密前  "+str(number))
    print("MD5 加密后  "+m.hexdigest())


print(create_md5("650106540000012003"))