import pandas as pd
import matplotlib.pyplot as plt
# Load the dataset
df = pd.read_csv('sales_data_sample.csv', encoding='latin1')

# Display the first few rows of the dataset
print(df.head())
# Get basic information about the dataset
print(df.info())

# Descriptive statistics
print(df.describe())

# Check for missing values
print(df.isnull().sum())
# Plot total sales per month


df['ORDERDATE'] = pd.to_datetime(df['ORDERDATE'])

# Extract year and month from ORDERDATE
df['YearMonth'] = df['ORDERDATE'].dt.to_period('M')


"""
# Analyze monthly sales trends
monthly_trends = df.groupby('YearMonth')['SALES'].sum()

# Plot a line chart for monthly sales trends
monthly_trends.plot(kind='line', marker='o', figsize=(12, 6))
plt.title('Monthly Sales Trends')
plt.xlabel('Year-Month')
plt.ylabel('Total Sales')
plt.grid(True)
plt.show()


"""

"""
# Analyze the best-selling products
best_selling_products = df.groupby('PRODUCTLINE')['QUANTITYORDERED'].sum().nlargest(10)

# Plot a bar chart for the top-selling products
best_selling_products.plot(kind='bar', figsize=(12, 6), color='coral')
plt.title('Top 10 Best-Selling Products')
plt.xlabel('Product Name')
plt.ylabel('Total Quantity Sold')
plt.show()

"""



# Analyze the distribution of customers by country
customer_country_distribution = df['COUNTRY'].value_counts()

# Plot a bar chart for customer distribution by country
customer_country_distribution.plot(kind='bar', figsize=(12, 6), color='skyblue')
plt.title('Customer Distribution by Country')
plt.xlabel('Country')
plt.ylabel('Number of Customers')
plt.show()





