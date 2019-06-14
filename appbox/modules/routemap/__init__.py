#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 19-4-3 上午11:38
# @Author  : Robert
# @File    : __init__.py.py
# Title    :

from flask import Flask
from flask import request as flaskrequest
from flask import Request
from flask import Markup
from flask import Response
from appbox.views.home import showhomepage
from appbox.views.fp import fpresponse
from appbox.views.box import boxmock
from appbox.views.huijufenfa import huijufenfamockoutput
from appbox.views.baidu import prebaidu
from appbox.views.run import runapp
from appbox.modules.loger import logger
import config,json
from appbox import data_body