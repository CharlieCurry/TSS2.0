import numpy as np
import matplotlib.pyplot as mp
src = 'dsyrk'
mp.rcParams['font.sans-serif'] = ['SimHei']
mp.figure(figsize=(8, 6))
data = np.loadtxt('(Parallel1)valiation_prediction'+src+'.csv', delimiter=",")

print(data.shape)
x= np.arange(8,513,8)
print(x.shape)
# print(x)
y1 = data[:,27]
print(y1.shape)
# print(y1)
y2 = data[:,28]
print(y2.shape)

# print(y2)
import matplotlib.pyplot as plt

ax = plt.subplot()
plt.axhline(0.3197557 , color='red', linestyle='--')
plt.axvline(232, color='black', linestyle='--')
plt.axvline(240, color='green', linestyle='--')
plt.ylabel('Execution Time',fontsize=18)
plt.xlabel('Tile Size',fontsize=18)

mp.tick_params(labelsize=18)
# l1=ax.scatter(x[0:63],y1[0:63],color='black',marker='d')
# ax.plot(x[0:63],y1[0:63],color='black')

#
#l2=ax.scatter(x[0:63],y1[64:127],color='black',marker='+')
#ax.plot(x[0:63],y1[64:127],color='black')
#
l3=ax.scatter(x[0:63],y1[384:447],color='black',marker='o')
ax.plot(x[0:63],y1[384:447],color='black')

#l4=ax.scatter(x[0:63],y1[448:511],color='black',marker='^')
#ax.plot(x[0:63],y1[448:511],color='black')
color = []
print(x[7])
for i in range(63):
    if (x[i]==56)|((x[i]<=272)&(x[i]>=240)):
        color.append("red")
    else:
        color.append("green")

    #ax.scatter(x,y2,color='blue')
    #plt.plot(x,y1,color='red')
print(color)
plt.plot(x[0:63],y2[384:447],color='green')
l4=ax.scatter(x[0:63],y2[384:447],color=color,marker='^')
#plt.plot(x[0:63],y2[448:511],color='blue')
# plt.plot(x[128:191],y2[128:191],color='blue')
# plt.plot(x[192:255],y2[192:255],color='blue')
plt.legend(handles=[l3,l4],labels=['real time','predicted time'],loc='upper left',fontsize=18)

plt.title("Dsyrk",size=18)
plt.show()
y2[384:447].sort()
y_ = y2[384:447]
print(y_[0:6])
