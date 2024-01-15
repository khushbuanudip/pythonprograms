import matplotlib.pyplot as plt
# Market share data
manufacturers = ['Samsung', 'Apple', 'Huawei', 'Xiaomi', 'Others']
market_share = [30, 25, 18, 12, 15]
# Colors for each slice
colors = ['lightblue', 'lightcoral', 'lightgreen', 'lightpink', 'lightgrey']
# Create a pie chart
plt.pie(market_share, labels=manufacturers, colors=colors, autopct='%1.1f%%')
# Title
plt.title('Smartphone Market Share')
# Show the pie chart
plt.show()
