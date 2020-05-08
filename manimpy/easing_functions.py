'''
@Author       : Jin Yuhan
@Date         : 2020-05-01 12:09:22
@LastEditors  : Jin Yuhan
@LastEditTime : 2020-05-01 12:18:40
@Description  : 缓动函数
'''
import numpy as np

def ease_out(x):
    t = 1 - x
    return 1 - (t ** 3 - 0.3 * t * np.sin(t * np.pi))