#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 19-4-2 下午9:09
# @Author  : Robert
# @File    : huijufenfa.py
# Title    :
from appbox.modules.loger import logger
from appbox.modules.callrequest import callrequest
from appbox import data_body
import json,time
import requests
import importlib


class HuiJuFenfaMockOutput():
    '''
    MOCK 汇聚分发平台 [移动VIID] 接口
    '''
    def __init__(self):
        importlib.reload(data_body)

    def demoA(self):
        logger.logger.info("This is a HuiJu Fenfa Mock Server Demo")
        return data_body.HUIJU_OUTPUT[0]
    def huijucheckInfo(self):
        return data_body.HUIJU_INPUT[3]
    def viidregister(self):
        '''
        :return:
        '''
        logger.logger.info("This is a HuiJu Fenfa Mock Server Demo")
        logger.logger.info("Response Result is : ")
        r_body =data_body.HUIJU_OUTPUT[4]
        logger.logger.info(json.dumps(r_body))
        return r_body

    def viidFaces(self):
        '''
        :return:
        '''
        logger.logger.info("This is a HuiJu Fenfa Mock Server Demo")
        logger.logger.info("Response Result is : ")
        r_body =data_body.HUIJU_OUTPUT[5]
        logger.logger.info(json.dumps(r_body))
        return r_body
    def viidSubscribes(self):
        '''
        :return:
        '''
        logger.logger.info("This is a HuiJu Fenfa Mock Server Demo")
        logger.logger.info("Response Result is : ")
        r_body =data_body.HUIJU_OUTPUT[6]
        logger.logger.info(json.dumps(r_body))
        return r_body

    def viidSubscribeNotifications(self):
        '''
        :return:
        '''
        logger.logger.info("This is a HuiJu Fenfa Mock Server Demo")
        logger.logger.info("Response Result is : ")
        r_body =data_body.HUIJU_OUTPUT[7]
        logger.logger.info(json.dumps(r_body))
        return r_body


    def viidupload(self,fun_url=None, fun_header=None,fun_data=None,totalcount=1, intervaltime=0):
        '''

        :return:
        '''
        self.fun_header =fun_header
        self.fun_url = fun_url
        self.fun_data = fun_data

        self.totalcount = totalcount
        self.intervaltime = intervaltime
        cur_callrequest =callrequest.CallRequest()
        cur_callrequest.postrequest(fun_url=self.fun_url, fun_header=self.fun_header,fun_data=self.fun_data,totalcount=self.totalcount, intervaltime=self.intervaltime)
        logger.logger.info("This is a HuiJu Fenfa Mock Server Demo")
        logger.logger.info("Response Result is : ")
        r_body =data_body.HUIJU_INPUT[1]
        logger.logger.info(json.dumps(r_body))
        return r_body


    def dxsubmitInfo(self):
        '''

        :return:
        '''
        logger.logger.info("This is a HuiJu Fenfa Mock Server Demo")
        logger.logger.info("Response Result is : ")
        r_body =data_body.HUIJU_OUTPUT[0]
        logger.logger.info(json.dumps(r_body))
        return data_body.HUIJU_OUTPUT[0]

    def dxcheckInfo(self):
        '''

        :return:
        '''
        logger.logger.info("This is a HuiJu Fenfa Mock Server Demo")
        logger.logger.info("Response Result is : ")
        r_body =data_body.HUIJU_OUTPUT[1]
        logger.logger.info(json.dumps(r_body))
        return data_body.HUIJU_OUTPUT[1]

    def dxsubscribes(self):
        '''
        :return:
        '''

        logger.logger.info("This is a HuiJu Fenfa Mock Server Demo")
        logger.logger.info("Response Result is : ")
        r_body =data_body.HUIJU_OUTPUT[2]
        logger.logger.info(json.dumps(r_body))
        return data_body.HUIJU_OUTPUT[2]


    def dxsubscribesbackcall(self,fun_url=None,fun_data=None,totalcount = 1, intervaltime = 1):

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

        logger.logger.info("This is a HuiJu Fenfa Mock Server Demo")
        logger.logger.info('dx/v1/init/subscribes')
        logger.logger.info("Response Result is : ")
        logger.logger.info(json.dumps(data_body.HUIJU_OUTPUT[8]))
        return data_body.HUIJU_OUTPUT[8]
    def dxupload(self,fun_url=None, fun_header=None,fun_data=None,totalcount=1, intervaltime=0):
        '''

        :return:
        '''
        self.fun_header =fun_header
        self.fun_url = fun_url
        self.fun_data = fun_data

        self.totalcount = totalcount
        self.intervaltime = intervaltime
        cur_callrequest =callrequest.CallRequest()
        cur_callrequest.postrequest(fun_url=self.fun_url, fun_header=self.fun_header,fun_data=self.fun_data,totalcount=self.totalcount, intervaltime=self.intervaltime)
        logger.logger.info("This is a HuiJu Fenfa Mock Server Demo")
        logger.logger.info('dx/v1/init/dxuploads')
        logger.logger.info("Response Result is : ")
        r_body =data_body.HUIJU_INPUT[0]
        logger.logger.info(json.dumps(r_body))
        return r_body