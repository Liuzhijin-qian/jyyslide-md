import os
import chardet

from src.settings import *


def get_file_code(file_path):  # 检测文件编码格式, 效率较低
    res = str()
    with open(file_path, "rb") as f:
        res = chardet.detect(f.read())["encoding"]
    return res


def read(filepath):  # 读取文本文件内容
    if os.path.exists(filepath):
        with open(filepath, "r", encoding=get_file_code(filepath)) as f:
            content = f.read()
            return content
    else:
        print("now in {}".format(os.getcwd()))
        print("the path {} is not exists".format(filepath))
        exit(-1)


def write(filepath, data):  # 向文件(覆)写入内容
    with open(filepath, "w", encoding="UTF-8") as f:
        f.write(data)