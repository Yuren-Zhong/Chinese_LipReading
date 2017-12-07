# -*- coding: utf-8 -*-

import codecs 
import io
import argparse
import json
from os import listdir, remove
from os.path import isfile, join
from shutil import copyfile

MIN_NUM = 0
MAX_NUM = 8010

titles = list()

videodir_path = 'D:\\Chinese_LipReading\\cntv_spider\\tutorial\\selected\\videos'
scriptdir_path = 'D:\\Chinese_LipReading\\cntv_spider\\tutorial\\selected\\scripts'

if __name__ == '__main__':
    num = 0
    for i in range(MIN_NUM, MAX_NUM):
        if isfile(join(scriptdir_path, str(i)+'.txt')) == False:
            continue

        with io.open(join(scriptdir_path, str(i)+'.txt'), 'r', encoding='utf-8') as file:
            title = file.readline()
        if title in titles:
            num += 1
            # remove
            try:
                remove(join(scriptdir_path, str(i)+'.txt'))
                remove(join(videodir_path, str(i)+'.mp4'))
            except Exception as e:
                print(e)
            j = 0
            for t in titles:
                if t == title:
                    print(j, i)#, title.encode('utf-8'))
                    break
                j +=1
        else:
            titles.append(title)

    print("NUM : ", num)