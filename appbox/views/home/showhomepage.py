#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 19-4-2 下午3:01
# @Author  : Robert
# @File    : showhomepage.py
# Title    :

from flask import Flask
from flask import render_template
from appbox.modules.loger import logger
import  datetime

class homepage():

    def __int__(self):
        logger.logger.info(self.__doc__)



    def defaulthomepage(self):
        logger.logger.info("访问主页面 "+str(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')))
        return "新疆盒子 测试系统"