import numpy as np
import matplotlib.pyplot as mp

# 设置中文字体
#mp.rcParams['font.sans-serif'] = ['SimHei']
# mp.rcParams['axes.unicode_minus'] = False
fig=mp.gcf()
fig.set_size_inches(18,10)
tss1 = np.array([1.1617,1.1319,1.16325,1.2580382,1.1245,1.2044,1.17396])
tss10 = np.array([1.1781,1.1379,1.2033,1.2324656,1.1401,1.1775,1.178227])
tsslc = np.array([1.0649,1.0465,1.0692,1.0576769,1.0390,1.0700,1.057879])
pluto = np.array([1.150,1.1047,1.2719, 1.213444,1.1478,1.1092,1.1661739])

# ptss = np.array([1.2790714219254447,1.2481219631319513,1.6439511256483947,1.343966418615594, 6.128879519183511,1.4644432399551648,2.1847389480766766])
# gtss = np.array([1.374065260408715,1.3716485037834816,1.96388009818339,1.3992445397509903, 6.605520762017123,1.5102665681152647,2.3707709553764937])
# #mp.figure('Bar Chart', facecolor='lightgray')
#mp.title('Bar Chart', fontsize=16)
mp.xlabel('Models', fontsize=18)
mp.ylabel('Nomalization Time', fontsize=18)
mp.tick_params(labelsize=18)
mp.grid(linestyle=':', axis='y')
x = np.arange(7)
a = mp.bar(x - 0.3, tss1, 0.1, color='dodgerblue', label='TSSP-T1', align='center')
b = mp.bar(x - 0.15, tss10, 0.1, color='orangered', label='TSSP-T6-Random', align='center',hatch = '/')
c = mp.bar(x - 0.0, tsslc, 0.1, color='green', label='TSSP-T6-Search', align='center',hatch = '|')
d = mp.bar(x + 0.15, pluto, 0.1, color='orange', label='Pluto', align='center',hatch = '-')
#e = mp.bar(x + 0.3, So, 0.1, color='b', label='Oracle(Exhaustive Search)', align='center',hatch = '+')
# 设置标签
for i in a + b+c+d:
    h = i.get_height()
    mp.text(i.get_x() + i.get_width() / 2, h, '%2.3f' % (h), ha='center', va='bottom',size='14')
mp.xticks(x, ['Gemm', 'Dsyrk', 'Dsyr2k', 'Tmm', 'Trmm', 'Matmul','AVG'])
mp.ylim(1,1.3)
mp.legend(loc='upper left',fontsize=20)
mp.show()

