#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 19-4-2 下午9:29
# @Author  : Robert
# @File    : prebaidu.py
# Title    :


from appbox.modules.loger import logger
from appbox import data_body


class preBaidu():

    def __init__(self):
        pass

    def demoA(self):
        logger.logger.info("This is a preBaidu Mock server demo")
        return data_body.preBAIDU_OUTPUT