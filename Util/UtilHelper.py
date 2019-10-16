#!/usr/bin/env python3.7m
# -*- coding: utf-8 -*-
# @Date    : 2019-10-12 18:24:51
# @Author  : xrayl (1world0x00@gmail.com)
# @Editor  : Your Name (you@example.org)
# @Version : 1.0.0

from os.path import dirname, join

ROOT_DIR = dirname(dirname(__file__))


def get_file_path(*path):

    return join(ROOT_DIR, *path)


