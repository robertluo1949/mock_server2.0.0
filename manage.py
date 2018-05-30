#coding:utf-8
'''
title:mock server   初始化
author:Robert,Shiyunliang
date:20180521
email:luoshuibo@vcredit.com,shiyunliang@vcredit.com
content:
other:
'''


import sys,os
curDir = os.getcwd()
sys.path.append(curDir)


from mockserver.templates import serverinfo, mock_body,showlogo,mock_body_PolicyDecision,mock_body_hbcf
from flask import Flask, jsonify, g, request
import requests
import random
import time
from datetime import datetime


app = Flask(__name__)




@app.before_request
def set_up_data():
    pass
    # g.in_body = mock_body.req_input_applycheck   ##导入参数

@app.route('/',methods=['GET','POST'])
def Hello():
    return  "This is a Mock Server!!!  author:Robert"

@app.route('/homepage',methods=['GET','POST'])
def homepage():
    return  "This is a Mock Server!!!  author:Robert"

@app.route('/mock/kbs/fund/PreCheck',methods=['POST'])
def mock_PreCheck():
    '''
    mock 资方平台fundsource 函数名称:PreCheck
    :return:
    '''
    g.in_body = mock_body.req_output_applycheck ##导入返回参数
    req = request.json
    reqpath = request.full_path
    try:
        print(datetime.now().strftime('%Y-%m-%d %H:%M:%S %f'), "☆request☆☆☆☆☆☆", reqpath)
        print(datetime.now().strftime('%Y-%m-%d %H:%M:%S %f'), "☆request☆☆☆☆☆☆", req)
        print(datetime.now().strftime('%Y-%m-%d %H:%M:%S %f'), "☆response☆☆☆☆☆☆", g.in_body)
    except Exception as ee:
        print("Mock server处理异常")
        print(ee)
    return jsonify(g.in_body)

@app.route('/mock/kbs/fund/createApply',methods=['POST'])
def mock_createApply():
    '''
    mock 资方平台fundsource 函数名称:createApply
    :return:
    '''
    g.in_body = mock_body.req_output_createApply    ##导入返回参数
    req =request.json
    reqpath =request.full_path
    print(datetime.now().strftime('%Y-%m-%d %H:%M:%S %f'), "☆request☆☆☆☆☆☆", reqpath)
    print(datetime.now().strftime('%Y-%m-%d %H:%M:%S %f'), "☆request☆☆☆☆☆☆", req)
    print(datetime.now().strftime('%Y-%m-%d %H:%M:%S %f'), "☆response☆☆☆☆☆☆", g.in_body)
    return jsonify(g.in_body)

def mock_request():
    '''

    :return:
    '''
    # http://10.139.60.61:8089/OrderApplyLendingService/OrderLendingStatusResult

    url = mock_body.kbsmsa+mock_body.OrderLendingStatusResult
    inputbody =mock_body.input_body
    tempp =requests.post(url,json=inputbody)



