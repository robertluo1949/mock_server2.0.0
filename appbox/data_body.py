#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 19-4-2 下午3:29
# @Author  : Robert
# @File    : data_body.py
# Title    :
import json
import config
import datetime,time
from appbox.modules.imagecontrol.imagecontent import ImageContent

t_headers = {'Content-Type': 'application/json','accept':'application/json'}
t_box_headers = {'Content-Type': 'application/json','accept':'application/json','expectResult':'1'}

###MOCK SERVER HOST+PORT
BOX_MOCK_SERVER ="http://"+config.HOST_NAME+":"+config.HOST_PORT+"/mock/box/"
FP_MOCK_SERVER  ="http://"+config.HOST_NAME+":"+config.HOST_PORT+"/mock/fp/"
MANAGE_MOCK_SERVER  ="http://"+config.HOST_NAME+":"+config.HOST_PORT+"/mock/manage/"


default_staff = {
    'james':{
        'staffname': '詹姆斯','stafffaceid':None, 'card_numbers':2007589655,'staffid':10642,
        'face_image_path':config.RUN_HOME_PATH + "appbox/static/james.jpeg"
    },
    'meixi': {
        'staffname': '里奥·梅西','stafffaceid':None,'card_numbers':4007589655, 'staffid':10644,
        'stafftagname':"apiteststafftag",'remark':"验证??结果",
        'face_image_path': config.RUN_HOME_PATH + "appbox/static/james.jpeg"
    },
}
__face_image_base64code = ImageContent(
    default_staff['james']['face_image_path']).imagetob64()


# ##MOCK FP data
# FP_RESPONSE_demo=json.dumps({"statusCode":200,
#                   "statusString":"get request OK,"})


###MOCK SERVER MAP
mockservermap={0:"box",1:"fp",2:"huiju",3:"prebaidu",4:"sanhui",5:"agentliu"}


mockpath={
    "box":{"hjurl":"http://10.10.23.123:7198",
           0:{"whitelist":"/video_box/v1/whitelist/upload"},
           1:{"greylist":"/video_box/v1/greylist/upload"},
           2:{"mockviidupload":"VIIDUploads"}
           },
    "fp":{
        0:{
            ###business/api
             "login":{0:"/business/api/login",1:"business",2:"api",3:"login"},
             "user":{ 0:"/business/api/user/self",1:"business",2:"api",3:"user",4:"self"},
             "repository":{0:"/business/api/repository",3:"repository"},
             "retrieval_repository":{0:"/business/api/retrieval_repository",3:"retrieval_repository"}
        },
        1:{"extract":{0:"/face/v1/framework/face_image/repository/picture/extract",
                        6:"extract"},
           "feature":{0:"/face/v1/framework/face_image/repository/picture/feature",
                        6:"feature"},
           },
        2:{"change_retrieval":{0:"/business/api/change_retrieval",1:"business",2:"api",3:"change_retrieval"}},

    },
    "huijudx":{
               0:{
                    ###[电信]  人脸采集信息上传
                 "submitInfo":{0:"dx/v1/init/submitInfo",1:"",2:"",4:"submitInfo"},
                    ###[电信]  人脸核查信息上传
                 "checkInfo": {0:"dx/v1/init/checkInfo",1:"",2:"",4:"checkInfo"},
                    ###[电信] 订阅接口
                 "subscribes": {0:"dx/v1/init/subscribes",1:"",2:"",4:"subscribes"},
                    ###[电信] 通知接口
                 "uploads":{0:"dx/v1/init/dxuploads",1:"",2:"",4:"dxuploads"},
                 "":"",
                },
               1:{
                   #### [移动]  注册
                  "Register":{1:"VIID/System/Register",2:"System",3:"Register"},
                   #### [移动]  上传自动采集人脸
                  "Faces": {1:"/VIID/Faces",2:"Faces"},
                   #### [移动]  订阅接口
                  "Subscribes":{1:"/VIID/Subscribes",2:"Subscribes"},
                   #### [移动]  通知接口
                  "SubscribeNotifications":{1:"/VIID/SubscribeNotifications",2:"SubscribeNotifications"},
                   #### [移动]  通知接口
                  "UPLOADS": {1:"/VIID/VIIDUploads",2:"VIIDUploads"}
               },
               3:{"subscribes":"dx/v1/init/subscribes"}},
    "prebaidu":{},
    "sanhui":{
        0:{
            ##预警比对接口调用请求方式(top3、白名单)
                "preventTrace":{1:"SynPreventTrace",2:"preventTrace.do"},
                "whitePanel": {1: "SynPreventTrace", 2: "whitePanel.do"},
            ##预警比对接口调用请求方式(top1)
                "getSfzMdInfo": {1: "SynPreventTrace", 2:"getSfzMdInfo"},
            },
        1:{
            ####下发白名单
            "downloadwhitelist":{1:"SynPreventTrace",2:"downloadwhitelist"},
            ####黑名单
            "downloadblacklist": {1: "SynPreventTrace", 2: "downloadblacklist"},
            ####内地来疆
            "downloadneidilist": {1: "SynPreventTrace", 2: "downloadneidilist"},
            ####全疆常口
            "downloadquanjianglist": {1: "SynPreventTrace", 2: "downloadquanjianglist"},
            ####外来人口
            "downloadwailailist": {1: "SynPreventTrace", 2: "downloadwailailist"}
        }

    },
    "agentliu":{
        0:{
            ###接收黑名单
            "recevieblacklist":{1:"/mock/agentliu/recevieblacklist",3:"recevieblacklist"}
        }
    }
}
ERROR_OUTPUT={
    0:{"message":"Not Find"},
}

