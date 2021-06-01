import numpy as np

tss1 = np.array([0.6668,0.7309,0.8574,0.2640,0.9828,0.6999,0.7003])
tss10 = np.array([0.6336,0.7060,0.8259,0.5523,0.9794,0.7282,0.7375])
tsslc = np.array([0.8680,0.8943,0.9416,0.8469,0.9934,0.8873,0.90525])
pluto = np.array([0.6957,0.7658,0.7515,0.7596,0.9796,0.8329,0.7975])



import numpy as np
import matplotlib.pyplot as mp

# 设置中文字体
mp.rcParams['font.sans-serif'] = ['SimHei']
# mp.rcParams['axes.unicode_minus'] = False


ptss = np.array([0.6957,0.7658,0.7515, 0.7456381,0.9796,0.8329,0.7955197])
gtss = np.array([0.8680,0.8943,0.9416,0.9289145,0.9934,0.8873,0.916966])
#mp.figure('Bar Chart', facecolor='lightgray')
#mp.title('Bar Chart', fontsize=16)
mp.xlabel('Models', fontsize=18)
mp.ylabel('Maximum Available Performance', fontsize=18)
mp.tick_params(labelsize=16)
mp.grid(linestyle=':', axis='y')
x = np.arange(7)
a = mp.bar(x - 0.2, ptss, 0.3, color='orange', label='Pluto', align='center',hatch = '-')
b = mp.bar(x + 0.2, gtss, 0.3, color='green', label='TSSP-T6-Search', align='center',hatch = '/')
# 设置标签
for i in a + b:
    h = i.get_height()
    mp.text(i.get_x() + i.get_width() / 2, h, '%2.3f' % (h), ha='center', va='bottom',size='12')
mp.xticks(x, ['Gemm', 'Dsyrk', 'Dsyr2k', 'Tmm', 'Trmm', 'Matmul','AVG'])
mp.ylim(0.6,1.1)
mp.legend(loc='upper left',fontsize=12)
mp.show()