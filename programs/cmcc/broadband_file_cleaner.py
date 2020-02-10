#!/usr/bin/env python
import os
import shutil
from pathlib import Path
from loguru import logger
from openpyxl import load_workbook


# 初始配置信息
DATA_EXTS = [".xls", ".xlsx"]
DATA_DATE = "0210"
DATA_PATH = Path("C:/Users/John/Desktop/集运商机/预约单/" + DATA_DATE)
PROV_NAMES = ["安徽", "北京", "重庆", "福建", "甘肃", "广东", "广西",
              "贵州", "海南", "河北", "河南", "黑龙江", "湖北", "湖南",
              "吉林", "江苏", "江西", "辽宁", "内蒙古", "宁夏", "青海",
              "山东", "山西", "陕西", "上海", "四川", "天津", "西藏",
              "新疆", "云南", "浙江"]
PROV_INFO = dict()
for index, item in enumerate(PROV_NAMES):
    # logger.info("%02d - %s" % (index, item))
    PROV_INFO[item] = "%02d" % (index+1, )


# 切换工作目录
os.chdir(DATA_PATH)
if Path.cwd() != DATA_PATH:
    logger.error("[Change Working Directory] Error!")
else:
    logger.info("[Change Working Directory] Success!")


# 函数
def change_name(_old_name, _suffix):
    for _prov_name in PROV_INFO:
        if _prov_name in _old_name:
            _prov_number = PROV_INFO[_prov_name]
            _new_name = "%s-%s-%s" % (_prov_number, _prov_name, DATA_DATE)
            return _new_name + _suffix
        else:
            continue


# 遍历处理数据文件
for excel in DATA_PATH.iterdir():
    if excel.is_file() and excel.suffix in DATA_EXTS:
        # 解析 Excel 文件名
        excel_old_name = excel.name
        excel_suffix = excel.suffix
        excel_new_name = change_name(excel_old_name, excel_suffix)
        logger.info("%s ==> %s" % (excel_old_name, excel_new_name))
        # shutil.move(excel_old_name, excel_new_name)
        # 删除 Excel 文件中的无用数据列
        wb = load_workbook(excel_old_name)
        ws = wb.active
        ws.delete_cols(1, 4)
        ws.delete_cols(2)
        ws.delete_cols(3)
        ws.delete_cols(4, 4)
        wb.save(excel_new_name)
