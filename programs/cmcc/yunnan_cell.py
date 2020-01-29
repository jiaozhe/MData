import os
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt

# Read Data from File
data_dir = os.path.dirname(__file__)
data_file = os.path.join(data_dir, 'data', 'yunnan_cell.txt')

data = []
with open(data_file) as fo:
    for line in fo:
        line = line.strip()
        row_data = line.split()
        # remove abnormal data
        if len(row_data) == 2 and float(row_data[0]) > 90 and float(row_data[1]) < 40:
                data.append(row_data)

# Put Data into NumPy ndarray object
data_array = np.array(data)
longitude = data_array[:, 0].astype(np.float64)
latitude = data_array[:, 1].astype(np.float64)

# 解决保存图像是负号'-'显示为方块的问题
mpl.rcParams['axes.unicode_minus'] = False
# 指定默认字体
mpl.rcParams['font.sans-serif'] = ['SimHei']

plt.plot(longitude, latitude, '.')
plt.title('云南移动基站位置信息图')
plt.xlabel('经度')
plt.ylabel('维度')
plt.show()
