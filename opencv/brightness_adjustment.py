#!/usr/bin/env python
# coding=utf-8
"""
    Copyright (C) 2019 * Ltd. All rights reserved.
 
    Editor      : PyCharm
    File name   : brightness_adjustment.py
    Author      : Charles
    Created date: 2020/7/23 8:31 下午
    Description :
        亮度是调整图像像素的的整体强度
        对比度调整指的是将图像暗处变得更暗，亮处变得更亮，从而扩展某个区域内的显示精度
       
"""
import cv2
import numpy as np

from slider_decorator import slider_decorator


@slider_decorator('brightness', 'pixel_afjustemnt', 100, 1000, 0.1)
def brightness_adjustment(img, beta=0, show=False):
    '''
    亮度调整函数, 必须*1.0，不然会出现clip无法限制的问题。
    :param bias: 控制亮度的值
    :return:
    '''
    res = np.uint8(np.clip((img * 1.0 + beta), 0, 255))

    if show:
        tmp = np.hstack((img, res))  # 将两张图片横向合并，便于显示
        cv2.namedWindow(f'brightness:{beta}', cv2.WINDOW_NORMAL)
        cv2.imshow(f'brightness:{beta}', tmp)
        cv2.waitKey(0)

    return res

@slider_decorator('contrast', 'pixel_afjustemnt', 100, 1000, 0.01)
def contrast_adjustment(img, alpha=1.0, show=False):
    '''
    对比度调整函数，通过公式计算bias的值
    :param img:
    :param weight:
    :param show:
    :return:
    '''

    beta = 125 * (1 - alpha)
    res = np.uint8(np.clip(img * alpha + beta, 0, 255))

    if show:
        tmp = np.hstack((img, res))  # 将两张图片横向合并，便与展示
        cv2.namedWindow(f'contrast:{alpha}', cv2.WINDOW_NORMAL)
        cv2.imshow(f'contrast:{alpha}', tmp)
        cv2.waitKey(0)

    return res


if __name__ == '__main__':
    path = '/Users/chracles/PycharmProjects/yolo_object_detection_system/data/image/lizi.jpg'

    img = cv2.imread(path)
    # for beta in range(-100, 100, 30):
    #     print('增加亮度:{}'.format(beta))
    #     brightness_adjustment(img, beta, True)
    #
    # for alpha in range(1, 20, 3):
    #     print('增加对比度:{}'.format(alpha))
    #     contrast_adjustment(img, alpha / 10, True)

    brightness_adjustment(img)