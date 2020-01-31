#!/usr/bin/env python
import os
import shutil
from pathlib import Path
from loguru import logger


# Function
def clean_name(old_name):
    # 删除文件名中的空白字符
    _tmp_name = old_name.strip()
    # 删除文件名中的网站标志
    _tmp_name = _tmp_name.replace("[阳光电影-www.ygdy8.com]", "")
    _tmp_name = _tmp_name.replace("[阳光电影-www.ygdy8.net]", "")
    # 删除文件名中的附加信息
    extra_info = ["", "HD", "BD", "720p", "中英双字幕", "国英双语", "国英双语中字", "国语中字", "粤语中字", "韩语中字", "日语中字"]
    extra_info_set = set(extra_info)
    _tmp_name_list = _tmp_name.split(".")
    _tmp_name_set = set(_tmp_name_list)
    _tmp_new_list = list(_tmp_name_set - extra_info_set)
    _tmp_new_list.sort(key=_tmp_name_list.index)
    _tmp_name = ".".join(_tmp_new_list)
    # 输出结果
    new_name = _tmp_name
    return new_name


# 初始配置信息
MOVIE_EXTS = [".rmvb", ".mp4", ".mkv"]
MOVIE_PATH = Path("C:/Downloads/唐人街探案")

# 切换工作目录
os.chdir(MOVIE_PATH)
if Path.cwd() != MOVIE_PATH:
    logger.error("[Change Working Directory] Error!")
else:
    logger.info("[Change Working Directory] Success!")

# 遍历处理电影文件
for movie in MOVIE_PATH.iterdir():
    if movie.is_file() and movie.suffix in MOVIE_EXTS:
        movie_name = movie.name
        movie_new_name = clean_name(movie.stem) + movie.suffix
        logger.info("%s ==> %s" % (movie_name, movie_new_name))
        shutil.move(movie_name, movie_new_name)
