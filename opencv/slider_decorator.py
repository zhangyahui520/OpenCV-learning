#!/usr/bin/env python
# coding=utf-8
"""
    Copyright (C) 2019 * Ltd. All rights reserved.
 
    Editor      : PyCharm
    File name   : slider_decorator.py
    Author      : Charles
    Created date: 2020/8/7 3:52 下午
    Description :
       OpenCV 滑动框装饰器

"""
import functools
import cv2


def nothing(x):
    pass


def slider_decorator(trackName, wname, min_num, max_num, rate):
    def _slider_decorator(func):
        @functools.wraps(func)
        def call_func(*args):
            # 定义窗口
            cv2.namedWindow(wname, cv2.WINDOW_NORMAL)
            cv2.createTrackbar(trackName, wname, min_num, max_num, nothing)
            flag = -1  # 增加一个判断标记，放置多次访问函数
            while 1:
                # 如果值变化了，才会进行函数返回
                value = cv2.getTrackbarPos(trackName, wname)  # gamma取值
                value = value * rate  # 压缩gamma范围，以进行精细调整
                if flag != value:
                    image_gamma_correct = func(*args, value)  # 2.5为gamma函数的指数值，大于1曝光度下降，大于0小于1曝光度增强
                    flag = value
                cv2.imshow(wname, image_gamma_correct)
                k = cv2.waitKey(1)
                if k == 13:  # 按回车键退出
                    cv2.destroyAllWindows()
                    break

        return call_func

    return _slider_decorator
