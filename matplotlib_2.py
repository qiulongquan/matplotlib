"""使用 matplotlib 提供的面向对象 API，需要导入 pyplot 模块，并约定简称为 plt
"""
from matplotlib import pyplot as plt
import numpy as np

x = np.linspace(0, 10, 20)
y = x * x + 2

print(x)
print(y)
#
# """方法 1：绘制上方一致的图形
# """
# fig = plt.figure() # 新建图形对象
#
# axes = fig.add_axes([0.1, 0.1, 0.8, 0.8]) # 控制画布的左, 下, 宽度, 高度 (从 0 到 1)
#
#
# axes.plot(x, y, 'r')
# # plt.show()
#
# """同样，我们可以绘制子图
# """
# fig, axes = plt.subplots(nrows=1, ncols=2) # 子图为 1 行，2 列
#
# for ax in axes:
#     ax.plot(x, y, 'r')
# # plt.show()

# """还能将一张图绘制在另一张图的内部
# """
# fig = plt.figure() # 新建画板
#
# axes1 = fig.add_axes([0.1, 0.1, 0.8, 0.8]) # 大画布
# axes2 = fig.add_axes([0.2, 0.5, 0.4, 0.3]) # 小画布
#
# # 大画布
# axes1.plot(x, y, 'r')
#
# # 小画布
# axes2.plot(y, x, 'g')
# plt.show()


"""
方法 3：使用 add_subplot() 添加画布
这里比较推荐使用 plt.subplots()，而下面的许多例子也将采用这种方式展开。
"""
fig = plt.figure() # 新建图形对象

fig.add_subplot()

plt.plot(x, y, 'r')
# plt.show()

"""调节画布尺寸和显示精度
"""
fig, axes = plt.subplots(figsize=(10,10), dpi=50) # 通过 figsize 调节尺寸, dpi 调节显示精度

axes.plot(x, y, 'r')


# 图名称、坐标轴名称、图例
"""设置图标题
"""
axes.set_title("title_test")

"""设置坐标轴名称
"""
axes.set_xlabel("x zhou")
axes.set_ylabel("y zhou")

"""设置图例,默认右上角显示
"""
axes.legend(["label1_tushi显示"])

plt.show()