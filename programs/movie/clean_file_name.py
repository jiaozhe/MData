#!/usr/bin/env python
import os
from loguru import logger


MOVIE_DIR = "E:/Downloads/Movie"
os.chdir(MOVIE_DIR)

MOVIE_EXTS = [".rmvb", ".mp4", ".mkv"]

dirty_strings = ""

movies = os.listdir(MOVIE_DIR)

for movie in movies:
    file_name, file_ext = os.path.splitext(movie)
    if os.path.isfile(file_name) and file_ext in MOVIE_EXTS:
        if file_name.startswith("[阳光电影"):
            tmp_name = file_name[19:]
            if tmp_name.startswith("."):
                tmp_name = tmp_name[1:]
            else:
                pass
            old_movie_name = file_name
            new_movie_name = tmp_name.split(".")[0]
            # Output
            try:
                os.rename(old_movie_name, new_movie_name)
            except Exception as e:
                logger.critical(e.message)
            else:
                logger.debug("{old_name} ==> {new_name}",
                             old_name=old_movie_name, new_name=new_movie_name)
