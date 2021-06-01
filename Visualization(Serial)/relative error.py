import numpy as np
import matplotlib.pyplot as mp

# 设置中文字体
mp.rcParams['font.sans-serif'] = ['SimHei']
# mp.rcParams['axes.unicode_minus'] = False


#otss = np.array([0.079,0.096, 0.099, 0.066,0.0735,0.154])
gtss = np.array([0.05757,0.05308,0.05785, 0.03980, 0.06920,0.15587,0.07222833])
#mp.figure('Bar Chart', facecolor='lightgray')
#mp.title('Bar Chart', fontsize=16)
mp.xlabel('Models', fontsize=18)
mp.ylabel('Mean Relative Error', fontsize=18)
mp.tick_params(labelsize=16)
mp.grid(linestyle=':', axis='y')
x = np.arange(7)
#a = mp.bar(x - 0.2, otss, 0.3, color='dodgerblue', label='O-TSS', align='center')
b = mp.bar(x , gtss, 0.3, color='orangered', label='TSS', align='center')
# 设置标签
for i in b:
    h = i.get_height()
    mp.text(i.get_x() + i.get_width() / 2, h, '%2.5f' % (h), ha='center', va='bottom',size='10')
mp.xticks(x, ['Gemm', 'Dsyrk', 'Dsyr2k', 'Tmm', 'Trmm', 'Matmul','AVG'])
mp.ylim(0,0.2)
mp.legend()
mp.show()