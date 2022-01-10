#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-

#########################################################
#
# Copyright (c) 2022 Baidu.com, Inc. All Rights Reserved
#
#########################################################
"""
configration file load
"""
import os

def get_conf(conf_file):
    url = os.path.join('./conf/', conf_file)
    with open(url, 'r') as f:
        print(f.readlines())

def sum(nums):
    print(sum(nums))