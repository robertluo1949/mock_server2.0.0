#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 19-4-5 上午10:49
# @Author  : Robert
# @File    : sanhuimock.py
# Title    :
from appbox.modules.loger import logger
from appbox import data_body,data_md5person
import json,time,random
import importlib
import pandas
from  flask import  request as flaskrequest
from appbox.modules.db_helper import db_loader


class SanHuiBigData():
    '''
    MOCK 三汇系统 [大数据平台] 接口
    '''
    def __init__(self):
        importlib.reload(data_body)

    def demoA(self):
        logger.logger.info("This is a SanHui BigData Mock Server Demo")

    def whitePanel(self):
        logger.logger.info("Response Result is : ")
        r_body =data_body.SanHuiBigData_OUTPUT[0]
        logger.logger.info(json.dumps(r_body))
        return r_body

    def preventTrace(self):
        logger.logger.info("Response Result is : ")
        r_body =data_body.SanHuiBigData_OUTPUT[1]
        logger.logger.info(json.dumps(r_body))
        return r_body
    def getSfzMdInfo(self):
        '''
        TOP1 白名单下发
        :return:
        '''
        logger.logger.info("Response Result is : ")

        try:

            pd =pandas.read_csv(data_md5person.hjdz_listcsv)
            filepath = data_md5person.hjdz_listcsv
            pd = pandas.read_csv(filepath)

            pdlen = len(pd.values)
            randomindex = random.randrange(1, pdlen)
            cur_request_data =flaskrequest.get_json()
            # print(flaskrequest.charset)
            ###把业务综合分析平台请求body进行组装,包装在响应body里面
            if cur_request_data["message"]["data"] is not  None:

                data_body.SanHuiBigData_OUTPUT[2]["data"][0]["sfzmd5"]=cur_request_data["message"]["data"]["sfzh"]
                data_body.SanHuiBigData_OUTPUT[2]["data"][0]["similar_degree"]=cur_request_data["message"]["data"]["similar_degree"]
                data_body.SanHuiBigData_OUTPUT[2]["data"][0]["location"]=cur_request_data["message"]["data"]["location"]
                data_body.SanHuiBigData_OUTPUT[2]["data"][0]["uuid"]=cur_request_data["message"]["data"]["uuid"]
                data_body.SanHuiBigData_OUTPUT[2]["data"][0]["hjdz"]=pd.values[randomindex][1]+pd.values[randomindex][0]
                person_list = db_loader.db_loader.get_instance().get_person_list()
                if cur_request_data["message"]["data"]["sfzh"] in dict.keys(person_list):
                    data_body.SanHuiBigData_OUTPUT[2]["data"][0]["pic_url"] = person_list[cur_request_data["message"]["data"]["sfzh"]]
                else:
                    data_body.SanHuiBigData_OUTPUT[2]["data"][0]["pic_url"] = person_list["不在大数据库中的人"]
        except BaseException as be:
            logger.logger.error(be)

        r_body =data_body.SanHuiBigData_OUTPUT[2]
        logger.logger.info(json.dumps(r_body).encode(encoding='utf-8'))
        return r_body

    def downloadwhitelist(self):
        logger.logger.info("Response Result is : ")
        r_body =data_body.SanHuiBigData_OUTPUT[2]
        logger.logger.info(json.dumps(r_body))
        return r_body

    def downloadblacklist(self):
        logger.logger.info("Response Result is : ")
        r_body =data_body.SanHuiBigData_OUTPUT[2]
        logger.logger.info(json.dumps(r_body))
        return r_body

    def downloadneidilist(self):
        logger.logger.info("Response Result is : ")
        r_body =data_body.SanHuiBigData_OUTPUT[2]
        logger.logger.info(json.dumps(r_body))
        return r_body

    def downloadquanjianglist(self):
        logger.logger.info("Response Result is : ")
        r_body =data_body.SanHuiBigData_OUTPUT[2]
        logger.logger.info(json.dumps(r_body))
        return r_body

    def downloadwailailist(self):
        logger.logger.info("Response Result is : ")
        r_body =data_body.SanHuiBigData_OUTPUT[2]
        logger.logger.info(json.dumps(r_body))
        return r_body
