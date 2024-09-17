import matplotlib
import pandas as pd
import matplotlib.pyplot as plt


file_path = '/Users/arthurzeng/desktop/宏远客诉文件/统一格式/客诉汇总数据.xlsx'
data = pd.read_excel(file_path)

data['日期'] = pd.to_datetime(data['日期'])  # 确保'日期'列是日期时间格式
data['月份'] = data['日期'].dt.to_period('M')  # 从'日期'列中提取月份并创建'月份'列

# 转换'投诉数量'为数值，处理非数值数据
data['投诉数量'] = pd.to_numeric(data['投诉数量'], errors='coerce')
data_cleaned = data.dropna(subset=['投诉数量'])

# 现在可以安全地使用'月份'列进行分组
monthly_complaints_cleaned = data_cleaned.groupby('月份')['投诉数量'].sum()

data['投诉数量'] = pd.to_numeric(data['投诉数量'], errors='coerce')
data_cleaned = data.dropna(subset=['投诉数量'])


# Plotting the cleaned data
plt.figure(figsize=(10, 6))
monthly_complaints_cleaned.plot(kind='bar', color='skyblue')
plt.title('Number of complaints per month')
plt.xlabel('Months')
plt.ylabel('Number of complaints')
plt.xticks(rotation=45)
plt.grid(True)
plt.tight_layout()
plt.show()