from matplotlib import pylab
import imageio

import cv2
import numpy as np

from os import listdir
from os.path import isfile, join

dirpath = 'C:\\downloads\\test'
filesuffix = '.mp4'
filename = '0001'

def f():
    vid = imageio.get_reader(dirpath+filename+filesuffix,  'ffmpeg')
    nums = [287]
    for num in nums:
        image = vid.get_data(num)
        fig = pylab.figure()
        fig.suptitle('image #{}'.format(num), fontsize=20)
        pylab.imshow(image)
    pylab.show()

def mp4_to_numpy(filepath, imgname):
    cap = cv2.VideoCapture(filepath)
    frameCount = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    frameWidth = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    frameHeight = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

    print(frameHeight, frameWidth)

    buf = np.empty((frameCount, frameHeight, frameWidth, 3), np.dtype('uint8'))

    fc = 0
    ret = True

    while (fc < frameCount  and ret):
        ret, buf[fc] = cap.read()
        fc += 1

    cap.release()

    length = len(buf)
    picked = list()
    for 

    cv2.imwrite(join(dirpath, imgname+'.png'), buf[10])

if __name__ == "__main__":
    onlyfiles = [f for f in listdir(dirpath) if isfile(join(dirpath, f))]

    for file in onlyfiles:
        print(file)
        try:
            mp4_to_numpy(join(dirpath, file), file)
        except Exception as e:
            pass
