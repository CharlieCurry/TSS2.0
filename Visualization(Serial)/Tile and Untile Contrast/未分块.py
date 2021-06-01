# -- coding: utf-8 --
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# 针对给定的PS,可视化x:tile size,y:time
c = []  # best tile list
d = []  # min time for each PS
PS = []  # PS
best = []
src = 'sourceCodeOutb.txt'
f = open(src)
data = f.read()
# print(data)
f.close()
b = data.split(' ')
for i in range(len(b)):
    b[i] = b[i].split()
# print(b)
b = np.array(b[:]).reshape((-1, 4))
#for i in range(b.shape[0]):
#   for j in range(7):
#      b[i][j] = float(b[i][j])
dataframe = pd.DataFrame(b[:][:], columns=['size1', 'size2', 'size3', 'time'], dtype='float')
#print(dataframe)
#print(dataframe.describe())

# df_group = dataframe[['size1','I','J','K','time']].sort_values(by="size1", ascending=True)
# df_group = dataframe[['size1','time']].groupby(by='size1',as_index=False).mean()
# print(df_group)
# dataframe1 = dataframe[['J','time']]
size = dataframe['size1'].as_matrix()
#print(size)
time = dataframe['time'].as_matrix()
#print(time)
import matplotlib.pyplot as plt
fig = plt.figure()
ax = plt.subplot()
plt.xlabel('Problem Size',size='16')
plt.ylabel('Execution Time',size='16')
for i, value in enumerate(size):
    l1 = ax.scatter(size[i], time[i], c='black')
plt.legend(handles=[l1],labels=['Untile'],loc='upper left')  #设置图例中显示的内容
# plt.xlim((0,850))
# plt.ylim((0,0.5))
plt.show()
