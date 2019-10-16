#!/usr/bin/env python3.7m
# -*- coding: utf-8 -*-
# @Date    : 2019-10-12 17:58:45
# @Author  : xrayl (1world0x00@gmail.com)
# @Version : 1.0.0

import logging
from Util.UtilHelper import get_file_path
from logging.config import fileConfig


class Logger:
    def __init__(self):
        pass

    @property
    def get_logger(self):
        logging_config = get_file_path('Conf\logging.ini')
        print(logging_config)
        fileConfig(logging_config)

        return logging.getLogger('Audit')
