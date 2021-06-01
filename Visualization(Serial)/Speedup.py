import numpy as np
import matplotlib.pyplot as mp

# 设置中文字体
mp.rcParams['font.sans-serif'] = ['SimHei']
# mp.rcParams['axes.unicode_minus'] = False


ptss = np.array([5.65047,9.90160,5.741731,4.254189,9.264703,1.449157,6.043641])
gtss = np.array([6.07547,10.72854,6.539737,4.622516,10.27579,1.578767,6.6368033])
#mp.figure('Bar Chart', facecolor='lightgray')
#mp.title('Bar Chart', fontsize=16)
mp.xlabel('Models', fontsize=18)
mp.ylabel('Speedup', fontsize=18)
mp.tick_params(labelsize=16)
mp.grid(linestyle=':', axis='y')
x = np.arange(7)
a = mp.bar(x - 0.2, ptss, 0.3, color='orange', label='Pluto', align='center',hatch = '-')
b = mp.bar(x + 0.2, gtss, 0.3, color='orangered', label='TSS-T6-Random', align='center',hatch = '/')
# 设置标签
for i in a + b:
    h = i.get_height()
    mp.text(i.get_x() + i.get_width() / 2, h, '%2.2f' % (h), ha='center', va='bottom',size='12')
mp.xticks(x, ['Gemm', 'Dsyrk', 'Dsyr2k', 'Tmm', 'Trmm', 'Matmul','AVG'])
mp.ylim(0,12)
mp.legend(fontsize=12)
mp.show()