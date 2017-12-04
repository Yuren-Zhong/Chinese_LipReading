import keras
from keras.models import Model, Sequential, load_model
import keras.layers as layers
from keras.regularizers import l2

import argparse

def gen_model(inputs, num_classes, use_max_pool):

    num_blocks = 3
    num_sub_blocks = 7
    num_filters = 16

    x = layers.Conv2D(
            filters = num_filters, 
            kernel_size = (3, 3), 
            padding = "same", 
            strides = 1, 
            kernel_initializer='he_normal',
            kernel_regularizer=l2(1e-4))(inputs)
    x = layers.BatchNormalization()(x)
    x = layers.Activation('relu')(x)

    if use_max_pool:
        x = MaxPooling2D(pool_size=3, strides=2, padding='same')(x)

    for i in range(num_blocks):
        for j in range(num_sub_blocks):
            strides = 1
            is_first_layer_but_not_first_block = j == 0 and i > 0
            last_layer_in_subblock = (j == num_sub_blocks - 1)
            if is_first_layer_but_not_first_block:
                strides = 2
            y = layers.Conv2D(num_filters,
                    kernel_size=3,
                    padding='same',
                    strides=strides,
                    kernel_initializer='he_normal',
                    kernel_regularizer=l2(1e-4))(x)
            y = layers.BatchNormalization()(y)
            y = layers.Activation('relu')(y)
            y = layers.Conv2D(num_filters,
                    kernel_size=3,
                    padding='same',
                    kernel_initializer='he_normal',
                    kernel_regularizer=l2(1e-4))(y)
            y = layers.BatchNormalization()(y)
            if is_first_layer_but_not_first_block:
                x = layers.Conv2D(num_filters,
                        kernel_size=1,
                        padding='same',
                        strides=2,
                        kernel_initializer='he_normal',
                        kernel_regularizer=l2(1e-4))(x)
            x = keras.layers.add([x, y])
			x = layers.Activation('relu')(x)

        num_filters = 2 * num_filters

    ##
    x = layers.AveragePooling2D()(x)
    x = layers.Flatten()(x)
    # x = layers.Dropout(0.2)(x)
    outputs = layers.Dense(num_classes, activation = "softmax", kernel_initializer='he_normal', name="deep_out")(x)

    ##
    model = Model(inputs, outputs)
    return model