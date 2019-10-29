import matplotlib.pyplot as plt # 数据可视化

# 解决中文字体显示问题
import matplotlib
matplotlib.rcParams['font.sans-serif']=['simhei'] # 配置字体
matplotlib.rcParams['font.family']='sans-serif'

plt.bar([1],[100],label="北京",color='y')
plt.bar([2],[300],label="山东")
plt.bar([3],[150],label="广东")

plt.legend() # 绘制
plt.savefig("1.jpg")# 保存图片
plt.show() # 显示

