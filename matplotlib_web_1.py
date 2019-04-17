import numpy as np
import matplotlib.mlab as mlab
import matplotlib.pyplot as plt

X = [0.5]
XX = [1.5]
Y = [20]
YY = [23]
# fig = plt.figure()
plt.bar(X, Y, 1, color="blue")
plt.bar(XX, YY, 1, color="yellow")  # 使用不同颜色
plt.xlabel("X-axis")  # 设置X轴Y轴名称
plt.ylabel("Y-axis")
plt.title("bar chart")
# 使用text显示数值
for a, b in zip(X, Y):
    c=b+1
    # c是表示的数值   a和b是表示文字的坐标
    plt.text(a, b + 0.05, '%.0f' % c, ha='center', va='bottom', fontsize=11)
for a, b in zip(XX, YY):
    plt.text(a, b + 0.05, '%.0f' % b, ha='center', va='bottom', fontsize=11)
plt.ylim(0, 37)  # 设置Y轴上下限
plt.show()

"""
用python画柱状图容易，但是如何对不同柱子使用不同颜色呢？同时在柱子顶端显示精确数值？

主要用的方法为：
atplotlib.pyplot.bar(left, height, width=0.8, bottom=None, hold=None, data=None, **kwargs)

参数说明：
left: 每一个柱形左侧的X坐标

height:每一个柱形的高度

width: 柱形之间的宽度

bottom: 柱形的Y坐标

color: 柱形的颜色
--------------------- 

首先，前边设置的x、y值其实就代表了不同柱子在图形中的位置（坐标），
通过for循环找到每一个x、y值的相应坐标——a、b，再使用plt.text在对应位置添文字说明来生成相应的数字标签，
而for循环也保证了每一个柱子都有标签。

其中，a, b+0.05表示在每一柱子对应x值、y值上方0.05处标注文字说明，
'%.0f' % b,代表标注的文字，即每个柱子对应的y值， ha='center',
va= 'bottom'代表horizontalalignment（水平对齐）、verticalalignment（垂直对齐）的方式，fontsize则是文字大小。

"""