#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/4/24 下午6:48
# @Author  : Robert
# @File    : config.py
# @Title    :


import os,datetime

####服务启动的主机名,端口号,DEBUG模式开关
HOST_NAME = "10.10.23.96"
HOST_PORT = "5000"
HOST_DEBUG_MODE =True



###服务需要的目录
RUN_HOME_PATH=os.path.dirname(os.path.abspath(__file__))+"/"     ##项目目录  例如  /home/sbluo/PycharmProjects/park-tool-api/
template_dir=RUN_HOME_PATH+"appbox/template"    #模板目录
static_dir=RUN_HOME_PATH+"appbox/template/static"         #项目静态资源目录


####LOG 配置
LOG_LEVEL="ERROR"
OBJ_LOGGER="[box tester]"
FILE_LOGGER=RUN_HOME_PATH+"tmp/logs/box"+str(datetime.datetime.now().strftime("%Y%m%d"))+".log"


###http request header
t_headers = {'Content-Type': 'application/json','accept':'application/json'}



#