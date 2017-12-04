import argparse
import keras
from keras import layers
import json
from convert_mp4 import mp4_to_numpy
from os import listdir
from os.path import isfile, join

parser = argparse.ArgumentParser(description='user defined variables')

args = parser.parse_args()

batch_size = 256
num_classes = 10
epochs = 500

dirpath = 'C:\\downloads\\test'

def build_dataset():
    with open('labels.json') as f:
        labels = json.load(f)
    for index in labels:
        res = int(labels[index])
        if res == 1:
            imgs_num = 20
        else:
            imgs_num = 10
        imgs = mp4_to_numpy(join(dirpath, str(index)+'.mp4'), imgs_num)
    


if __name__ = "__main__":
    x, y = build_dataset()