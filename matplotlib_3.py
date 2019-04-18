"""使用 matplotlib 提供的面向对象 API，需要导入 pyplot 模块，并约定简称为 plt
"""
from matplotlib import pyplot as plt
import numpy as np

x = np.linspace(0, 10, 20)
y = x * x + 2

print(x)
print(y)

"""绘制包含图标题、坐标轴标题以及图例的图形
"""

fig = plt.figure() # 新建图形对象

fig.add_subplot()

fig, axes = plt.subplots()

axes.set_xlabel('x label_test')
axes.set_ylabel('y label_test')
axes.set_title('title_test')

axes.plot(x, x**2,'r')
axes.plot(x, x**3,'r')
# 显示图例 legend  loc表示图例显示的位置  1表示右上角 2表示左上角  3表示左下角  4表示右下角  0表示自动匹配
axes.legend(["y = x**2", "y = x**3"], loc=2)

"""设置线的颜色、透明度
"""
fig, axes = plt.subplots()

axes.plot(x, x+1, color="red", alpha=0.1)
axes.plot(x, x+2, color="#1155dd")
axes.plot(x, x+3, color="#15cc55")


"""设置线型
"""
fig, ax = plt.subplots(figsize=(12,6))

# 线宽
ax.plot(x, x+1, color="blue", linewidth=0.25)
ax.plot(x, x+2, color="blue", linewidth=0.50)
ax.plot(x, x+3, color="blue", linewidth=1.00)
ax.plot(x, x+4, color="blue", linewidth=2.00)

# 虚线类型
ax.plot(x, x+5, color="red", lw=2, linestyle='-')
ax.plot(x, x+6, color="red", lw=2, ls='-.')
ax.plot(x, x+7, color="red", lw=2, ls=':')

# 虚线交错宽度
line, = ax.plot(x, x+8, color="black", lw=1.50)
line.set_dashes([5, 10, 15, 10])

# 符号
ax.plot(x, x+ 9, color="green", lw=2, ls='--', marker='+')
ax.plot(x, x+10, color="green", lw=2, ls='--', marker='o')
ax.plot(x, x+11, color="green", lw=2, ls='--', marker='s')
ax.plot(x, x+12, color="green", lw=2, ls='--', marker='1')

# 符号大小和颜色
ax.plot(x, x+13, color="purple", lw=1, ls='-', marker='o', markersize=2)
ax.plot(x, x+14, color="purple", lw=1, ls='-', marker='o', markersize=4)
ax.plot(x, x+15, color="purple", lw=1, ls='-', marker='o', markersize=8, markerfacecolor="red")
ax.plot(x, x+16, color="purple", lw=1, ls='-', marker='s', markersize=8,
        markerfacecolor="yellow", markeredgewidth=2, markeredgecolor="blue")


"""设置画布网格和坐标轴范围
"""
fig, axes = plt.subplots(1, 2, figsize=(10,5))

# 显示网格
axes[0].plot(x, x**2, x, x**3, lw=2)
axes[0].grid(True)

# 设置坐标轴范围
axes[1].plot(x, x**2, x, x**3)
axes[1].grid(True)
# 设置极限值，显示的极限值。只在这个范围显示数值。
axes[1].set_ylim([0, 60])
axes[1].set_xlim([2, 5])

plt.show()