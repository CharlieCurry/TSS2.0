# -- coding: utf-8 --
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
c = []
d = []
PS = []
best = []
src = 'sourceCodeOut.txt'
f = open(src)
data = f.read()
#print(data)
f.close()
b = data.split(' ')
#print("lenb1:",len(b))
for i in range(len(b)):
    b[i] = b[i].split()
#print(b)
b = np.array(b[:]).reshape((-1, 7))
#for i in range(b.shape[0]):
 #   for j in range(7):
  #      b[i][j] = float(b[i][j])
dataframe = pd.DataFrame(b[:][:],columns=['size1','size2','size3','I','J','K','time'],dtype='float')
#print(dataframe)
#print(dataframe.describe())
df_group = dataframe[['size1','I','time']].groupby(by='size1',as_index=False).min()
#print(df_group)
size = dataframe['size1'].as_matrix()
#print(size)
time = dataframe['time'].as_matrix()

tilesize = dataframe['I'].as_matrix()



c1 = []#best tile list
d1 = []#min time for each PS
PS1 = []#PS
best1 = []
src = 'sourceCodeOutb.txt'
f1 = open(src)
data1 = f1.read()
#print(data)
f1.close()
b1 = data1.split(' ')
#print("lenb1:",len(b1))
for i in range(len(b1)):
    b1[i] = b1[i].split()
print(b)
b1 = np.array(b1[:]).reshape((-1, 4))
#for i in range(b.shape[0]):
 #   for j in range(7):
  #      b[i][j] = float(b[i][j])
dataframe1 = pd.DataFrame(b1[:][:],columns=['size1','size2','size3','time'],dtype='float')
# print(dataframe1)
# print(dataframe1.describe())

#df_group = dataframe[['size1','I','J','K','time']].sort_values(by="size1", ascending=True)
#df_group = dataframe[['size1','time']].groupby(by='size1',as_index=False).mean()
#print(df_group)
#dataframe1 = dataframe[['J','time']]
size1 = dataframe1['size1'].as_matrix()
time1 = dataframe1['time'].as_matrix()




import matplotlib.pyplot as plt
fig = plt.figure()
ax = plt.subplot()
plt.xlabel('Problem Size',size='16')
plt.ylabel('Execution Time',size='16')
for i,value in enumerate(size):
    l1=ax.scatter(size[i],time[i],c='black',marker='+')
for i,value in enumerate(size1):
    l2=ax.scatter(size1[i],time1[i],c='black',marker='o')
#plt.xlim((0,850))
#plt.ylim((0,0.5))
plt.legend(handles=[l1,l2],labels=['Tiled','Untile'],loc='upper left')  #设置图例中显示的内容

plt.show()
