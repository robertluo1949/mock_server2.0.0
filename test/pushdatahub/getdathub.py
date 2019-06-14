#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/4/9 下午2:46
# @Author  : Robert
# @File    : getdathub.py
# Title    :

import requests
from appbox.modules.callrequest.callrequest import CallRequest
from appbox.modules.loger import logger
import sys
import traceback
from datahub import DataHub
from datahub.exceptions import ResourceExistException
from datahub.models import FieldType, RecordSchema, TupleRecord, BlobRecord, CursorType, RecordType


access_id = "LTAIFk1MAdnLWVcJ"
access_key =" WObRiv45dnf6GKjjT3Ef7ZthKaVVZF"
endpoint = "https://dh-cn-shanghai.aliyuncs.com"
project_name ="box_a"
topic_name ="synway_fws_withe"


#
##https://usercenter.console.aliyun.com/#/manage/ak


# cur_dh =datahubconnect.DataHubMock()
#
# con_dh=cur_dh.connectDH(access_id, access_key, endpoint)
# cur_dh.getsechema(con_dh,project_name=project_name,topic_name=topic_name)


try:
    r =CallRequest()
    r.disablehttpswarnning()
    cur_h =DataHub(access_key=access_key,access_id=access_id,endpoint=endpoint)
    logger.logger.debug(cur_h)
    results_project = cur_h.list_project()
    logger.logger.debug(results_project)
    results_top = cur_h.list_topic(project_name)
    logger.logger.debug(results_top)
    results_schames=cur_h.list_shard(project_name,topic_name=topic_name)
    logger.logger.debug(results_schames)


except ResourceExistException as ree:
    logger.logger.error(ree)
# cur_h.create_project(project_name='box_b',comment='box_b')

