# coding: utf8

import os
# 切换工作目录到项目根目录
project = os.path.split(os.path.realpath(__file__))[0]
os.chdir(project)

from lib.cntv import get_download_link


if __name__ == '__main__':
        url = 'http://tv.cctv.com/2017/11/28/VIDETRtb7usiG8XC3Om6ovxg171128.shtml'
        get_download_link(url, quality_type=5, get_dlink_only=False, is_merge=True, is_remain=False)
