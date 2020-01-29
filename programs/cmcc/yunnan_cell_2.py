import os
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Pandas
# Read Data from File
data_dir = os.path.join(os.path.dirname(__file__), 'data')
data_file = os.path.join(data_dir, 'yunnan_cell.txt')

# Pandas
df = pd.read_table(data_file, header=None, names=['Longitude', 'Latitude'], skip_blank_lines=True)
df.drop_duplicates(inplace=True)
df.replace(to_replace=df[df.Longitude < 90], value=np.nan, inplace=True)
df.dropna(inplace=True)

# Matplotlib Plotting
plt.scatter(df['Longitude'], df['Latitude'], s=1, c='b', marker='.')
plt.title('云南移动基站位置信息图')
plt.xlabel('经度')
plt.ylabel('维度')
plt.show()