@app.route('/mock/kbs/fund/ReadLoan',methods=['POST'])
def mock_ReadLoan():
    '''
        模拟查询放款结果
    :return: sonify(g.in_body)
    '''

    req = request.json

    mock_body.req_output_ReadLoan_ok["Data"]["ApplyCode"] = req["ApplyCode"]
    mock_body.req_output_ReadLoan_ok["Data"]["LoanNo"] = req["ApplyCode"]
    mock_body.req_output_ReadLoan_ok["Data"]["OutSeq"] =req["ApplyCode"]
    mock_body.req_output_ReadLoan_ok["Data"]["LoanDate"] =str(datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
    g.in_body = mock_body.req_output_ReadLoan_ok  ##导入返回参数

    reqpath = request.full_path
    print(datetime.now().strftime('%Y-%m-%d %H:%M:%S %f'), "☆request☆☆☆☆☆☆", reqpath)
    print(datetime.now().strftime('%Y-%m-%d %H:%M:%S %f'), "☆request☆☆☆☆☆☆", req)
    print(datetime.now().strftime('%Y-%m-%d %H:%M:%S %f'), "☆response☆☆☆☆☆☆", g.in_body)

    return jsonify(g.in_body)

@app.route('/mock/kbs/fund/createApplyold',methods=['POST'])
def mock_createApplyold():
    '''
    已停止使用
    '''
    req = request.json
    reqpath = request.full_path
    g.in_body ={"aa":"aa"}

    print(datetime.now().strftime('%Y-%m-%d %H:%M:%S %f'), "☆request☆☆☆☆☆☆", reqpath)
    print(datetime.now().strftime('%Y-%m-%d %H:%M:%S %f'), "☆request☆☆☆☆☆☆", req)
    print(datetime.now().strftime('%Y-%m-%d %H:%M:%S %f'), "☆response☆☆☆☆☆☆", g.in_body)


    return jsonify(g.in_body)



@app.route('/mock/kbs/fund/ChangeRepayCard',methods=['POST'])
def mock_ChangeRepayCard():
    '''
        模拟查询放款结果
    :return: sonify(g.in_body)
    '''

    req = request.json
    try :
        if req["LoanCode"] is not None:
            print(req)
        else:
            print("缺少参数LoanCode")

    except Exception as ex:

        print("输入参数req   不正确")
        mock_body.req_output_ChangeRepayCard_ok["Data"]["Ext"] = "请求参数不正确"
        mock_body.req_output_ChangeRepayCard_ok["Data"]["Status"] = "40"

    reqpath = request.full_path
    g.in_body = mock_body.req_output_ChangeRepayCard_ok  ##导入返回参数
    print(datetime.now().strftime('%Y-%m-%d %H:%M:%S %f'), "☆request☆☆☆☆☆☆", reqpath)
    print(datetime.now().strftime('%Y-%m-%d %H:%M:%S %f'), "☆request☆☆☆☆☆☆", req)
    print(datetime.now().strftime('%Y-%m-%d %H:%M:%S %f'), "☆response☆☆☆☆☆☆", g.in_body)


    return jsonify(g.in_body)

@app.route('/mock/fundparty/hbcf/lcAppl', methods=['POST'])
def mock_hbcflcAppl():
    '''
    模拟放款方哈银消金的贷款申请接口
    :return:
    '''
    req = request.json
    try :
        if req  is not None:
            print(req)
        else:
            print("入参为空,输入错误")
    except Exception as ex:
        print("输入参数req   不正确")

    g.in_body = mock_body_hbcf.req_output_hbcf_lcappl_ok
    return jsonify(g.in_body)

@app.route('/mock/vbs/api/PolicyDecision/Execute',methods=['POST'])
def mock_PolicyDecision_Execute():
    '''
        模拟查询集团VBS决策结果
    :return: jsonify(g.in_body)
    '''
    req = request.json
    # try :
    #     if req["LoanCode"] is not None:
    #         print(req)
    #     else:
    #         print("缺少参数LoanCode")
    #
    # except Exception as ex:
    #
    #     print("输入参数req   不正确")
    #     mock_body.req_output_PolicyDecision_ok["Data"]["Ext"] = "请求参数不正确"
    #     mock_body.req_output_PolicyDecision_ok["Data"]["Status"] = "40"

    # reqpath = request.full_path

    print(mock_body_PolicyDecision.req_output_PolicyDecision_ok)
    try:
        req = request.json
        reqpath = request.full_path
        g.in_body = mock_body_PolicyDecision.req_output_PolicyDecision_ok  ##导入返回参数
    except:
        g.in_body ={"mes":"error"}

    print(datetime.now().strftime('%Y-%m-%d %H:%M:%S %f'), "☆request☆☆☆☆☆☆", reqpath)
    print(datetime.now().strftime('%Y-%m-%d %H:%M:%S %f'), "☆request☆☆☆☆☆☆", req)
    print(datetime.now().strftime('%Y-%m-%d %H:%M:%S %f'), "☆response☆☆☆☆☆☆", g.in_body)


    return jsonify(g.in_body)

@app.route('/mock/ccl/order/cancel/contract',methods=['POST'])
def mock_CancelContract():
    '''
    mock Appservice  函数名称:/order/cancel/contract
    :return:
    '''
    g.in_body = mock_body.req_output_cancelcontract ##导入返回参数
    req = request.json
    reqpath = request.full_path
    try:
        print(datetime.now().strftime('%Y-%m-%d %H:%M:%S %f'), "☆request☆☆☆☆☆☆", reqpath)
        print(datetime.now().strftime('%Y-%m-%d %H:%M:%S %f'), "☆request☆☆☆☆☆☆", req)
        print(datetime.now().strftime('%Y-%m-%d %H:%M:%S %f'), "☆response☆☆☆☆☆☆", g.in_body)
    except Exception as ee:
        print("Mock server处理异常")
        print(ee)
    return jsonify(g.in_body)

@app.route('/mock/ccl/customer/selectMobileScore',methods=['POST'])
def mock_selectMobileScore():
    '''
    mock Appservice  函数名称:/customer/selectMobileScore
    :return:
    '''
    g.in_body = mock_body.req_output_selectMobileScore ##导入返回参数
    req = request.json
    reqpath = request.full_path
    try:
        print(datetime.now().strftime('%Y-%m-%d %H:%M:%S %f'), "☆request☆☆☆☆☆☆", reqpath)
        print(datetime.now().strftime('%Y-%m-%d %H:%M:%S %f'), "☆request☆☆☆☆☆☆", req)
        print(datetime.now().strftime('%Y-%m-%d %H:%M:%S %f'), "☆response☆☆☆☆☆☆", g.in_body)
    except Exception as ee:
        print("Mock server处理异常")
        print(ee)
    return jsonify(g.in_body)



if __name__ == '__main__':
    command_kill = "ps -ef | grep java | grep '${TOMCAT_DIR}/bin' | awk '{print $2}' | sed -n '$p'| xargs kill -9"
    # ps -ef | grep java | grep '${TOMCAT_DIR}/bin' | awk '{print $2}' | sed -n '$p'| xargs kill -9
    cs = serverinfo.serverinfo()         ##实例化
    ip = cs.get_serverip_local()                    ##获取本地ip
    showlogo.showlog()
    app.run(host=ip , port=5000 ,debug=True )



