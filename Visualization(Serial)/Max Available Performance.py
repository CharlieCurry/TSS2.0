import numpy as np
import matplotlib.pyplot as mp

# 设置中文字体
mp.rcParams['font.sans-serif'] = ['SimHei']
# mp.rcParams['axes.unicode_minus'] = False

pluto = np.array([0.97736,0.98702,0.963824,0.964126,0.9841094,0.805228,0.946944])
tss10 = np.array([0.992071,0.9955749,0.988627, 0.987734,0.995825,0.952406,0.985372])
tss1 = np.array([0.99237,0.995209,0.989463,0.987475,0.995740,0.95302,0.98554])

#mp.figure('Bar Chart', facecolor='lightgray')
#mp.title('Bar Chart', fontsize=16)
mp.xlabel('Models', fontsize=18)
mp.ylabel('Maximum Available Performance', fontsize=18)
mp.tick_params(labelsize=16)
mp.grid(linestyle=':', axis='y')
x = np.arange(7)
a = mp.bar(x - 0.2, pluto, 0.3, color='orange', label='Pluto', align='center',hatch = '-')
b = mp.bar(x + 0.2, tss10, 0.3, color='orangered', label='TSS-T6-Random', align='center',hatch = '/')
# 设置标签
for i in a + b:
    h = i.get_height()
    mp.text(i.get_x() + i.get_width() / 2, h, '%2.3f' % (h), ha='center', va='bottom',size='12')
mp.xticks(x, ['Gemm', 'Dsyrk', 'Dsyr2k', 'Tmm', 'Trmm', 'Matmul','AVG'])
mp.ylim(0.75,1.1)
mp.legend(loc='upper left',fontsize=12)
mp.show()