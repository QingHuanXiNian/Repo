import pandas as pd
import matplotlib.pyplot as plt

# 从CSV文件读取数据
data = pd.read_csv(r'C:\Users\LX\Desktop\学习\数据可视化\world-population.csv')

# 提取横轴和纵轴数据
x_values = data['Year']
y_values = data['Population']

# 创建折线图
plt.plot(x_values, y_values, marker='o')
plt.title('World Population')
plt.xlabel('Year')
plt.ylabel('Population')
plt.show()
