import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

with open('valiation(trmm100cube).txt',"r") as f:
    str = f.read()
data = str.split(' ')
for i in range(len(data)):
    data[i] = data[i].split()
data=np.array(data[:]).reshape((-1,7))
print(data.shape)

rows = data.shape[0]
kinds = rows/64
print("rows:",rows)
print("kinds:",kinds)



data = pd.DataFrame(data,columns=['size1','size2','size3','I','J','K','real_time',],dtype='float')
print(data.head())


real_best = pd.DataFrame(columns=['real_time','size1','size2','size3','I','J','K'],dtype='float')
real_worst = pd.DataFrame(columns=['real_time','size1','size2','size3','I','J','K'],dtype='float')

for i in range(int(kinds)):
    start=i*64
    end= i*64+64
    kind1 = data[start:end][:]
    kind1_dataframe = pd.DataFrame(kind1,columns=['real_time','size1','size2','size3','I','J','K'],dtype='float')
    df_group = kind1_dataframe.groupby('real_time',as_index=False).min()
    df_group_sort = kind1_dataframe.sort_values(by='real_time',ascending=True)
    # base = base.append(kind1_dataframe[kind1_dataframe['I']==32],ignore_index=True)
    # base = base.append(kind1_dataframe[kind1_dataframe['I'] == 32], ignore_index=True)
    # base = base.append(kind1_dataframe[kind1_dataframe['I'] == 32], ignore_index=True)
    # base = base.append(kind1_dataframe[kind1_dataframe['I'] == 32], ignore_index=True)
    # base = base.append(kind1_dataframe[kind1_dataframe['I']==32],ignore_index=True)
    # base = base.append(kind1_dataframe[kind1_dataframe['I'] == 32], ignore_index=True)
    print(real_best.head())
    real_best = real_best.append(df_group_sort[0:6],ignore_index=True)

    #real_worst = real_worst.append(df_group_sort[63:],ignore_index=True)
    #print("real_best:",real_best.head())
    print(real_best['real_time'])
    real_best['real_time']=real_best['real_time'].astype('float')
print(real_best.describe())


print(real_best.shape)
#print(real_worst.shape)
print(real_best.head())
#print(real_worst.shape)
size1 = real_best['size1'].tolist()
#size2 =real_worst['size1'].tolist()
ts1 =real_best['I'].tolist()
#ts2 =real_worst['I'].tolist()


print(size1)
print(ts1)
fig = plt.figure()
plt.xlabel('Problem Size',size='16')
plt.ylabel('Optimal Tile Size',size='16')


plt.scatter(size1,ts1,c='0.1',marker='o')
#plt.scatter(size1,ts2,c='0.1',marker='o')
#plt.plot(size1,ts)
plt.show()

# 3D Plot

# col1 =[]
# #可以去查RGB
# for a in ts:
#     if a <= 128:
#         col1.append('y')
#     elif (a <= 256) & (a>128):
#         col1.append('g')
#     elif (a <= 384) & (a>256):
#         col1.append('r')
#     elif (a <= 512) & (a>384):
#         col1.append('b')
#     elif (a>512):
#         col1.append('black')
# fig1 = plt.figure()
# ax3D = fig1.add_subplot(111, projection='3d')
# threeD =ax3D.scatter(size1, size2, size3,c=col1,marker='o')
#
# #plt.legend(handles=[threeD],labels=['8-128','128-256','256-384','384-512'],loc='upper left')
# #plt.xlim((0,1000))
# plt.xlabel("size1")
# plt.ylabel("size")
# #plt.ylim((0,1000))
#
# plt.show()