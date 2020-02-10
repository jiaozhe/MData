#!/usr/bin/env python
import os
from pathlib import Path
from loguru import logger
import pandas as pd


# 初始配置信息
DATA_EXTS = [".xls", ".xlsx"]
DATA_PATH = Path("C:/Users/John/Desktop/集运商机/预约单/0208")

# 切换工作目录
os.chdir(DATA_PATH)
if Path.cwd() != DATA_PATH:
    logger.error("[Change Working Directory] Error!")
else:
    logger.info("[Change Working Directory] Success!")

# 遍历处理数据文件
for excel in DATA_PATH.iterdir():
    if excel.is_file() and excel.suffix in DATA_EXTS:
        excel_name = excel.name
        df = pd.read_excel(excel)
        data_pid = df["身份证"].values
        data_records = len(set(data_pid))
        logger.info("%s ==> %s" % (excel_name, data_records))
