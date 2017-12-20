# -*- coding: utf-8 -*-

import codecs 
import io
import argparse
import json
import filecmp
from os import listdir, remove
from os.path import isfile, join
from shutil import copyfile

MIN_NUM = 0
MAX_NUM = 60000

index = list()

videodir_path = 'D:\\Chinese_LipReading\\cntv_spider\\tutorial\\selected\\new_videos'
scriptdir_path = 'D:\\Chinese_LipReading\\cntv_spider\\tutorial\\selected\\new_scripts'

if __name__ == '__main__':
    num = 0
    for i in range(MIN_NUM, MAX_NUM):
        if isfile(join(scriptdir_path, str(i)+'.txt')) == False:
            try:
                remove(join(videodir_path, str(i)+'.mp4'))
            except Exception:
                pass
            continue

        if isfile(join(videodir_path, str(i)+'.mp4')) == False:
            try:
                remove(join(scriptdir_path, str(i)+'.txt'))
            except Exception:
                pass
            continue

        flag = True
        for idx in index:
            #print(idx, i)
            if filecmp.cmp(join(videodir_path, str(i)+'.mp4'), join(videodir_path, str(idx)+'.mp4'), shallow=False):
                num += 1
                flag = False
                print(i, idx)

                remove(join(videodir_path, str(i)+'.mp4'))
                remove(join(scriptdir_path, str(i)+'.txt'))
                break
        if flag:
            index.append(i)
    print("NUM : ", num)