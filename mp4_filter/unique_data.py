# -*- coding: utf-8 -*-

import codecs 
import io
import argparse
import json
from os import listdir
from os.path import isfile, join
from shutil import copyfile

MIN_NUM = 0
MAX_NUM = 2750

titles = list()

videodir_path = 'D:\\Chinese_LipReading\\cntv_spider\\tutorial\\selected\\videos'
scriptdir_path = 'D:\\Chinese_LipReading\\cntv_spider\\tutorial\\selected\\scripts'

if __name__ == '__main__':
	i = MIN_NUM
	num = 0
	while i < MAX_NUM:
		if isfile(join(scriptdir_path, str(i)+'.txt')) == False:
			i += 1
			continue

		with io.open(join(scriptdir_path, str(i)+'.txt'), 'r', encoding='utf-8') as file:
			title = file.readline()
		if title in titles:
			num += 1
			# remove
			j = 0
			for t in titles:
				if t == title:
					print(j, i)#, title.encode('utf-8'))
					break
				j +=1
		else:
			titles.append(title)
		i += 1
	print("NUM : ", num)