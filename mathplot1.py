import matplotlib.pyplot as plt
# Sample data: Daily temperatures for a month
days = list(range(1, 31))
temperatures = [68, 70, 72, 75, 77, 80, 82, 83, 81, 78, 75, 72, 71, 70, 72, 74, 77, 79,
80, 82, 84, 86, 88, 87, 85, 82, 80, 77, 75, 73]
# Create the line plot
plt.plot(days, temperatures,marker='o')
# Add labels and a title
plt.xlabel("Day of the Month")
plt.ylabel("Temperature (°F)")
plt.title("Daily Temperature Over a Month")
plt.show()
