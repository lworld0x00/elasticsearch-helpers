#!/usr/bin/env python3.7m
# -*- coding: utf-8 -*-
# @Date    : 2019-10-12 18:10:12
# @Author  : xrayl (1world0x00@gmail.com)
# @Editor  : Your Name (you@example.org)
# @Version : 1.0.0

'''

此脚本用于将获取的指定格式的Json文件导入ES中
使用python elasticsearch api中的bulk接口

'''

import sys
from os import path
sys.path.append(path.join(path.dirname(__file__), '../..'))

from elasticsearch import Elasticsearch
from elasticsearch import ElasticsearchException
from Common.ElasticLogin import ElasticSearchLogin
import json

class ImportES(object):
    pass