###MOCK BOX DATA
BOX_INPUT ={
    0:{
            "faceId": "mockfaceid",
            "cardId": "mockcardID",
            "name": "mockname",
            "score": "99.899999",
            "infoKind": 0,
            "sourceId": "mock",
            "deviceId": "mock",
            "libType": "mock",
            "sceneType": "mock",
            "faceAppearTime": "mock",
            "nativeCityCode": "mock",
            "sceneType": "01",
            "longitude": "mock",
            "latitude": "mock",
            "location": "mock",
            "inOutStatus": "mock",
            "communityCode": "mock",
            "images": [{
                "imageId": "mock",
                "eventSort": "mock",
                "deviceId": "mock",
                "data": "ABCD"
            }]
        }
}
BOX_OUTPUT={
    0:{
         "data": "ff30585b-16cf-40e2-9666-716aac2b3f07",
         "message": "sucess",
         "code": "200"   },
    1:{"status":"Failed","message":"BOX Mock Server"},
    3:{}
}

##FP  分库比对模拟
FP_INPUT ={
    0:{}
}
FP_OUTPUT={
    0:{"status":"OK","message":"FP Mock Server"},
    1:{"status":"Failed","message":"FP Mock Server"},
    ###FP请求接口(基于ydn.4)  POST  #登陆
    2:{"rtn":0,"message":"mock OK","session_id":"mock381784214@XJFP_1554371568"},
    ###FP请求接口(基于ydn.4) #获取自身（保活） GET
    3:{"rtn":0,"message":"mock OK","id":"mock3@XJFP_1554371568","name":"admin"},
    ####FP请求接口  POST 抽特征
    4:{"message": "mock OK", "results": [{"feature_base64": __face_image_base64code}], "rtn": 0},
    ### FP请求接口  POST  #特征建库
    5:{"message": "mock OK", "rtn": 0},
    ### FP请求接口 #新建人像库
    6:{"rtn":0,"message":"mock OK","id":"33"},
    #### 获取人像库列表
    7:{
    "rtn": 0,
    "results": [{
                            "id": "3",
                            "name": "area_repertory",
                            "face_image_num": 0,
                            "create_time": int(time.time()),
                            "permission_map": {
                                "0": 2,
                                "1": 2,
                                "101": 2,
                                "102": 2,
                                "400": 2,
                                "452": 2,
                                "453": 2,
                                "501": 2,
                                "502": 2,
                                "503": 2,
                                "504": 2,
                                "505": 2,
                                "553": 2,
                                "554": 2,
                                "601": 2,
                                "602": 2,
                                "603": 2,
                                "604": 2,
                                "605": 2
                            }
                        },{
                            "id": "2",
                            "name": "total_repertory",
                            "face_image_num": 0,
                            "create_time": int(time.time()),
                            "permission_map": {
                                "0": 2,
                                "1": 2,
                                "101": 2,
                                "102": 2,
                                "400": 2,
                                "452": 2,
                                "453": 2,
                                "501": 2,
                                "502": 2,
                                "503": 2,
                                "504": 2,
                                "505": 2,
                                "553": 2,
                                "554": 2,
                                "601": 2,
                                "602": 2,
                                "603": 2,
                                "604": 2,
                                "605": 2
                            }
                        },{
                            "id": "1",
                            "name": "white_list_repertory",
                            "face_image_num": 30001,
                            "creator_id": 3,
                            "create_time":int(time.time()),
                            "permission_map": {
                                "0": 2,
                                "1": 2,
                                "101": 2,
                                "102": 2,
                                "400": 2,
                                "452": 2,
                                "453": 2,
                                "501": 2,
                                "502": 2,
                                "503": 2,
                                "504": 2,
                                "505": 2,
                                "553": 2,
                                "554": 2,
                                "601": 2,
                                "602": 2,
                                "603": 2,
                                "604": 2,
                                "605": 2
                            }
                        },{
                            "id": "0",
                            "name": "black_list_repertory",
                            "face_image_num": 30001,
                            "creator_id": 3,
                            "create_time": int(time.time()),
                            "permission_map": {
                                "0": 2,
                                "1": 2,
                                "101": 2,
                                "102": 2,
                                "400": 2,
                                "452": 2,
                                "453": 2,
                                "501": 2,
                                "502": 2,
                                "503": 2,
                                "504": 2,
                                "505": 2,
                                "553": 2,
                                "554": 2,
                                "601": 2,
                                "602": 2,
                                "603": 2,
                                "604": 2,
                                "605": 2
                            }
                        }
    ]
},
    #### #人像库检索  返回比对结果为True
    80:{"rtn":0,"message":"80 OK","retrieval_query_id":"17","results":[
        {"picture_uri":"normal://repository-builder/20190405/1B2M2Y8AsgTpgAmY7PhCfg==@1",
        "person_id":"mock_persion","is_writable":True,"born_year":0,
         "face_image_uri":"normal://repository-builder/20190405/1B2M2Y8AsgTpgAmY7PhCfg==@1",
         "repository_id":"34","nation":0,"face_image_id":"mock9223372036854815812","name":"mock",
         "similarity":98.29735655048604,"gender":0,"offset":0},
        {"picture_uri":"normal://repository-builder/20190405/1B2M2Y8AsgTpgAmY7PhCfg==@1",
                "person_id":"mock_persion","is_writable":True,"born_year":0,
                 "face_image_uri":"normal://repository-builder/20190405/1B2M2Y8AsgTpgAmY7PhCfg==@1",
                 "repository_id":"34","nation":0,"face_image_id":"mock9223372036854815812","name":"mock",
                 "similarity":97.29735655048604,"gender":0,"offset":0},
        {"picture_uri":"normal://repository-builder/20190405/1B2M2Y8AsgTpgAmY7PhCfg==@1",
                "person_id":"mock_persion","is_writable":True,"born_year":0,
                 "face_image_uri":"normal://repository-builder/20190405/1B2M2Y8AsgTpgAmY7PhCfg==@1",
                 "repository_id":"34","nation":0,"face_image_id":"mock9223372036854815812","name":"mock",
                 "similarity":96.29735655048604,"gender":0,"offset":0}],
        "total":3},
    81: {"rtn": 0, "message": "81 OK", "retrieval_query_id": "2", "results": [], "total": 0},
    82: {"rtn": 0, "message": "82 OK", "retrieval_query_id": "1", "results": [], "total": 0},
    83: {"rtn": 0, "message": "83 OK", "retrieval_query_id": "0", "results": [], "total": 0},
    "count_retrieval":{"value":80,"count":1,"valuelist":[80,81,82,83]},
    "error":{"totalcount":10,"intervaltime":0,"changevalue":82,"message":"error"}
}


