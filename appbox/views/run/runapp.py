#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 19-4-2 下午3:00
# @Author  : Robert
# @File    : 33.py
# Title    :


from flask import Flask,Blueprint,g
from flask import request as flaskrequest
from flask import Markup
from flask import Request
from flask import Response
from appbox.views.home import showhomepage
from appbox.views.fp import fpresponse
from appbox.views.box import boxmock
from appbox.views.run import runapp
from appbox.modules.loger import logger
import config,json
from appbox import data_body


app = Flask(__name__,static_folder=config.static_dir,template_folder=config.template_dir)

bp = Blueprint('frontend', __name__, url_prefix='/<lang_code>')


@bp.url_defaults
def add_language_code(endpoint, values):
    values.setdefault('lang_code', g.lang_code)



@app.route('/')
def home():
    '''
    :return:
    '''
    obj_home =showhomepage.homepage()
    obj_home.defaulthomepage()
    return obj_home.defaulthomepage()



@app.route('/mock/box/demoA',methods=['POST'])
def boxdemoA():
    '''
    :return:
    '''
    logger.logger.info(flaskrequest.data)

    logger.logger.info(json.dumps(data_body.BOX_REQUEST_DEMO))
    return data_body.BOX_REQUEST_DEMO


@app.route('/mock/box/demoB',methods=['POST'])
def boxdemoB():
    '''
    :return:
    '''
    logger.logger.info(flaskrequest.data)
    obj_c =boxmock.boxMock()
    obj_c.manytimes(totalcount=1,intervaltime=1)

    return {"status":200}



@app.route('/mock/fp/response',methods=['POST','GET'])
def fpresponsedemo():
    rp =flaskrequest.data

    print(flaskrequest.data)
    print(flaskrequest.headers)

    if rp != None:
        logger.logger.info(flaskrequest.data)
    s_fp =fpresponse.FacePlatformMock()
    return s_fp.fpdemoresponse()


@app.route('/mock/fp/demoB',methods=['POST'])
def fpdemob():
    rp =flaskrequest.data

    print(json.dumps(flaskrequest.json))

    if rp != None:
        logger.logger.info(flaskrequest.data)
    s_fp =fpresponse.FacePlatformMock()
    return s_fp.fpdemoresponse()






if __name__=='__main__':
    try:
        logger.logger.info("服务启动中")
        app.run(host=config.HOST_NAME, port=config.HOST_PORT,
                debug=config.HOST_DEBUG_MODE,load_dotenv=True,
                threaded=True,processes=1)


    except Exception as e:
        logger.logger.error("服务启动失败")
        logger.logger.error(str(e))
    finally:
        logger.logger.info("服务停止成功")