import numpy as np
src = "matmul"
with open('baseline/sourceCodeOutb.txt',"r") as f:
    str = f.read()
b = str.split(' ')
for i in range(len(b)):
    b[i] = b[i].split()
b=np.array(b[:]).reshape((-1,4))
print(b.shape)
baseline = []
for i in range(len(b)):
    #print(len(b))
    bs = np.tile(b[i:i+1,3:4],(6,1))
    #print(bs)
    baseline = np.append(baseline,bs).astype('float')

print(baseline)
print(baseline.shape)
baseline=baseline.reshape((600,1))
print(baseline.shape)

print(baseline)
np.savetxt('baseline/baselineO2_'+src+'.txt',baseline,fmt="%2.10f")
