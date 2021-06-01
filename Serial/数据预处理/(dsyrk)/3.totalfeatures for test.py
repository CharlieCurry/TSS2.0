import numpy as np

with open('data_8/sourceCodeOut(32000).txt',"r") as f:
    str = f.read()
b = str.split(' ')
for i in range(len(b)):
    b[i] = b[i].split()
b=np.array(b[:]).reshape((-1,7))
print(b.shape)

datamax  = b[:,0:4].astype('float').max(axis=0)
datamin  = b[:,0:4].astype('float').min(axis=0)

labelmax  = b[:,6:7].astype('float').max(axis=0)
labelmin  = b[:,6:7].astype('float').min(axis=0)
print("min:",labelmin)
print("max:",labelmax)

#去重之后
src = "dsyrk"
b = np.loadtxt('test/test_'+src+'.txt')
print(b.shape)
b = b.astype('float')
b[:,0:4] = ((b[:,0:4]-datamin)/(datamax-datamin)).astype('float')
b[:,6:7] = ((b[:,6:7]-labelmin)/(labelmax-labelmin)).astype('float')

tmm_features = np.loadtxt('features/'+src+'_test_features.txt')
print(tmm_features.shape)

c = np.append(b[:,0:4],tmm_features,axis=1).astype('float')
print(c.shape)

d = np.append(c,b[:,6:7],axis=1).astype('float')
print(d.shape)
print(d[:2,:])
print("save")
np.savetxt('totalfeatures/'+src+'_test_totalfeatures.txt',d,fmt="%2.10f")
