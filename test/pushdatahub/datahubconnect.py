#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/4/9 下午2:47
# @Author  : Robert
# @File    : datahubconnect.py
# Title    :

from appbox.modules.loger import logger
import sys
import traceback
from datahub import DataHub
from datahub.exceptions import ResourceExistException
from datahub.models import FieldType, RecordSchema, TupleRecord, BlobRecord, CursorType, RecordType

# access_id = "LTAIFk1MAdnLWVcJ"
# access_key =" WObRiv45dnf6GKjjT3Ef7ZthKaVVZF"
# endpoint = "https://dh-cn-shanghai.aliyuncs.com"
# project_name ="boxqatest"
# topic_name ="whitelist"
# records=[("records1")]



class DataHubMock(DataHub):

    def __init__(self):
        pass

    def connectDH(self,access_id, access_key, endpoint):
        dh = DataHub(access_id, access_key, endpoint)
        logger.logger.debug(str(dh))
        return dh

    def gettopic(self,dh):
        pass

    def getsechema(self,dh,project_name,topic_name):
        '''
        获取datahub上面的sechema
        :param dh:
        :return:
        '''
        topic_result = dh.get_topic(project_name, topic_name)
        record_schema = topic_result.record_schema
        logger.logger.debug(str(record_schema))
        return record_schema

    def getshards(self,dh):
        '''

        :return:
        '''
        shargs_result =dh.list


    def getcurson(self,dh):
        pass