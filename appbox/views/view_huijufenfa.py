#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 19-4-3 下午3:19
# @Author  : Robert
# @File    : view_huijufenfa.py
# Title    :


from flask import Blueprint

huijufenfa =Blueprint('huijufenfa',__name__)

@huijufenfa.route('dx/v1/init/subscribes')
def subscribes():
    return