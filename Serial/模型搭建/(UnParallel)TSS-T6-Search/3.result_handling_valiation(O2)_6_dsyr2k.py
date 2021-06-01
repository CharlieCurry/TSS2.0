import numpy as np
import pandas as pd
#在加载csv文件之前，先手动把表头给去掉
src = 'dsyr2k'

val_pre_data = np.loadtxt('prediction/valiation_prediction'+src+'.csv', delimiter=",")
print(val_pre_data.shape)
print(val_pre_data.shape[0])
rows = val_pre_data.shape[0]
kinds = rows/64
print("rows:",rows)
print("kinds:",kinds)
predict_best = pd.DataFrame(columns=['predict_time','size1','size2','size3','I','j-0','j-i','k-0','k-i','k-j','L3_RP','L3_RNP','L3_RI','L3_WP','L3_WNP','L3WI','L2_RP','L2_RNP','L2_RI','L2_WP','L2_WNP','L2WI','L1_RP','L1_RNP','L1_RI','L1_WP','L1_WNP','L1WI','real_time'],dtype='float')
real_best = pd.DataFrame(columns=['predict_time','size1','size2','size3','I','j-0','j-i','k-0','k-i','k-j','L3_RP','L3_RNP','L3_RI','L3_WP','L3_WNP','L3WI','L2_RP','L2_RNP','L2_RI','L2_WP','L2_WNP','L2WI','L1_RP','L1_RNP','L1_RI','L1_WP','L1_WNP','L1WI','real_time'],dtype='float')
base = pd.DataFrame(columns=['I','real_time'],dtype='float')

for i in range(int(kinds)):
    start=i*64
    end= i*64+64
    kind1 = val_pre_data[start:end][:]
    kind1_dataframe = pd.DataFrame(kind1,columns=['size1','size2','size3','I','j-0','j-i','k-0','k-i','k-j','L3_RP','L3_RNP','L3_RI','L3_WP','L3_WNP','L3WI','L2_RP','L2_RNP','L2_RI','L2_WP','L2_WNP','L2WI','L1_RP','L1_RNP','L1_RI','L1_WP','L1_WNP','L1WI','real_time','predict_time'],dtype='float')
    df_group = kind1_dataframe.groupby('predict_time',as_index=False).min()
    df_group_sort = kind1_dataframe.sort_values(by='real_time',ascending=True)
    predict_best = predict_best.append(df_group[0:6],ignore_index=True)
    real_best = real_best.append(df_group_sort[0:1],ignore_index=True)
print(predict_best.shape)
print(real_best.shape)


oracle = pd.DataFrame(columns=['predict_time','size1','size2','size3','I','j-0','j-i','k-0','k-i','k-j','L3_RP','L3_RNP','L3_RI','L3_WP','L3_WNP','L3WI','L2_RP','L2_RNP','L2_RI','L2_WP','L2_WNP','L2WI','L1_RP','L1_RNP','L1_RI','L1_WP','L1_WNP','L1WI','real_time'],dtype='float')
for i in range(len(real_best)):
    a = real_best.loc[i]
    d = pd.DataFrame(a).T
    oracle = oracle.append([d]*6)
#print(oracle)
print("oralce shape",oracle.shape)
oracle = oracle.reset_index(drop=True)


base = np.loadtxt('baseline/baselineO2_'+src+'.txt')
print("base shape:",base.shape)

big_dataframe=pd.concat([predict_best[['real_time','I','predict_time','size1','size2','size3']],oracle[['real_time','I']]],axis=1).astype('float')
big_dataframe.columns = ['T1','I1','predict_time1','size1','size2','size3','To','I2']
print(big_dataframe)
P = pd.DataFrame(dtype='float')
P.insert(0,'T',base)
P.insert(1,'T1',big_dataframe['T1'])
P.insert(2,'To',big_dataframe['To'])

print(P)


P = P.astype('float')
print("+++++++++++++++++++++++")
print(P.ix[(P==0).any(axis=1), :] )
#P = P.ix[~(P==0).any(axis=1), :]
print("+++++++++++++++++++++++")
#dsyr2k
labelmax = 9.765625
labelmin = 0.421875

P=P.dropna(axis=0,how='any')

P['To'] = P['To']*(labelmax-labelmin)+labelmin
P['T1'] = P['T1']*(labelmax-labelmin)+labelmin
#P['T'] = P['T']*(labelmax-labelmin)+labelmin
#P = P.loc[(P['T']>P['To'])]
print(P)
#P = P.loc[(P['T']>P['To'])&(P['T']>=P['T1'])]
P['p']=(P['T']-P['T1'])/(P['T']-P['To'])
P['speedup=T/T1'] = P['T']/P['T1']
P['normalization_time'] = P['T1']/P['To']
P['So'] = P['T']/P['To']

print(P)
print(P.describe())

result = pd.DataFrame(columns=['T','T1','To','p','speedup=T/T1','normalization_time','So'],dtype='float')
for i in range(len(P)):
    cut = P.iloc[i*6:(i+1)*6, :]
    cut_sort = cut.groupby('T1',as_index=False).min()
    #print(cut_sort)
    result = result.append(cut_sort[0:1],ignore_index=True)
print(result)
print(result.shape)
print("*****************************")
speedup_mean = result['speedup=T/T1'].mean()
So_mean = result['So'].mean()
print("speedup:",speedup_mean)
print("So_mean",So_mean)
print("normalization_time:",result['normalization_time'].mean())
print("P:",(1-1/speedup_mean)/(1-1/So_mean))
print("*****************************")