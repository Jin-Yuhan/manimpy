'''
@Author       : Jin Yuhan
@Date         : 2020-04-07 16:49:38
@LastEditors  : Jin Yuhan
@LastEditTime : 2020-05-08 12:08:54
@Description  : 提供对资源的查找
'''
import sys
from os import path


def get_asset_path_in_module(relative_path: str, module=None) -> str:
    """
    获取指定模块内资源的绝对路径
    :param relative_path: 资源对于指定模块的相对路径
    :param module: 资源所在的模块，如果值为None，则在调用者文件目录查找
    :return: 资源的绝对路径
    """
    file_name = module.__file__ if module else sys._getframe().f_back.f_code.co_filename
    return path.join(path.dirname(file_name), relative_path)

BILIBILI_GOOD_SVG: str = get_asset_path_in_module(r"assets\good.svg")
"""
bilibili点赞SVG路径，FROM MK
"""

BILIBILI_COIN_SVG: str = get_asset_path_in_module(r"assets\coin.svg")
"""
bilibili投币SVG路径，FROM MK
"""

BILIBILI_FAVO_SVG: str = get_asset_path_in_module(r"assets\favo.svg")
"""
bilibili收藏SVG路径，FROM MK
"""
