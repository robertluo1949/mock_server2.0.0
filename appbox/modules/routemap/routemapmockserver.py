#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 19-4-3 上午11:39
# @Author  : Robert
# @File    : routemap.py
# Title    :
from flask import request as flaskrequest
from appbox.views.fp import fpresponse
from appbox.views.box import boxmock
from appbox.views.huijufenfa import huijufenfamockoutput
from appbox.views.baidu import prebaidu
from appbox.views.sanhui import sanhuimock
from appbox.views.agentliu import agentliu
from appbox.modules.loger import logger
import config,json
from appbox import data_body


class RouteMapMockServer():
    '''
    这是资源URL的映射类
    []
    '''
    ##定义请求URL资源的默认响应body为空

    return_result=None
    mockservermap=data_body.mockservermap
    mockpath=data_body.mockpath
    box_input_body=data_body.BOX_INPUT
    viid_input_body=data_body.HUIJU_INPUT
    def __init__(self):

        pass

    def mapserveraction(self, mockserver, mockaction):
        '''
        :param server:
        :param mockaction:
        :return:
        '''
        self.mockserver=mockserver
        self.mockaction =mockaction

        jsonData = flaskrequest.get_json()
        logger.logger.debug(flaskrequest)
        logger.logger.debug(json.dumps(jsonData))

        __s_box = boxmock.boxMock()
        __s_fp = fpresponse.FacePlatformMock()
        __s_prebaidu=prebaidu.preBaidu()
        __s_huiju =huijufenfamockoutput.HuiJuFenfaMockOutput()
        __s_sanhui=sanhuimock.SanHuiBigData()
        __s_agentliu =agentliu.AgentLiuMockOutput()

        if self.mockserver==self.mockservermap[5]:
            if self.mockaction==str(self.mockpath['agentliu'][0]['recevieblacklist'][3]):
               self.return_result =__s_agentliu.recevieblacklist()
               return  (json.dumps(self.return_result))

        if self.mockserver==self.mockservermap[0]:

            ###处理 盒子的MOCK URL
            if self.mockaction== 'demoA':
                self.return_result = json.dumps(data_body.BOX_OUTPUT[0])
            elif self.mockaction== 'demoB':
                __s_box.manytimes(totalcount=1,intervaltime=1)
                self.return_result= json.dumps(data_body.BOX_OUTPUT[0])
            elif self.mockaction== 'demoC':
                logger.logger.info(jsonData)
                totalcount = jsonData['totalcount']
                intervaltime = jsonData['intervaltime']
                self.return_result = __s_box.manytimes(totalcount=totalcount, intervaltime=intervaltime)

            elif self.mockaction == 'greylist':
                self.totalcount = jsonData['totalcount']
                self.intervaltime = jsonData['intervaltime']
                __s_box.boxuploadlist(fun_url=self.mockpath['box']['hjurl'] +
                                              self.mockpath['box'][1]['greylist'],
                                      fun_data=self.box_input_body[0],
                                      totalcount=self.totalcount,
                                      intervaltime=self.intervaltime
                                      )
                self.return_result = json.dumps(self.box_input_body[0])


            elif self.mockaction == 'whitelist':
                self.totalcount = jsonData['totalcount']
                self.intervaltime = jsonData['intervaltime']
                __s_box.boxuploadlist(fun_url=self.mockpath['box']['hjurl'] +
                                              self.mockpath['box'][0]['whitelist'],
                                      fun_data=self.box_input_body[0],
                                      totalcount=self.totalcount,
                                      intervaltime=self.intervaltime
                                      )
                self.return_result = json.dumps(self.box_input_body[0])

        else:
            error_message="模拟盒子- 失败"
            logger.logger.error(error_message)
            self.return_result = error_message

        logger.logger.info(str(self.return_result))
        return json.dumps(self.return_result)


    def viidroutemap(self, vaction):
        '''
        移动 汇聚 和分发  路由映射  ---非注册接口
        :param vaction:
        :return:
        '''
        self.mockaction =vaction

        jsonData = flaskrequest.get_json()
        logger.logger.info(flaskrequest)
        logger.logger.info(flaskrequest.headers)
        logger.logger.info(json.dumps(jsonData))

        __s_huiju =huijufenfamockoutput.HuiJuFenfaMockOutput()

        if self.mockaction==str(self.mockpath['huijudx'][1]['Faces'][2]):
            self.return_result=__s_huiju.viidFaces()
        elif self.mockaction==str(self.mockpath['huijudx'][1]['Subscribes'][2]):
            self.return_result=__s_huiju.viidSubscribes()
        elif self.mockaction==str(self.mockpath['huijudx'][1]['SubscribeNotifications'][2]):
            self.return_result=__s_huiju.viidSubscribeNotifications()
        elif self.mockaction==str(self.mockpath['huijudx'][1]['UPLOADS'][2]):

            __url=jsonData['destinaionurl']
            __totalcount=jsonData['totalcount']
            __intervaltime=jsonData['intervaltime']
            __header =data_body.t_box_headers
            # __url="http://10.10.23.123:7198/VIID/SubscribeNotifications"
            self.return_result=__s_huiju.viidupload(fun_url=__url, fun_header=__header,fun_data=self.viid_input_body[1],
                                                    totalcount=__totalcount, intervaltime=__intervaltime)
        else:
            error_message="模拟汇聚平台-移动 VIID 失败"
            logger.logger.error(error_message)
            self.return_result = error_message
        return  json.dumps(self.return_result)

    def viidregisterroutemap(self, vsystem, vaction):
        '''
        VIID移动的路由映射
        :param vsystem:
        :param vaction:
        :return:
        '''
        self.vsystem = vsystem
        self.mockaction = vaction

        jsonData = flaskrequest.get_json()
        logger.logger.info(flaskrequest)
        logger.logger.info(flaskrequest.headers)
        logger.logger.info(json.dumps(jsonData))

        __s_huiju = huijufenfamockoutput.HuiJuFenfaMockOutput()

        if self.vsystem == 'System' and self.mockaction == 'Register':
            self.return_result = __s_huiju.viidregister()
        else:
            error_message = "模拟汇聚平台-移动 VIID register 失败"
            logger.logger.error(error_message)
            self.return_result = error_message

        return  json.dumps(self.return_result)

    def dxinitroutemap(self, dxaction):
        '''
        电信 的路由映射
        :param dxaction:
        :return:
        '''

        self.mockaction = dxaction

        jsonData = flaskrequest.get_json()
        logger.logger.info(flaskrequest)
        logger.logger.info(flaskrequest.headers)
        logger.logger.info(json.dumps(jsonData))

        __s_huiju = huijufenfamockoutput.HuiJuFenfaMockOutput()

        if self.mockaction==str(self.mockpath['huijudx'][0]['submitInfo'][4]):
            self.return_result=__s_huiju.dxsubmitInfo()
        elif self.mockaction==str(self.mockpath['huijudx'][0]['checkInfo'][4]):
            self.return_result=__s_huiju.dxcheckInfo()
        elif self.mockaction==str(self.mockpath['huijudx'][0]['subscribes'][4]):
            self.return_result=__s_huiju.dxsubscribes()
        elif self.mockaction==str(self.mockpath['huijudx'][0]['uploads'][4]):

            self.return_result=__s_huiju.dxupload(fun_url=None, fun_header=None,fun_data=None,totalcount=1, intervaltime=0)
        else:
            error_message="模拟汇聚平台-电信 dx 失败"
            logger.logger.error(error_message)
            self.return_result = error_message

        return  json.dumps(self.return_result)

    def sanhuiroutemap(self,shaction):
        '''
        三汇 大数据中心的路由映射
        :param shaction:
        :return:
        '''
        self.mockaction = shaction

        jsonData = flaskrequest.get_json()
        logger.logger.info(flaskrequest)
        logger.logger.info(flaskrequest.headers)
        logger.logger.info(str(json.dumps(jsonData)))
        logger.logger.info(json.dumps(jsonData).encode(encoding='utf-8'))
        # logger.logger.info(json.dumps(jsonData).decode(encoding="utf-8", errors="strict"))
        __s_sanhui=sanhuimock.SanHuiBigData()

        if self.mockaction==str(self.mockpath['sanhui'][0]['preventTrace'][2]):
            self.return_result=__s_sanhui.preventTrace()
        elif self.mockaction==str(self.mockpath['sanhui'][0]['whitePanel'][2]):
            self.return_result=__s_sanhui.whitePanel()
        elif self.mockaction ==str(self.mockpath['sanhui'][0]['getSfzMdInfo'][2]):
            self.return_result=__s_sanhui.getSfzMdInfo()
        else:
            error_message="模拟三汇中心-大数据平台 sys 失败"
            logger.logger.error(error_message)
            self.return_result = error_message
        return  json.dumps(self.return_result)

    def faceplatformroutemap(self,fpaction):
        '''
        人像大平台的路由映射
        :param fpaction:
        :return:
        '''
        self.mockaction=fpaction
        jsonData = flaskrequest.get_json()
        logger.logger.info(flaskrequest)
        logger.logger.info(flaskrequest.headers)
        logger.logger.info(json.dumps(jsonData))
        __s_faceplatform=fpresponse.FacePlatformMock()

        if self.mockaction==str(self.mockpath['fp'][0]['login'][3]):
            if flaskrequest.method =='POST':
                self.return_result=__s_faceplatform.fplogin()
        elif self.mockaction==str(self.mockpath['fp'][0]['user'][4]):
            if flaskrequest.method=='GET':
                self.return_result=__s_faceplatform.userself()
        elif self.mockaction==str(self.mockpath['fp'][0]['repository'][3]):

            if flaskrequest.method=='GET':
                self.return_result=__s_faceplatform.repositoryget()
            elif flaskrequest.method == 'POST':
                self.return_result=__s_faceplatform.repositorypost()
            else:
                logger.logger.error("error request")
        elif self.mockaction==str(self.mockpath['fp'][0]['retrieval_repository'][3]):
            self.return_result=__s_faceplatform.retrieval_repository()
        elif self.mockaction==str(self.mockpath['fp'][1]['extract'][6]):
            self.return_result=__s_faceplatform.extract()
        elif self.mockaction==str(self.mockpath['fp'][1]['feature'][6]):
            self.return_result=__s_faceplatform.feature()
        elif self.mockaction==str(self.mockpath['fp'][2]['change_retrieval'][3]):
            if "changevalue" not in data_body.FP_OUTPUT['count_retrieval']['valuelist']:
                logger.logger.warning("请求参数不合适")

                self.return_result=__s_faceplatform.change_retrieval_error()
            else:
                getvalue=jsonData['changevalue']
                logger.logger.info("获取getvalue  "+str(getvalue))
                self.return_result=__s_faceplatform.change_retrieval(changevalue=getvalue)
        else:
            error_message="模拟人像大平台-FacePlatform 失败"
            logger.logger.error(error_message)
            self.return_result = error_message
        return  json.dumps(self.return_result)
