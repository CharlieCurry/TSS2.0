import numpy as np
src = 'dsyrk'
features = [1,0,0,0,1,2,0,1,1,0,0,1,1,1,0,1,0,0,2,1,0,0,1]
features = np.tile(features,(6400,1))
print(features)
print(features.shape)
np.savetxt('features/'+src+'_test_features.txt',features,fmt="%1.1f")
data = np.loadtxt('features/'+src+'_test_features.txt')
print(data)
print(data.shape)
e=np.append(features,data,axis=1)
print(e.shape)

