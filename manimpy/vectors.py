'''
@Author       : Jin Yuhan
@Date         : 2020-03-25 17:23:04
@LastEditors  : Jin Yuhan
@LastEditTime : 2020-05-08 12:08:12
@Description  : 提供对向量/方向的操作
'''
from manimlib.imports import *
from typing import Union


def random_direction(scale: Union[float, np.ndarray] = 1, allow_z_directions: bool = False) -> np.ndarray:
    """
    获取一个随机的位移向量
    :param scale: 对向量大小的缩放
    :param allow_z_directions: 是否允许返回z轴的位移向量
    :return: 随机的位移向量
    """
    dirs = [LEFT, RIGHT, UP, DOWN, UR, UL, DR, DL]
    if allow_z_directions:
        dirs.append(IN)
        dirs.append(OUT)
    return random.choice(dirs) * scale


def vec(*args: float) -> np.ndarray:
    """
    构建一个n维向量
    :param args: 向量的所有分量
    :return: 根据参数构建的n维向量
    """
    return np.array(args)


def sqr_magnitude(v: np.ndarray) -> float:
    """
    计算向量的模长的平方
    :param v: 向量
    :return: 向量的模长的平方
    """
    result = 0
    for i in range(len(v)):
        result += v[i] ** 2
    return result


def magnitude(v: np.ndarray) -> float:
    """
    计算向量的模长
    :param v: 向量
    :return: 向量的模长
    """
    return np.sqrt(sqr_magnitude(v))


def normalize(v: np.ndarray) -> np.ndarray:
    """
    计算归一化向量（方向不变，模长为1）
    :param v: 向量
    :return: 归一化后的向量
    """
    return v / magnitude(v)


def sqr_distance(a: np.ndarray, b: np.ndarray) -> float:
    """
    计算两个点间距离的平方
    :param a: 点1
    :param b: 点2
    :return: a和b的距离的平方
    """
    return sqr_magnitude(a - b)


def distance(a: np.ndarray, b: np.ndarray) -> float:
    """
    计算两个点间距离
    :param a: 点1
    :param b: 点2
    :return: a和b的距离
    """
    return np.sqrt(sqr_distance(a, b))


def dot(v1: np.ndarray, v2: np.ndarray) -> float:
    """
    计算两个向量的点乘
    :param v1: 向量1
    :param v2: 向量2
    :return: v1, v2的点乘结果
    """
    result = 0.
    for i in range(np.min(len(v1), len(v2))):
        result += v1[i] * v2[i]
    return result


def angle(v1: np.ndarray, v2: np.ndarray) -> float:
    """
    计算两个向量的夹角度数（弧度制）
    :param v1: 向量1
    :param v2: 向量2
    :return: v1和v2间的角度
    """
    dot_product = dot(v1, v2)
    cos_value = dot_product / np.sqrt(sqr_magnitude(v1) * sqr_magnitude(v2))
    return np.arccos(cos_value)


def reflect(in_dir: np.ndarray, normal=DOWN) -> np.ndarray:
    """
    计算反射向量
    :param in_dir: 入射向量
    :param normal: 法线向量
    :return: 反射向量
    """
    return (-2 * dot(in_dir, normalize(normal))) * normal + in_dir


def cross(v1: np.ndarray, v2: np.ndarray) -> np.ndarray:
    """
    计算两个三维向量的叉乘
    :param v1: 向量1
    :param v2: 向量2
    :return: v1和v2的叉乘
    """
    return vec(v1[1] * v2[2] - v1[2] * v2[1], v1[2] * v2[0] - v1[0] * v2[2], v1[0] * v2[1] - v1[1] * v2[0])


def vertical_vec(v: np.ndarray) -> np.ndarray:
    """
    计算与当前向量垂直的向量
    :param v: 向量
    :return: 与当前向量垂直的向量
    """
    return vec(v[1], -v[0], v[2])


def x_of(v: np.ndarray) -> float:
    """
    获取向量的x分量
    :param v: 向量
    :return: 向量的x分量
    """
    return v[0]


def y_of(v: np.ndarray) -> float:
    """
    获取向量的y分量
    :param v: 向量
    :return: 向量的y分量
    """
    return v[1]


def z_of(v: np.ndarray) -> float:
    """
    获取向量的z分量
    :param v: 向量
    :return: 向量的z分量
    """
    return v[2]