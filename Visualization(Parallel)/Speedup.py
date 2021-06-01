import numpy as np
import matplotlib.pyplot as mp

import numpy as np
import matplotlib.pyplot as mp
# 设置中文字体
#mp.rcParams['font.sans-serif'] = ['SimHei']
# mp.rcParams['axes.unicode_minus'] = False

tss1 = np.array([1.2643,1.2844,1.8079,1.097,6.2316,1.3633,2.17475])
tss10 = np.array([1.2479,1.2721,1.7558,1.2286,6.1222,1.3836,2.1684])
tsslc = np.array([1.3740,1.3716,1.9638,1.3992,6.6055,1.5102,2.3707])
pluto = np.array([1.2790,1.3021,1.6439,1.3439,6.1288,1.4644,2.1936])
So = np.array([1.4568,1.4346,2.08851,1.5080,6.8588,1.6148,2.493585])


# 设置中文字体
mp.rcParams['font.sans-serif'] = ['SimHei']
# mp.rcParams['axes.unicode_minus'] = False


ptss = np.array([1.2790,1.3021,1.6439,1.467828,6.1288,1.4644,2.214338])
gtss = np.array([1.3740,1.3716,1.9638,1.658547,6.6055,1.5102,2.413941])
#mp.figure('Bar Chart', facecolor='lightgray')
#mp.title('Bar Chart', fontsize=16)
mp.xlabel('Models', fontsize=18)
mp.ylabel('Speedup', fontsize=18)
mp.tick_params(labelsize=16)
mp.grid(linestyle=':', axis='y')
x = np.arange(7)


a = mp.bar(x - 0.2, ptss, 0.3, color='orange', label='Pluto', align='center',hatch = '-')
b = mp.bar(x + 0.2, gtss, 0.3, color='green', label='TSSP-T6-Search', align='center',hatch = '/')
# 设置标签
for i in a + b:
    h = i.get_height()
    mp.text(i.get_x() + i.get_width() / 2, h, '%2.2f' % (h), ha='center', va='bottom',size='12')
mp.xticks(x, ['Gemm', 'Dsyrk', 'Dsyr2k', 'Tmm', 'Trmm', 'Matmul','AVG'])
mp.ylim(0,7)
mp.legend(loc='upper left',fontsize=12)
mp.show()