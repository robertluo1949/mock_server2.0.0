#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 19-4-4 上午10:32
# @Author  : Robert
# @File    : callrequest.py
# Title    :

import requests
import urllib3
import json,time
from appbox import data_body
from appbox.modules.loger import logger


class CallRequest():
    '''
    定义http request,默认调用次数是1,间隔 0s,默认超时时间3s

    '''

    def postrequest(self, fun_url=None, fun_header=None,fun_data=None,totalcount=1, intervaltime=0):
        '''
        :param fun_url:
        :param fun_data:
        :param fun_header:
        :param totalcount:
        :param intervaltime:
        :return:
        '''
        self.fun_header =fun_header
        self.fun_url = fun_url
        self.fun_data = fun_data

        self.totalcount = totalcount
        self.intervaltime = intervaltime

        try:

            if self.totalcount >= 1 and self.intervaltime >= 0:
                logger.logger.info(str(self.totalcount) + "   " + str(self.intervaltime))
                index = 0
                while index < self.totalcount:
                    logger.logger.info("index   " + str(index))
                    r = requests.post(url=self.fun_url, headers=self.fun_header,
                                      data=json.dumps(self.fun_data),verify=False,timeout=3)
                    logger.logger.info(self.fun_url)
                    logger.logger.info("Resquest Body is : ")
                    logger.logger.info(json.dumps(self.fun_data))
                    logger.logger.info("Response Result is : ")
                    logger.logger.info(r.status_code)
                    logger.logger.info(json.dumps(r.json()))
                    time.sleep(self.intervaltime)
                    index += 1

        except BaseException as e:
            logger.logger.exception(e)
        return requests.status_codes

    def disablehttpswarnning(self):

        requests.packages.urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
