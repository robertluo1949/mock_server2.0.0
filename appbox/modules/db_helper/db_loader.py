#!/usr/bin/env python
# -*- coding: utf-8 -*-

import atexit
import  pymysql
from threading import Lock
from apscheduler.schedulers.background import BackgroundScheduler
from appbox import data_body

class db_loader():

    __instance = None

    person_list = {}
    lock = Lock()

    @staticmethod
    def get_instance():
        if db_loader.__instance == None:
            db_loader()
        return db_loader.__instance

    def __init__(self):
        if db_loader.__instance != None:
            raise Exception("This class is a singleton!")
        else:
            ##执行定时任务
            self.refresh_person_list()
            scheduler = BackgroundScheduler()
            scheduler.add_job(func=self.refresh_person_list,
                              trigger="interval",
                              seconds=10)
            scheduler.start()

            # Shut down the scheduler when exiting the app
            atexit.register(lambda: scheduler.shutdown())
            db_loader.__instance = self

    def get_person_list(self):
        with self.lock:
           return self.person_list

    def refresh_person_list(self):
        '''
           添加定时任务
        :return:
        '''
        with self.lock:
            conn = pymysql.connect(host=data_body.SanHuiBigDB_connect["connect"]["host"],
                                   user=data_body.SanHuiBigDB_connect["connect"]["user"],
                                   passwd=data_body.SanHuiBigDB_connect["connect"]["passwd"],
                                   db=data_body.SanHuiBigDB_connect["connect"]["db"])
            cur = conn.cursor()
            cur.execute(data_body.SanHuiBigDB_connect["exceselect"])
            for r in cur:
                self.person_list[r[0]] = r[1]
            cur.close()
            conn.close()