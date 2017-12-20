# -*- coding: utf-8 -*-

from os.path import isfile, join

MIN_NUM = 0
MAX_NUM = 60000

scriptdir_path = 'D:\\Chinese_LipReading\\cntv_spider\\tutorial\\selected\\new_scripts'

eng_char = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

def delete_firstline(filepath):
    # done 
    script_exist = isfile(filepath)
    if script_exist:
        with open(filepath, 'r', encoding='utf-8') as fin:
            data = fin.read().splitlines(True)
        with open(filepath, 'w', encoding='utf-8') as fout:
            fout.writelines(data[1:])

def delete_xinwenlianbo(filepath):
    script_exist = isfile(filepath)
    if script_exist:
        with open(filepath, 'r', encoding='utf-8') as fin:
            data = fin.read()
        new_data = data.replace(u'（新闻联播）：', '')
        new_data = new_data.replace(u'(新闻联播)：', '')
        with open(filepath, 'w', encoding='utf-8') as fout:
            fout.write(new_data)

def delete_and(filepath):
    script_exist = isfile(filepath)
    if script_exist:
        with open(filepath, 'r', encoding='utf-8') as fin:
            data = fin.read()
        and_found = False
        to_delete = list()
        i = 0
        for c in data:
            if c == '&' and and_found == False:
                to_delete.append(i)
                and_found = True
            if c == ';' and and_found == True:
                to_delete.append(i+1)
                and_found = False
            i += 1

        if len(to_delete) % 2 == 1:
            to_delete.append(len(data))
        to_delete.insert(0, 0)
        to_delete.append(len(data))    
        n = len(to_delete)
        new_data = ''
        j = 0
        while j < n:
            new_data += data[to_delete[j]:to_delete[j+1]]
            j += 2

        with open(filepath, 'w', encoding='utf-8') as fout:
            fout.write(new_data)

def delete_html_tag(filepath):
    script_exist = isfile(filepath)
    if script_exist:
        with open(filepath, 'r', encoding='utf-8') as fin:
            data = fin.read()
        right_bracket_found = False
        to_delete = list()
        i = 0
        for c in data:
            if c == '<' and right_bracket_found == False:
                to_delete.append(i)
                right_bracket_found = True
            if c == '>' and right_bracket_found == True:
                to_delete.append(i+1)
                right_bracket_found = False
            i += 1

        if len(to_delete) % 2 == 1:
            to_delete.append(len(data))
        to_delete.insert(0, 0)
        to_delete.append(len(data))    
        n = len(to_delete)
        new_data = ''
        j = 0

        while j < n:
            new_data += data[to_delete[j]:to_delete[j+1]]
            j += 2

        with open(filepath, 'w', encoding='utf-8') as fout:
            fout.write(new_data)

def delete_blank(filepath):
    script_exist = isfile(filepath)
    if script_exist:
        with open(filepath, 'r', encoding='utf-8') as fin:
            data = fin.read()

        new_data = data.replace(' ', '')
        new_data = data.replace('\n', '')
        new_data = data.replace('\t', '')
        new_data = data.replace('　', '')

        with open(filepath, 'w', encoding='utf-8') as fout:
            fout.write(new_data)

def count_js(filepath):
    script_exist = isfile(filepath)
    if script_exist:
        with open(filepath, 'r', encoding='utf-8') as fin:
            data = fin.read()
        if 'script' in data:
            print(filepath)

for i in range(MIN_NUM, MAX_NUM):
    #delete_html_tag(join(scriptdir_path, str(i)+'.txt'))
    #delete_and(join(scriptdir_path, str(i)+'.txt'))
    #delete_xinwenlianbo(join(scriptdir_path, str(i)+'.txt'))
    delete_blank(join(scriptdir_path, str(i)+'.txt'))