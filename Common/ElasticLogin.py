#!/usr/bin/env python3.7m
# -*- coding: utf-8 -*-
# @Date    : 2019-10-12 18:07:16
# @Author  : xrayl (1world0x00@gmail.com)
# @Editor  : Your Name (you@example.org)
# @Version : 1.0.0
import sys
from os import path

sys.path.append(path.join(path.dirname(__file__), '..'))

from elasticsearch import Elasticsearch
from elasticsearch import ConnectionError
from Util.Logger import Logger
from Util import get_config


class ElasticSearchLogin:

    """
    参数说明：
    server: elasticsearch服务器
    port: elasticsearch服务端口
    http_user: 认证用户名，默认为空值
    http_pass: 认证密码，默认为空值
    """

    def __init__(self):
        self.server = get_config('ES', 'ES_SERVER')
        self.port = int(get_config('ES', 'ES_PORT'))
        self.http_user = get_config('ES', 'ES_USERNAME')
        self.http_pass = get_config('ES', 'ES_PASSWORD')
        self.logger = Logger().get_logger

    """
    
    """

    def get_es_server(self):
        es_servers = [{
            "host": self.server,
            "port": self.port
        }]
        http_auth = (self.http_user, self.http_pass)
        es = Elasticsearch(hosts=es_servers, http_auth=http_auth)
        try:
            es.info()
        except ConnectionError as err:
            self.logger.error("ES连接失败")
            exit(-1)
        else:
            self.logger.info("ES连接成功")
            return es
