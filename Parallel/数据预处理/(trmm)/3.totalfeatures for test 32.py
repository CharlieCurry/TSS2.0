import numpy as np

with open('data_8/sourceCodeOut(32000).txt',"r") as f:
    str = f.read()
b = str.split(' ')
for i in range(len(b)):
    b[i] = b[i].split()
b=np.array(b[:]).reshape((-1,7))
print(b.shape)

datamax  = b[:,0:3].astype('float').max(axis=0)
datamin  = b[:,0:3].astype('float').min(axis=0)

labelmax  = b[:,6:7].astype('float').max(axis=0)
labelmin  = b[:,6:7].astype('float').min(axis=0)
print("min:",labelmin)
print("max:",labelmax)
#序列化的读取方式
src = 'trmm'
with open('test/test_'+src+'.txt',"r") as f:
     str = f.read()
b = str.split(' ')
for i in range(len(b)):
     b[i] = b[i].split()
b=np.array(b[:]).reshape((-1,7))
#去重之后

print(b.shape)
b = b.astype('float')
b[:,0:3] = ((b[:,0:3]-datamin)/(datamax-datamin)).astype('float')
b[:,6:7] = ((b[:,6:7]-labelmin)/(labelmax-labelmin)).astype('float')

tmm_features = np.loadtxt('features/'+src+'_test_features.txt')
print(tmm_features.shape)

c = np.append(b[:,0:4],tmm_features,axis=1).astype('float')
print(c.shape)

d = np.append(c,b[:,6:7],axis=1).astype('float')
print(d.shape)
print(d[:2,:])
print("save")
np.savetxt('totalfeatures/'+src+'_test_totalfeatures_32.txt',d,fmt="%2.10f")
