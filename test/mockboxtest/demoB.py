#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 19-4-2 下午6:29
# @Author  : Robert
# @File    : demoB.py
# Title    :

from appbox.views.box import boxmock



c =boxmock.boxMock()
c.manytimes(totalcount=3,intervaltime=3)