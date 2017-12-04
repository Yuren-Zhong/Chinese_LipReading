from convert_mp4 import mp4_to_numpy
import json
from os.path import isfile, join

if __name__ == '__main__':
    with open('D:\\Chinese_LipReading\\mp4_filter\\labels.json') as file:
        data = json.load(file)

    points = [
        [60,  60],
        [60,  80],
        [60,  420],
        [60,  400],
        [80,  60],
        [80,  80],
        [80,  420],
        [80,  400],
        [300, 60],
        [300, 80],
        [300, 420],
        [300, 400],
        [280, 60],
        [280, 80],
        [280, 420],
        [280, 400]
        ]

    p_y = list()
    p_n = list()

    for i in range(16):
        p_y.append(list())
        p_n.append(list())

    videodir_path = 'D:\\Chinese_LipReading\\cntv_spider\\tutorial\\videos'

    if type(data) == dict:
        max_num = 10
        total = 1
        for index, res in data.items():
            if (total == max_num):
                break
            total += 1
            img_num = 3
            imgs = mp4_to_numpy(join(videodir_path, index+'.mp4'), img_num)
            if res == 0:
                for j in range(img_num):
                    img = imgs[j]
                    for i in range(16):
                        x = points[i][0]
                        y = points[i][1]
                        p_n[i].append(img[x][y])

            else: # res == 1
                for j in range(img_num):
                    img = imgs[j]
                    for i in range(16):
                        x = points[i][0]
                        y = points[i][1]
                        p_y[i].append(img[x][y])

    for i in range(16):
        with open('out_y_'+str(i)+'.txt', 'a') as file:
            file.write('\n'+str(p_y[i]))

        with open('out_n_'+str(i)+'.txt', 'a') as file:
            file.write('\n'+str(p_n[i]))