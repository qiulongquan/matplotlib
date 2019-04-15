# 使用兼容 MATLAB 风格的 API 的好处在于，如果熟悉 MATLAB，那么将很快上手使用 Python 绘图。
# 不过，除了一些简单的图形之外，并不鼓励使用兼容MATLAB 的 API。
# 于此同时，实验更加建议学习和使用 Matplotlib 提供的面向对象 API，它更加强大和好用

"""使用 matplotlib 提供的兼容 MATLAB API，需要导入 pylab 模块
"""
from matplotlib import pylab

"""使用 NumPy 生成随机数据
"""
import numpy as np

# >>> np.linspace(2.0, 3.0, num=5)
# array([ 2.  ,  2.25,  2.5 ,  2.75,  3.  ])
x = np.linspace(0, 10, 20)
y = x * x + 2

"""只需要 1 句命令就可以完成绘图
"""
pylab.plot(x, y, 'r') # 'r' 代表 red
pylab.show()
"""绘制子图
"""
# 索引如果一样，表示在一张图片中显示
pylab.subplot(1,2,1) # 括号中内容代表（行，列，索引）
pylab.plot(x, y, 'r--') # ‘’ 中的内容确定了颜色和线型

pylab.subplot(1,2,1)
pylab.plot(y, x, 'g*-')

pylab.show()