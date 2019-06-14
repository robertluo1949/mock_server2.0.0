#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 19-4-6 上午10:49
# @Author  : Robert
# @File    : randomtest.py
# Title    :


print ('中国')

# 以指定的概率获取元素 以一个列表为基准概率，从一个列表中随机获取元素

import random


def random_pick(some_list, probabilities):
    x = random.uniform(0, 1)
    cumulative_probability = 0.0
    for item, item_probability in zip(some_list, probabilities):
        cumulative_probability += item_probability
        if x < cumulative_probability: break
    print(item)
    return item


some_list = [1, 2, 3, 4]
probabilities = [0.1, 0.2, 0.3, 0.4]

# print (random_pick(some_list, probabilities))


# 根据权重来获取 核心在于权重乘以 就相当于次数

def random_pick_odd(some_list, odds):
    print ('table2')
    table = [z for x, y in zip(some_list, odds) for z in [x] * y]
    print (table)
    return random.choice(table)


some_list = [1, 2, 3, 4]
odds = [3, 1, 4, 2]

# print (random_pick_odd(some_list, odds))

# for item in random_picks()


def testrandom_pick():

    count1=1
    count2=2
    count3=3
    count4=4
    index =0

    while index< 100:
        r =random_pick(some_list,probabilities)
        if r==1:
            count1+=1
        elif r==2:
            count2+=1
        elif r==3:
            count3+=1
        elif r==4:
            count4+=1
        else:
            print("error")
        index+=1
    return "count1",count1,",count2",count2,",count3",count3,",count4",count4
print(testrandom_pick())