##汇聚分发平台M模拟
HUIJU_INPUT ={
    0:{
        "FaceListObject": {
            "FaceObject": [{
                "FaceID": "20190122301",
                "InfoKind": 2,
                "DeviceID": "hk_001",
                "FaceAppearTime": "2019-01-18 19:59:40",
                "NativeCityCode": "11111111",
                "SceneType": "01",
                "Longitude": "6.666666",
                "Latitude": "6.666666",
                "Location": "xxxx街道",
                "InOutStatus": "0",
                "CommunityCode": "123",
                "SubImageList": {
                    "SubImageInfoObject": [{
                        "ImageID": "20181227170803",
                        "DeviceID": "11011218001320068039",
                        "Type": "11",
                        "Data": __face_image_base64code
                    }]
                }
            }]
        }
    },
    ### 以下是 移动上传给 智能业务综合分析平台的数据
    1:{
        "notificationID":"mockID",
        "subscribeID":"mockID",
        "FaceListObject":{
            "FaceObject":[
                {
                    "FaceID": "asfas",
                    "IDNumber": "0000",
                    "IDName":"mockID",
                    "Score":"98.989898989",
                    "InfoKind":0,
                    "SourceID":"01fdsfds",
                    "DeviceID":"mock",
                    "LibType":"mock",
                    "FaceAppearTime":"mock",
                    "NativeCityCode":"mock",
                    "SceneType":"01",
                    "Longitude":"mock",
                    "Latitude":"mock",
                    "Location":"mock",
                    "InOutStatus":"mock",
                    "CommunityCode":"mock",
                    "SubImageList":[
                        {
                            "ImageID":"mock",
                            "Type":"mock",
                            "DeviceID":"mock",
                            "Data":__face_image_base64code
                        }
                    ]
                }
            ]
        }
    }
}
HUIJU_OUTPUT={
    ####电信   1.人脸采集信息上传
    0:{"responseStatus":{"id":"mockdeviceListID","requestURL":"","statusCode":800,"statusString":"认证通过","localTime":str(datetime.datetime.now().strftime('%Y%m%d%H%M%S'))}},
    ####电信   2.人脸核查信息上传
    1:{"responseStatus":{"id":"mockdeviceListID","requestURL":"","statusCode":800,"statusString":"认证通过","localTime":str(datetime.datetime.now().strftime('%Y%m%d%H%M%S'))}},
    ####电信   3.订阅接口  dx/v1/init/subscribes
    2:{"responseStatus":{"id":"mockdeviceListID","requestURL":"","statusCode":800,"statusString":"认证通过","localTime":str(datetime.datetime.now().strftime('%Y%m%d%H%M%S'))}},
    ####电信   4.通知接口
    3:{"responseStatus":{"id":"mockdeviceListID","requestURL":"","statusCode":800,"statusString":"认证通过","localTime":str(datetime.datetime.now().strftime('%Y%m%d%H%M%S'))}},


    ##  注册 通知接口移动VIID
    4: {"ResponseStatusObject": {
        "Id": "mockid", "RequestURL": "", "StatusCode": 0,
        "StatusString": "认证通过", "LocalTime": str(datetime.datetime.now().strftime('%Y%m%d%H%M%S'))}},
    ##订阅接口 Subscribes  移动VIID
    5:{"ResponseStatusListObject":{
        "ResponseStatusObject":[
            {"Id": "mockid","RequestURL":"","StatusCode":0,"StatusString":"认证通过",
            "LocalTime": str(datetime.datetime.now().strftime('%Y%m%d%H%M%S'))}]}
        },
    ##通知接口  移动VIID
    6:{"ResponseStatusListObject":{
        "ResponseStatusObject":[
            {"Id": "mockid","RequestURL":"","StatusCode":0,"StatusString":"认证通过",
            "LocalTime": str(datetime.datetime.now().strftime('%Y%m%d%H%M%S'))}]}
        },
    ##1.人脸采集信息上传 批量FACES  移动VIID
    7:{"ResponseStatusListObject":{
        "ResponseStatusObject":[
            {"Id": "mockid","RequestURL":"","StatusCode":0,"StatusString":"认证通过",
            "LocalTime": str(datetime.datetime.now().strftime('%Y%m%d%H%M%S'))}]}
        },
}

