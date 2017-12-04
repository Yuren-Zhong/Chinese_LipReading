import argparse
import json
from convert_mp4 import mp4_to_numpy
from os import listdir
from os.path import isfile, join

rgb_range = [   # [point num][3d][list of possible value]
        # p0
        [   [[210, 255],    [0, 160]],
            [[40, 180],     [0, 80]],
            [[0, 100],      [0, 60]]
        ],
        # p1
        [   [[210, 255],    [0, 160]],
            [[40, 180],     [0, 80]],
            [[0, 100],      [0, 60]]
        ],
        # p2
        [   [[70, 200],     [0, 150]],
            [[0, 100],      [0, 90]],
            [[0, 80],       [0, 60]]
        ],
        # p3
        [   [[0, 180]],
            [[0, 80]],
            [[0, 60]]
        ],
        # p4
        [   [[70, 200],     [0, 150]],
            [[0, 100],      [0, 90]],
            [[0, 80],       [0, 60]]
        ],
        # p5
        [   [[70, 200],     [0, 150]],
            [[0, 100],      [0, 90]],
            [[0, 80],       [0, 60]]
        ],
        # p6
        [   [[70, 250],     [0, 150]],
            [[0, 150],      [0, 90]],
            [[0, 120],       [0, 60]]
        ],
        # p7
        [   [[70, 250],     [0, 150]],
            [[0, 150],      [0, 90]],
            [[0, 120],      [0, 60]]
        ],
        # p8
        [   [[0, 250]],
            [[60, 190]],
            [[60, 190]]
        ],
        # p9
        [   [[50, 170]],
            [[0, 100]],
            [[0, 70]]
        ],
        # p10
        [   [[0, 150],      [50, 200],      [100, 255]],
            [[0, 150],      [50, 200],      [100, 255]],
            [[0, 150],      [50, 200],      [100, 255]]
        ],
        # p11
        [   [[0, 150],      [50, 200],      [100, 255]],
            [[0, 150],      [50, 200],      [100, 255]],
            [[0, 150],      [50, 200],      [100, 255]]
        ],
        # p12
        [   [[70, 250],     [0, 150]],
            [[50, 200],     [0, 150]],
            [[0, 120],      [0, 60]]
        ],
        # p13
        [   [[40, 200],     [0, 150]],
            [[30, 150],     [0, 100]],
            [[0, 120],      [0, 100]]
        ],
        # p14
        [   [[80, 220],     [0, 150]],
            [[70, 200],     [0, 120]],
            [[60, 190],      [0, 100]]
        ],
        # p15
        [   [[135, 255],     [0, 150]],
            [[120, 255],     [0, 120]],
            [[100, 255],      [0, 100]]
        ]
    ]

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

def in_range(range_list, val):
    for rg in range_list:
        a = rg[0]
        b = rg[1]
        if val >= a and val <= b:
            return True
    return False

def check_point(img, i):
    global rgb_range
    global points
    x = points[i][0]
    y = points[i][1]
    ranges = rgb_range[i]
    range1 = ranges[0]
    range2 = ranges[1]
    range3 = ranges[2]
    values = img[x][y]
    value1 = values[0]
    value2 = values[1]
    value3 = values[2]
    if in_range(range1, value1) and in_range(range2, value2) and in_range(range3, value3):
        return True
    print(value1, value2, value3)
    return False

def check_img(img):
    for i in range(16):
        if check_point(img, i) == False:
            print('point '+str(i)+' wrong')
            return False
    return True

if __name__ == '__main__':
    videodir_path = 'D:\\Chinese_LipReading\\cntv_spider\\tutorial\\videos'
    imgs = mp4_to_numpy(join(videodir_path, '136.mp4'), 10)
    for img in imgs:
        check_img(img)