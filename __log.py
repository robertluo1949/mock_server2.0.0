#coding:utf-8
'''
title:逻辑控制模块   control
author:Robert
date:20171115
email:luoshuibo@vcredut.com
content:
other:
'''

import logging

import  logging
import sys,os


__filename = str(os.getcwd()),"\\log.txt"
print(__filename)

logging.debug("aaaa")

logging.basicConfig(filename=__filename,format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')