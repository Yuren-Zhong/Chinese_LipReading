from matplotlib import pylab
import imageio

import cv2
import numpy as np

dirpath = 'C:\\downloads\\flv\\x_train\\'
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

def mp4_to_numpy(filepath):
    cap = cv2.VideoCapture(filepath)
    frameCount = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    frameWidth = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    frameHeight = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

    buf = np.empty((frameCount, frameHeight, frameWidth, 3), np.dtype('uint8'))

    fc = 0
    ret = True

    while (fc < frameCount  and ret):
        ret, buf[fc] = cap.read()
        fc += 1

    cap.release()

    cv2.namedWindow('frame')
    cv2.imshow('frame', buf[287])

    cv2.waitKey(0)

mp4_to_numpy(dirpath+filename+filesuffix)