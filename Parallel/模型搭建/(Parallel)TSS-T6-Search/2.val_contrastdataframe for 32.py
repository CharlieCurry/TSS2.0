# -- coding: utf-8 --
from __future__ import print_function
import numpy as np
import pandas as pd
#读入训练集和测试集的原始数据


#读入测试集的原始数据
src = 'trmm'
data = np.loadtxt('test/'+src+'_test_totalfeatures_32.txt')
print(data.shape)
#data[:,6:7] = (data[:,6:7].astype('float')-labelmin)/(labelmax-labelmin)
data_dataframe = pd.DataFrame(data,columns=['size1','size2','size3','I','j-0','j-i','k-0','k-i','k-j','L3_RP','L3_RNP','L3_RI','L3_WP','L3_WNP','L3WI','L2_RP','L2_RNP','L2_RI','L2_WP','L2_WNP','L2WI','L1_RP','L1_RNP','L1_RI','L1_WP','L1_WNP','L1WI','real_time'],dtype='float')


#读入网络对验证集的预测数据
with open('prediction/txt/test_prediction'+src+'.txt',"r") as f:
    str=f.read()
b = str.split(' ')
for i in range(len(b)):
    b[i] = b[i].split()
prediction_label=np.array(b[:]).reshape((-1,1))
prediction_label =prediction_label.astype('float')

print(prediction_label.shape)
#插入预测结果
data_dataframe.insert(28,'predict_time',prediction_label)
data_dataframe['predict_time'] = prediction_label
print(data_dataframe)
#将dataframe的所有内容保存到csv文件中
data_dataframe.to_csv('prediction/test_prediction'+src+'_32.csv',index=False)


