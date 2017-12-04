from matplotlib import pylab
import imageio
from random import randint

import cv2
import numpy as np

from os import listdir
from os.path import isfile, join

dirpath = '/home/yurzho/Chinese_LipReading/mp4_filter/test'
filesuffix = '.mp4'

def mp4_to_numpy(filepath, image_num):
    cap = cv2.VideoCapture(filepath)
    frameCount = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    frameWidth = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    frameHeight = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

    print(frameHeight, frameWidth)
    print(filepath)

    buf = np.empty((frameCount, frameHeight, frameWidth, 3), np.dtype('uint8'))

    fc = 0
    ret = True

    while (fc < frameCount  and ret):
        ret, buf[fc] = cap.read()
        fc += 1

    cap.release()

    length = len(buf)
    picked = list()
    total = image_num
    while total > 0:
        x = randint(int(length/4), int(length*4/5))
        if x not in picked:
            picked.append(x)
            total -= 1

    ret = list()
    for i in picked:
        raw = buf[i]
        ret.append(buf[i])

    return ret


    cv2.imwrite(join(dirpath, imgname+'.png'), buf[10])

if __name__ == "__main__":
    onlyfiles = [f for f in listdir(dirpath) if isfile(join(dirpath, f))]

    for file in onlyfiles:
        print(file)
        try:
            mp4_to_numpy(join(dirpath, file), file)
        except Exception as e:
            pass
