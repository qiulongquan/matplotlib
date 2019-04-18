```
在使用机器学习方法解决问题的过程中，一定会遇到需要针对数据进行绘图的场景。
Matplotlib 是支持 Python 语言的开源绘图库，因为其支持丰富的绘图类型、简单的绘图方式以及完善的接口文档，
深受 Python 工程师、科研学者、数据工程师等各类人士的喜欢。Matplotlib 拥有着十分活跃的社区以及稳定的版本迭代，
在机器学习的时候，掌握 Matplotlib 的使用无疑是最重要的准备工作之一。
将使用 Matplotlib 绘制 2D 和 3D 图形的方法。

MATLAB，它是一种用于算法开发、数据可视化、数据分析以及数值计算的高级技术计算语言和交互式环境。
而在 Matplotlib 中，也提供了和 MATLAB 相似的 API。

matplotlib 可以视为Python 数据可视化的基准和主力，它与 NumPy 紧密集成。

实验知识点

兼容 MATLAB 代码风格 API
图名称、坐标轴名称、图例
线型、颜色、透明度
画布网格、坐标轴范围
其他 2D 图形
3D 图形


里面有很多matplotlib的图形画法，可以参考。
matplotlib 的主要资源可以在下面的网站上找到。
matplotlib 主页当然是最好的起点：http://matplotlib.org
matplotlib 网站上有一个展厅,其中有许多实用示例：http://matplotlib.org/gallery.html
这里可以找到一个 2D绘图的教程：http://matplotlib.org/users/pyplot_tutorial.html
这里是 3D绘图教程：http://matplotlib.org/mpl_toolkits/mplot3d/tutorial.html


#-*- coding: utf-8 -*-
from matplotlib import pyplot as plt
plt.rcParams['font.sans-serif']=['SimHei'] #用来正常显示中文标签
plt.rcParams['axes.unicode_minus']=False #用来正常显示负号
#有中文出现的情况，需要u'内容'

# python matplotlib 中文显示参数设置
# https://segmentfault.com/a/1190000005144275
```