###摆渡前置机模拟
preBAIDU_INPUT ={
    0:{}
}
preBAIDU_OUTPUT={
    0:{"status":"OK","message":"preBAIDU Mock Server"},
    1:{"status":"Failed","message":"preBAIDU Mock Server"}
}


###三汇  大数据平台的输入和输入json BODY
SanHuiBigData_INPUT={
    ##白名单 输入
    0:{
        "sfz_md5":"d7c6ffc97b856740fbd6e886bddeed75",
        "sfzh":"'650201198401011830",
        "name":"白_买买提01",
        "xqbh":"650106540000012003",
        "status":"1",
        "datatime":"2019-04-08 22:00:00"
        },
    ##黑名单 输入
    1:{},
    ##区县名单 输入
    2:{},
    ##全疆名单 输入
    3:{},
    ##外来名单 输入
    4: {"key":"",
        "sign":"",
        "message":{
            "data":{
                "uuid":"",
                "sfzh":"*必填-身份证md5",
                "sqbh":"*必填-小区编号",
                "location":"*必填-小区地址名称",
                "areacode":"*必填-6位行政区划",
                "longitude":"*必填-经度longitude(xx.xxxxxx小数点后6位，不是度分秒格式)",
                "latitude":"*必填-纬度latitude(xx.xxxxxx小数点后6位，不是度分秒格式)",
                "devicecode" :"*必填-设备编码",
                "passtime":"*必填-通过时间(yyyy-MM-dd HH24:mi:ss)",
                "jcbs":"进入离开标识(0:进入，1：离开)",
                "similar_degree":"人证比对相似度",
                "vender":"*必填-数据来源(hk、hw、ks、yh)",
                "cjlx":"*必填-场景类型(01封闭式小区；02内保单位；03停车场；04集贸市场；05旅馆、酒店；06公共交通车辆；07巷道口；08 检查站)",
                "timestamp":""
                }
        }
}

}
SanHuiBigData_OUTPUT={
    0:	{
        "type":"face","retcode":"1","msg":"比对成功！",
        "flag":"normal","data":[]},
    1:{
        "type":"face","retcode":"1","msg":"比对成功！",
        "flag":"black /gray","data":[]},
    2:{
        "type":"face","retcode":"1","msg":"比对成功！",
        "data":[{"uuid":"mockuuid","sfzmd5":"mocksfzmd5","hjdz":"新疆省乌鲁木齐开发区"+str(time.time()).replace(".","")+"号",
                 "pic_url":"mockpic_url","devicecode":"mockdevicecode","similar_degree":"98.988888888",
               "location":"新疆省克拉玛依mocklocation","passtime":str(datetime.datetime.now().strftime('%Y%m%d%H%M%S'))}
               ]  },
}

###三汇大数据平台的TOP1 白名单图片会从这里拿
SanHuiBigDB_connect ={
    "connect":{"host":"10.10.23.74", "user":"yituadmin", "passwd":"Yitu@123", "db":"capture_platform"},
    "scheduler":{"trigger":"interval","seconds":60},
    "exceselect":"SELECT sfzh_md5, photo_url FROM gray_list "
}


###流代理的输出
AgentLiu_OUTPUT={
    0:{"responseStatus":{"id":"mockdeviceListID","requestURL":"","statusCode":800,"statusString":"流代理通过","localTime":str(datetime.datetime.now().strftime('%Y%m%d%H%M%S'))}},

}

