import numpy as np
import pandas as pd
#在加载csv文件之前，先手动把表头给去掉
# src = '_data_32'
#
# val_pre_data = np.loadtxt('prediction/valiation_prediction'+src+'.csv', delimiter=",")
src = 'trmm'

val_pre_data = np.loadtxt('prediction/valiation_prediction_32'+src+'.csv', delimiter=",")

#tmp现在是128*8的矩阵
print(val_pre_data.shape)
print(val_pre_data.shape[0])
rows = val_pre_data.shape[0]
kinds = rows/64
print("rows:",rows)
print("kinds:",kinds)
predict_best = pd.DataFrame(columns=['predict_time','size1','size2','size3','I','j-0','j-i','k-0','k-i','k-j','L3_RP','L3_RNP','L3_RI','L3_WP','L3_WNP','L3WI','L2_RP','L2_RNP','L2_RI','L2_WP','L2_WNP','L2WI','L1_RP','L1_RNP','L1_RI','L1_WP','L1_WNP','L1WI','real_time'],dtype='float')
real_best = pd.DataFrame(columns=['predict_time','size1','size2','size3','I','j-0','j-i','k-0','k-i','k-j','L3_RP','L3_RNP','L3_RI','L3_WP','L3_WNP','L3WI','L2_RP','L2_RNP','L2_RI','L2_WP','L2_WNP','L2WI','L1_RP','L1_RNP','L1_RI','L1_WP','L1_WNP','L1WI','real_time'],dtype='float')
base_32 = pd.DataFrame(columns=['I','real_time'],dtype='float')
#print(best)
for i in range(int(kinds)):
    #print(i)
    start=i*64
    end= i*64+64
    kind1 = val_pre_data[start:end][:].astype('float')

    kind1_dataframe = pd.DataFrame(kind1,columns=['size1','size2','size3','I','j-0','j-i','k-0','k-i','k-j','L3_RP','L3_RNP','L3_RI','L3_WP','L3_WNP','L3WI','L2_RP','L2_RNP','L2_RI','L2_WP','L2_WNP','L2WI','L1_RP','L1_RNP','L1_RI','L1_WP','L1_WNP','L1WI','real_time','predict_time'],dtype='float')
    df_group = kind1_dataframe.groupby('predict_time',as_index=False,sort=True).min()

    df_group_sort = kind1_dataframe.sort_values(by='real_time',ascending=True)
    base_32 = base_32.astype('float')
    base_32 = base_32.append(kind1_dataframe[kind1_dataframe['I']==32],ignore_index=True)
    base_32 = base_32.append(kind1_dataframe[kind1_dataframe['I'] == 32], ignore_index=True)
    base_32 = base_32.append(kind1_dataframe[kind1_dataframe['I'] == 32], ignore_index=True)
    base_32 = base_32.append(kind1_dataframe[kind1_dataframe['I'] == 32], ignore_index=True)
    base_32 = base_32.append(kind1_dataframe[kind1_dataframe['I']==32],ignore_index=True)
    base_32 = base_32.append(kind1_dataframe[kind1_dataframe['I'] == 32], ignore_index=True)
    predict_best = predict_best.append(df_group[0:6],ignore_index=True)
    real_best = real_best.append(df_group_sort[0:1],ignore_index=True)
print("base32",base_32[['I','real_time']])

oracle = pd.DataFrame(columns=['predict_time','size1','size2','size3','I','j-0','j-i','k-0','k-i','k-j','L3_RP','L3_RNP','L3_RI','L3_WP','L3_WNP','L3WI','L2_RP','L2_RNP','L2_RI','L2_WP','L2_WNP','L2WI','L1_RP','L1_RNP','L1_RI','L1_WP','L1_WNP','L1WI','real_time'],dtype='float')
for i in range(len(real_best)):
    a = real_best.loc[i]
    d = pd.DataFrame(a).T
    oracle = oracle.append([d]*6)
#print(oracle)
print("oralce shape",oracle.shape)
oracle = oracle.reset_index(drop=True)

base_o2 = np.loadtxt('baseline/baselineO2_'+src+'.txt')
print("base shape:",base_o2.shape)

big_dataframe=pd.concat([predict_best[['real_time','I','predict_time','size1','size2','size3']],oracle[['real_time','I']]],axis=1)
big_dataframe.columns = ['T_p32','I_32','predict_time1','size1','size2','size3','To','I_o']
#print(big_dataframe)
#columns=['T','T1(predict_real_time)','To(oralce_real_time)']
P = pd.DataFrame(dtype='float')
#T_32Pluto默认的32分块
P.insert(0,'T_32',base_32['real_time'])
#T_o2未分块
P.insert(1,'T',base_o2)

P.insert(2,'T_p32',big_dataframe['T_p32'])

P.insert(3,'To',big_dataframe['To'])
#dsyr2k
#labelmax = 6.9250307
#labelmin = 0.1244027
#dsyrk
#labelmax = 1.3129827
#labelmin = 0.0831317
#tmm
#labelmax = 2.3524685
#labelmin = 0.0651701
#trmm
labelmax = 1.9884247
labelmin = 0.0472126
#gemm
##labelmax = 1.9300515
#abelmin = 0.0953698
#matmul
#labelmax = 2.3311794
#labelmin = 0.1018574
P=P.dropna(axis=0,how='any')
P['T_32'] = P['T_32']*(labelmax-labelmin)+labelmin
#P['T'] = P['T']*(labelmax-labelmin)+labelmin
P['To'] = P['To']*(labelmax-labelmin)+labelmin
#P = P.loc[(P['T']>P['To'])]
#P = P.loc[(P['T']>=P['T_32'])&(P['T_32']>=P['To'])]
print("P",P)
print(P.describe())



P['p_32']=(P['T']-P['T_32'])/(P['T']-P['To'])
P['speedup=T/T_32'] = P['T']/P['T_32']
P['T_32/T_O'] = P['T_32']/P['To']
P['So'] = P['T']/P['To']
print("--------------------------------")
#print("p_32:",P['p_32'].mean())
S32_mean =P['speedup=T/T_32'].mean()
So_mean = P['So'].mean()

print("speedup=T/T_32:",S32_mean)
print("So_mean",So_mean)
print("T_32/T_O:",P['T_32/T_O'].mean())
print("--------------------------------")
print("P:",(1-1/S32_mean)/(1-1/So_mean))