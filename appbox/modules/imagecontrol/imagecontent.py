#coding:utf-8
'''
title:   图片和base64码的转换
author:Robert
date:20180103
email:shuibo.luo@yitu-inc.com
other:
'''

import base64,os
from appbox.modules.loger import logger

class ImageContent(object):
        '''
        :return base64码或者可查看到图片
        '''

        def __init__(self,image_path,bs64codestr = None,newimagepath=None):
           '''

           :param image_path:   待转换图片的路径
           :param bs64codestr:   base64码字符
           :param newimagepath:  新生成的图片路径
           '''
           self.image_path =image_path
           self.bs64code = bs64codestr
           self.newimagepath = newimagepath


        def imagetob64(self):
            '''
            把照片转换成base64字符
            :return:     把照片转换成base64字符
            '''
            with open(self.image_path, "rb") as f:
                # 将读取的二进制文件转换为base64字符串
                bs64_str = base64.b64encode(f.read())
                # 打印图像转换base64格式的字符串,type结果为<class 'bytes'>
                # print("bs64_str",bs64_str.decode(encoding='utf-8'), type(bs64_str))
                f.close()
            logger.logger.debug(str("进行图片与base64转换 ")+self.image_path+" " )
            return bs64_str.decode(encoding='utf-8')


        def b64toimage(self):
            '''

            :return:
            '''
            # 将base64格式的数据装换为二进制数据
            imgdata = base64.b64decode(self.bs64codestr)
            # 将二进制数据装换为图片
            with open(self.newimagepath, "wb") as f2:
                f2.write(imgdata)
            return self.newimagepath

