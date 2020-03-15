from loguru import logger
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


df = pd.read_excel("sample_results.xlsx", sheet_name="Sheet1", parse_dates=["统计日期"])
df["宽带预约量"].fillna(0, inplace=True)
df["外呼接通成功量"].fillna(0, inplace=True)
df["业务办理成功量"].fillna(0, inplace=True)
gb = df.groupby("统计日期").sum()
gb.drop(columns=["序号"], inplace=True)
gb["外呼成功率"] = gb["外呼接通成功量"] / gb["宽带预约量"]
gb["办理成功率"] = gb["业务办理成功量"] / gb["宽带预约量"]

logger.info(gb)
