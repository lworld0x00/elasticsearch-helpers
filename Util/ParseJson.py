#!/usr/bin/env python3.7m
# -*- coding: utf-8 -*-
# @Date    : 2019-10-12 18:10:31
# @Author  : xrayl1 (1world0x00@gmail.com)
# @Editor  : Your Name (you@example.org)
# @Version : 1.0.0

import json
import sys
from os import path

sys.path.append(path.join(path.dirname(__file__), '..'))

from elasticsearch.helpers import scan

from elasticsearch import Elasticsearch, ElasticsearchException

from Common.ElasticLogin import ElasticSearchLogin

'''

此脚本用于获取ES服务器上数据，然后处理后导入本地ES
Json数据格式如下图所示(按照bulk接口规定)：
{ "index" : { "_index" : "test", "_type" : "_doc", "_id" : "1" } }
{ "field1" : "value1" }

'''


class ParseJson(object):
    def __init__(self):
        # pass
        self.es_inst = ElasticSearchLogin()
        self.es = self.es_inst.get_es_server()

    def download_data(self, index_name):
        result_list = []
        res = scan(
            self.es,
            query={
                "query": {
                    "match_all": {}
                },
            },
            index=index_name,
            scroll='1m'
        )
        # res是个generator
        for re in res:
            result_list.append(re)
        with open("index1.json", "w") as f:
            for doc in result_list:
                index_dict = {}
                index_dict['_index'] = doc.get('_index')
                index_dict['_type'] = doc.get('_type')
                index_dict['_id'] = doc.get('_id')
                final_index_dict = {}
                final_index_dict['index'] = index_dict
                source_dict = {}
                for item in doc['_source']:
                    source_dict[item] = doc['_source'].get(item)
                json.dump(final_index_dict, f)
                f.write('\n')
                json.dump(source_dict, f)
                f.write('\n')
            f.write('\n')


if __name__ == "__main__":
    pj = ParseJson()
    index_name = "test_index"
    pj.download_data(index_name)
