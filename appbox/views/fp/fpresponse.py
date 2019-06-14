#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 19-4-2 下午3:46
# @Author  : Robert
# @File    : fpresponse.py
# Title    :


from flask import Flask
from flask import request as flaskrequest
from flask import Response
from appbox.modules.loger import logger
from flask import render_template
from flask import request as f_request
import requests
import  json
from appbox import data_body

class FacePlatformMock():
    '''
    响应body
    '''

    def __init__(self):

        logger.logger.info("This is FP Mock Server function ")
        logger.logger.info(flaskrequest)
        logger.logger.info(flaskrequest.get_json())


    def fpdemoresponse(self):
        logger.logger.info(flaskrequest)

        return str(data_body.FP_RESPONSE_demo)

    def fpdemoB(self):
        return str(data_body.FP_RESPONSE_demo)


    def fplogin(self):
        r_body =data_body.FP_OUTPUT[2]
        logger.logger.info(json.dumps(r_body))
        return r_body

    def userself(self):
        r_body =data_body.FP_OUTPUT[3]
        logger.logger.info(json.dumps(r_body))
        return r_body

    def extract(self):
        r_body =data_body.FP_OUTPUT[4]
        logger.logger.info(json.dumps(r_body))
        return r_body

    def feature(self):
        r_body =data_body.FP_OUTPUT[5]
        logger.logger.info(json.dumps(r_body))
        return r_body

    def repositorypost(self):
        r_body =data_body.FP_OUTPUT[6]
        logger.logger.info(json.dumps(r_body))
        return r_body

    def repositoryget(self):
        r_body =data_body.FP_OUTPUT[7]
        logger.logger.info(json.dumps(r_body))
        return r_body

    def retrieval_repository(self):

        r_body =data_body.FP_OUTPUT[data_body.FP_OUTPUT['count_retrieval']['value']]
        logger.logger.info(json.dumps(r_body))

        self.autochange_retrieval()
        return r_body

    def change_retrieval(self,changevalue):
        '''
        对FP 分层比对结果进行改变
        :return:
        '''
        try:
            __message=data_body.FP_OUTPUT.keys()
            self.changevalue=changevalue
            data_body.FP_OUTPUT['error']['message'] = __message
            data_body.FP_OUTPUT['count_retrieval']['value']=changevalue
            logger.logger.info("修改 FP 比对结果")
            r_body =data_body.FP_OUTPUT[data_body.FP_OUTPUT['count_retrieval']['value']]
            logger.logger.info(json.dumps(r_body))
        except Exception as e:
            r_body = data_body.FP_OUTPUT['error']
        return r_body

    def change_retrieval_error(self):
        __message="改变FP 分层比对结果失败,参数不正确 changevalue ,预期值是 "+str(data_body.FP_OUTPUT['count_retrieval']['valuelist'])
        logger.logger.info(__message)
        data_body.FP_OUTPUT['error']['message'] =__message
        r_body= data_body.FP_OUTPUT['error']
        logger.logger.info(json.dumps(r_body))
        return r_body

    def autochange_retrieval(self):
        __message ="修改 81--80 error"
        data_body.FP_OUTPUT['count_retrieval']['count'] +=1
        if data_body.FP_OUTPUT['count_retrieval']['count'] >=4:
            data_body.FP_OUTPUT['count_retrieval']['value'] =\
            data_body.FP_OUTPUT['count_retrieval']['valuelist'][3]
            data_body.FP_OUTPUT['count_retrieval']['count'] =0
        elif data_body.FP_OUTPUT['count_retrieval']['count'] ==3:

            data_body.FP_OUTPUT['count_retrieval']['value'] =\
                data_body.FP_OUTPUT['count_retrieval']['valuelist'][2]
        elif data_body.FP_OUTPUT['count_retrieval']['count'] == 2:
            data_body.FP_OUTPUT['count_retrieval']['value'] =\
                data_body.FP_OUTPUT['count_retrieval']['valuelist'][1]
        elif data_body.FP_OUTPUT['count_retrieval']['count'] == 1:
            data_body.FP_OUTPUT['count_retrieval']['value'] =\
                data_body.FP_OUTPUT['count_retrieval']['valuelist'][0]
        else:
            logger.logger.warning(__message)


        logger.logger.info("修改 81--80")

