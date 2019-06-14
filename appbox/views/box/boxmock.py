#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 19-4-2 下午3:21
# @Author  : Robert
# @File    : boxmock.py
# Title    : MOCK SERVER 盒子

from flask import Flask
from flask import render_template
from flask import request as f_request
import requests
from appbox import data_body
from appbox.modules.loger import  logger
import time,json

class boxMock():
    # fun_url=None
    # fun_data=None

    def __int__(self):
        pass

    def boxrequestdemo(self):
        '''

        :return:
        '''
        try:
            r =requests.get(url="http://www.baidu.com", headers=data_body.t_headers,  timeout=1)
            logger.logger.info(r)
        except Exception as e:
            logger.logger.error(e)
        return r


    def boxwritelist(self,fun_url=None,fun_data=None):
        '''
        :param fun_url:
        :param fun_data:
        :return:
        '''

        self.fun_url=fun_url
        self.fun_data =fun_data
        try:
            requests.post(url=self.fun_url,headers=data_body.t_headers,data=self.fun_data,timeout=3)
            logger.logger.info(self.fun_data)
        except BaseException as e:
            logger.logger.exception(e)
        return requests.status_codes

    def boxuploadlist(self,fun_url=None,fun_data=None,totalcount = 1, intervaltime = 1):
        '''
        :param fun_url:
        :param fun_data:
        :return:
        '''
        self.fun_url=fun_url
        self.fun_data =fun_data
        self.totalcount=totalcount
        self.intervaltime=intervaltime
        try:

            if self.totalcount>=1 and self.intervaltime>=0:
                logger.logger.info(str(self.totalcount)+"   "+str(self.intervaltime))
                index=0
                while index <self.totalcount:
                    logger.logger.info("index   "+str(index))
                    r = requests.post(url=self.fun_url, headers=data_body.t_box_headers, data=json.dumps(self.fun_data),
                                      timeout=3)
                    logger.logger.info("Resquest Body is : ")
                    logger.logger.info(self.fun_url)
                    logger.logger.info(json.dumps(self.fun_data))
                    logger.logger.info("Response Result is : ")
                    logger.logger.info(r.status_code)
                    logger.logger.info(json.dumps(r.json()))
                    time.sleep(self.intervaltime)
                    index+=1

        except BaseException as e:
            logger.logger.exception(e)
        return requests.status_codes


    def showPATH(self):
        return None



    def manytimes(self,totalcount=1,intervaltime=1):
        '''
        :param totalcount:
        :param intervaltime:
        :return:
        '''

        self.totalcount=totalcount
        self.intervaltime=intervaltime

        try:
            if totalcount>=1 and intervaltime>=1:
                logger.logger.info(str(totalcount)+"   "+str(intervaltime))
                index=0
                while index <totalcount:
                    logger.logger.info("index   "+str(index))
                    self.boxrequestdemo()
                    time.sleep(intervaltime)
                    index+=1
                    rp_body={"status":"OK"}
            else:
                logger.logger.warning("request body invalid")
                logger.logger.warning(str(totalcount)+"  "+str(intervaltime))
                rp_body = {"status": "BLOCK"}
        except BaseException as be:
            logger.logger.error("box mock server request error ")
            logger.logger.error(be)
            rp_body = {"status": "FAILED"}

        return rp_body



