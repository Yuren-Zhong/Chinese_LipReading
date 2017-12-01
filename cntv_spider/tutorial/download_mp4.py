# coding: utf8

import os
# 切换工作目录到项目根目录
project = os.path.split(os.path.realpath(__file__))[0]
os.chdir(project)

from lib.cntv import get_download_link

import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--url')
parser.add_argument('--index')

args = parser.parse_args()

if __name__ == '__main__':
        url = args.url
        index = args.index
        link = get_download_link(url, target_filename=index+'.mp4', quality_type=5, get_dlink_only=False, is_merge=False, is_remain=False)
