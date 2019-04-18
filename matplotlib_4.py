from matplotlib import pyplot as plt
import numpy as np

x = np.linspace(0, 10, 20)
y = x * x + 2

print(x)
print(y)


"""绘制散点图、梯步图、条形图、面积图
"""
n = np.array([0,1,2,3,4,5])

fig, axes = plt.subplots(1, 4, figsize=(16,5))

axes[0].scatter(x, x + 0.25*np.random.randn(len(x)))
axes[0].set_title("scatter")

axes[1].step(n, n**2, lw=2)
axes[1].set_title("step")

axes[2].bar(n, n**2, align="center", width=0.5, alpha=0.5)
axes[2].set_title("bar")

axes[3].fill_between(x, x**2, x**3, color="green", alpha=0.5)
axes[3].set_title("fill_between")


"""绘制雷达图
"""
fig = plt.figure(figsize=(6,6))
ax = fig.add_axes([0.0, 0.0, .6, .6], polar=True)
t = np.linspace(0, 2 * np.pi, 100)
ax.plot(t, t, color='blue', lw=3)


"""绘制直方图
"""
n = np.random.randn(100000)
fig, axes = plt.subplots(1, 2, figsize=(12,4))

axes[0].hist(n)
axes[0].set_title("Default histogram")
axes[0].set_xlim((min(n), max(n)))

axes[1].hist(n, cumulative=True, bins=50)
axes[1].set_title("Cumulative detailed histogram")
axes[1].set_xlim((min(n), max(n)))

plt.show()