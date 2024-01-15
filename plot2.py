import matplotlib.pyplot as plt
# Sample data: Population distribution by age group in a city
age_groups = ["0-10", "11-20", "21-30", "31-40", "41-50", "51-60", "61-70", "71+"]
population = [15000, 22000, 30000, 28000, 25000, 18000, 12000, 8000]
# Create the bar plot
plt.barh(age_groups, population, color='lightblue')
# Add labels and a title
plt.xlabel("Age Group")
plt.ylabel("Population")
plt.title("Population Distribution by Age Group")
# Display the plot
plt.show()
