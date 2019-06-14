#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/4/8 下午10:09
# @Author  : Robert
# @File    : pushdatahub.py
# Title    :

import sys
import traceback
from datahub import DataHub
from datahub.exceptions import ResourceExistException
from datahub.models import FieldType, RecordSchema, TupleRecord, BlobRecord, CursorType, RecordType

access_id = "LTAIFk1MAdnLWVcJ"
access_key =" WObRiv45dnf6GKjjT3Ef7ZthKaVVZF"
endpoint = "https://dh-cn-shanghai.aliyuncs.com"
project_name ="boxqatest"
topic_name ="whitelist"
# records=[("records1")]


def connectDH(access_id, access_key, endpoint):
    dh = DataHub(access_id, access_key, endpoint)
    print(dh)
    return dh
# project_name = 'project'
# comment = 'comment'

def CreatePro(dh,project_name, comment):
    try:
        dh.create_project(project_name, comment)
        print("create project success!")
        print("=======================================\n\n")
    except ResourceExistException:
        print("project already exist!")
        print("=======================================\n\n")
    except Exception as e:
        print(traceback.format_exc())
        sys.exit(-1)



topic_name = "tuple_topic"
shard_count = 3
life_cycle = 7

def UpdateTopic(dh):
    record_schema = RecordSchema.from_lists(
        ['bigint_field', 'string_field', 'double_field', 'bool_field', 'time_field'],
        [FieldType.BIGINT, FieldType.STRING, FieldType.DOUBLE, FieldType.BOOLEAN, FieldType.TIMESTAMP])
    try:
        dh.create_tuple_topic(project_name, topic_name, shard_count, life_cycle, record_schema, comment)
        print("create tuple topic success!")
        print("=======================================\n\n")
    except ResourceExistException:
        print("topic already exist!")
        print("=======================================\n\n")
    except Exception as e:
        print(traceback.format_exc())
        sys.exit(-1)



def defineschema(dh,json_str):
    record_schema_1 = RecordSchema.from_json_str(json_str)
    return record_schema_1


##数据发布/订阅
#####--获取Shard列表

def getShards(dh):
    shard_result = dh.list_shard(project_name, topic_name)
    shards = shard_result.shards
    print("获取Shard列表 "+str(len(shards)))
    return shards


###--发布数据

def pubRecords(dh,records):
    put_result = dh.put_records(project_name, topic_name, records)
    print("发布数据 "+str(put_result.failed_record_count))
    print(put_result.failed_records)




# ##----写入Tuple类型Record示例
# try:
#     # block等待所有shard状态ready
#     dh.wait_shards_ready(project_name, topic_name)
#     print("shards all ready!!!")
#     print("=======================================\n\n")
#     topic_result = dh.get_topic(project_name, topic_name)
#     print(topic_result)
#     if topic_result.record_type != RecordType.TUPLE:
#         print("topic type illegal!")
#         sys.exit(-1)
#     print("=======================================\n\n")
#     record_schema = topic_result.record_schema
#     records0 = []
#     record0 = TupleRecord(schema=record_schema, values=[1, 'yc1', 10.01, True, 1455869335000000])
#     record0.shard_id = '0'
#     record0.put_attribute('AK', '47')
#     records0.append(record0)
#     record1 = TupleRecord(schema=record_schema)
#     record1.set_value('bigint_field', 2)
#     record1.set_value('string_field', 'yc2')
#     record1.set_value('double_field', None)
#     record1.set_value('bool_field', False)
#     record1.set_value('time_field', 1455869335000011)
#     record1.hash_key = '4FFFFFFFFFFFFFFD7FFFFFFFFFFFFFFD'
#     records0.append(record1)
#     record2 = TupleRecord(schema=record_schema)
#     record2.set_value(0, 3)
#     record2.set_value(1, 'yc3')
#     record2.set_value(2, 1.1)
#     record2.set_value(3, False)
#     record2.set_value(4, 1455869335000011)
#     record2.attributes = {'key': 'value'}
#     record2.partition_key = 'TestPartitionKey'
#     records0.append(record2)
#     put_result = dh.put_records(project_name, topic_name, records0)
#     print(put_result)
#     print("put tuple %d records, failed count: %d" % (len(records0), put_result.failed_record_count))
#     # failed_record_count如果大于0最好对failed record再进行重试
#     print("=======================================\n\n")
# except DataHub.DatahubException as e:
#     print(e)
#     sys.exit(-1)



curdh =connectDH(access_id=access_id,access_key=access_key,endpoint=endpoint)
