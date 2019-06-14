#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 19-4-2 下午3:00
# @Author  : Robert
# @File    : app.py
# Title    :


from flask import Flask
from appbox.views.home import showhomepage
from appbox.modules.routemap import routemapmockserver
from appbox.modules.loger import logger
from appbox.modules.db_helper import db_loader
import config

app = Flask(__name__,static_folder=config.static_dir,template_folder=config.template_dir)


@app.route('/')
def home():
    '''
    :return:
    '''
    obj_home =showhomepage.homepage()
    obj_home.defaulthomepage()
    return obj_home.defaulthomepage()

###对http 请求URL 进行映射
@app.route('/mock/<server>/<action>',methods=['POST'])
def serveraction(server,action):
    '''
    :param server:
    :param action:
    :return:
    '''
    __routemap=routemapmockserver.RouteMapMockServer()
    return_body =__routemap.mapserveraction(mockserver=server, mockaction=action)
    return return_body

@app.route("/VIID/<vsystem>/<vaction>",methods=['POST'])

def viidsysaction(vsystem,vaction):
    __routemap=routemapmockserver.RouteMapMockServer()
    return_body =__routemap.viidregisterroutemap(vsystem, vaction)
    return return_body

@app.route("/VIID/<vaction>",methods=['POST'])
def viidaction(vaction):
    __routemap=routemapmockserver.RouteMapMockServer()
    return_body =__routemap.viidroutemap(vaction)
    return return_body


@app.route("/dx/v1/init/<dxaction>",methods=['POST'])
def dxinitdaction(dxaction):
    __routemap=routemapmockserver.RouteMapMockServer()
    return_body =__routemap.dxinitroutemap(dxaction)
    return return_body

@app.route("/SynPreventTrace/<shaction>",methods=['POST'])
def sanhuiction(shaction):
    __routemap=routemapmockserver.RouteMapMockServer()
    return_body =__routemap.sanhuiroutemap(shaction)
    return return_body

@app.route("/business/api/<fpaction>",methods=['POST','GET'])
@app.route("/business/api/user/<fpaction>",methods=['POST','GET'])
@app.route("/face/v1/framework/face_image/repository/picture/<fpaction>",methods=['POST'])
def fpaction(fpaction):
    '''
    :param fpaction:
    :return:
    '''
    __routemap=routemapmockserver.RouteMapMockServer()
    return_body=__routemap.faceplatformroutemap(fpaction)
    return return_body


##程序入口
if __name__=='__main__':
    try:
        loader = db_loader.db_loader.get_instance()
        logger.logger.info("服务启动中")
        app.run(host=config.HOST_NAME, port=config.HOST_PORT,
                debug=config.HOST_DEBUG_MODE,load_dotenv=True,
                threaded=True,processes=0,use_reloader=False)

    except Exception as e:
        logger.logger.error("服务启动失败")
        logger.logger.error(str(e))
    finally:
        logger.logger.info("服务停止成功")