import numpy as np
import matplotlib.pyplot as mp

# 设置中文字体
mp.rcParams['font.sans-serif'] = ['SimHei']
# mp.rcParams['axes.unicode_minus'] = False

fig=mp.gcf()
fig.set_size_inches(18,10)
ptss = np.array([1.1229,1.1323,1.2190,1.1369, 1.15413,1.11907,1.14738])
gtss = np.array([1.0379,1.0484,1.0810,1.05210,1.041619,1.031611,1.04877])
tss1 = np.array([1.035210,1.05316,1.07494,1.05326,1.04215,1.031683,1.0484005])


import numpy as np
import matplotlib.pyplot as mp

# 设置中文字体
#mp.rcParams['font.sans-serif'] = ['SimHei']
# mp.rcParams['axes.unicode_minus'] = False
fig=mp.gcf()
fig.set_size_inches(18,10)
tss1 = np.array([1.035210,1.05316,1.07494,1.05326,1.04215,1.031683,1.0484005])
tss10 = np.array([1.0379,1.0484,1.0810,1.05210,1.041619,1.031611,1.04877])
tsslc = np.array([1.02105,1.01756,1.03499,1.020284,1.012546,1.0176575,1.020681])
pluto = np.array([1.1229,1.1323,1.2190,1.1369, 1.15413,1.11907,1.14738])

# ptss = np.array([1.2790714219254447,1.2481219631319513,1.6439511256483947,1.343966418615594, 6.128879519183511,1.4644432399551648,2.1847389480766766])
# gtss = np.array([1.374065260408715,1.3716485037834816,1.96388009818339,1.3992445397509903, 6.605520762017123,1.5102665681152647,2.3707709553764937])
# #mp.figure('Bar Chart', facecolor='lightgray')
#mp.title('Bar Chart', fontsize=16)
mp.xlabel('Models', fontsize=24)
mp.ylabel('Nomalization Time', fontsize=24)
mp.tick_params(labelsize=22)
mp.grid(linestyle=':', axis='y')
x = np.arange(7)
a = mp.bar(x - 0.4, tss1, 0.1, color='dodgerblue', label='TSS-T1', align='center')
b = mp.bar(x - 0.2, tss10, 0.1, color='orangered', label='TSS-T6-Random', align='center',hatch = '/')
c = mp.bar(x - 0.0, tsslc, 0.1, color='green', label='TSS-T6-Search', align='center',hatch = '|')
d = mp.bar(x + 0.2, pluto, 0.1, color='orange', label='Pluto', align='center',hatch = '-')
#e = mp.bar(x + 0.3, So, 0.1, color='b', label='Oracle(Exhaustive Search)', align='center',hatch = '+')
# 设置标签
for i in a + b+c+d:
    h = i.get_height()
    mp.text(i.get_x() + i.get_width() / 2, h, '%2.3f' % (h), ha='center', va='bottom',size='13')
mp.xticks(x, ['Gemm', 'Dsyrk', 'Dsyr2k', 'Tmm', 'Trmm', 'Matmul','AVG'])
mp.ylim(1,1.25)
mp.legend(loc='upper left',fontsize=22)
mp.show()

