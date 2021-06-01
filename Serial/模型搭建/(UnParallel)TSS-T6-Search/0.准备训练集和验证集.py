import numpy as np
tmm_data = np.loadtxt('totalfeatures/tmmtotalfeatures.txt')
matmul_data = np.loadtxt('totalfeatures/matmultotalfeatures.txt')
dsyr2k_data = np.loadtxt('totalfeatures/dsyr2ktotalfeatures.txt')
dsyrk_data = np.loadtxt('totalfeatures/dsyrktotalfeatures.txt')
gemm_data = np.loadtxt('totalfeatures/gemmtotalfeatures.txt')
trmm_data = np.loadtxt('totalfeatures/trmmtotalfeatures.txt')

tmm_data = tmm_data.astype('float')
matmul_data = matmul_data.astype('float')
trmm_data = trmm_data.astype('float')
gemm_data = gemm_data.astype('float')
dsyr2k_data = dsyr2k_data.astype('float')
dsyrk_data = dsyrk_data.astype('float')



index = np.arange(32000)
np.random.shuffle(index)

tmm_data = tmm_data[index]
matmul_data = matmul_data[index]
trmm_data = trmm_data[index]
dsyr2k_data = dsyr2k_data[index]
dsyrk_data = dsyrk_data[index]
gemm_data = gemm_data[index]

train_tmm = tmm_data[:28800,:]
test_tmm = tmm_data[28800:,:]

train_matmul = matmul_data[:28800,:]
test_matmul = matmul_data[28800:,:]

train_trmm = trmm_data[:28800,:]
test_trmm = trmm_data[28800:,:]

train_gemm = gemm_data[:28800,:]
test_gemm = gemm_data[28800:,:]

train_dsyr2k = dsyr2k_data[:28800,:]
test_dsyr2k = dsyr2k_data[28800:,:]

train_dsyrk = dsyrk_data[:28800,:]
test_dsyrk = dsyrk_data[28800:,:]


print(train_tmm.shape)
print(test_tmm.shape)
print(train_matmul.shape)
print(test_matmul.shape)

train_data = np.append(train_matmul,train_tmm,axis=0)
train_data = np.append(train_data,train_trmm,axis=0)
train_data = np.append(train_data,train_gemm,axis=0)
train_data = np.append(train_data,train_dsyrk,axis=0)
train_data = np.append(train_data,train_dsyr2k,axis=0)


test_data = np.append(test_matmul,test_tmm,axis=0)
test_data = np.append(test_data,test_trmm,axis=0)
test_data = np.append(test_data,test_gemm,axis=0)
test_data = np.append(test_data,test_dsyrk,axis=0)
test_data = np.append(test_data,test_dsyr2k,axis=0)

print("train data shape",train_data.shape)
print("valiation data shape",test_data.shape)

index = np.arange(len(train_data))
np.random.shuffle(index)
train_data = train_data[index]
np.savetxt('train/train_data.txt',train_data,fmt="%2.10f")

index = np.arange(len(test_data))
np.random.shuffle(index)
test_data = test_data[index]
np.savetxt('valiation/valiation_data.txt',test_data,fmt="%2.10f")
