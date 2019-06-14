#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/4/9 下午9:07
# @Author  : Robert
# @File    : connectoss.py
# Title    :


# -*- coding: utf-8 -*-
import oss2



###AccessKey ID      [LTAIqzxJBydllAVR]
###Access Key Secret [4oXL3hwYsZhuzbtAYv0JHEbrrn79rj]


###连接 OSS

accesskeyid ='LTAIqzxJBydllAVR'
accesskeysecret ='4oXL3hwYsZhuzbtAYv0JHEbrrn79rj'

# 阿里云主账号AccessKey拥有所有API的访问权限，风险很高。强烈建议您创建并使用RAM账号进行API访问或日常运维，请登录 https://ram.console.aliyun.com 创建RAM账号。
auth = oss2.Auth(accesskeyid, accesskeysecret)
# Endpoint以杭州为例，其它Region请按实际情况填写。
bucket = oss2.Bucket(auth, 'http://oss-cn-shanghai.aliyuncs.com', 'yitu-face-private')

# 设置此签名URL在60秒内有效。
print(bucket.sign_url('GET', '全疆_买买提01.jpg', 60))


