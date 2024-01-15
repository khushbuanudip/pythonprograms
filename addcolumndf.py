import pandas as pd
# Create an initial DataFrame
data = {'Name': ['Alice', 'Bob', 'Charlie', 'David'],
'Age': [25, 30, 35, 28],
'City': ['New York', 'Los Angeles', 'Chicago', 'Houston']}
df = pd.DataFrame(data)
# Display the initial DataFrame
print("Initial DataFrame:")
print(df)
# Create data for the new row
new_row = pd.DataFrame([{'Name': 'Eve', 'Age': 24, 'City': 'San Francisco'}])
#now we are adding a row at the end of the DataFrame
df = pd.concat([df, new_row], ignore_index=True)
# Display the DataFrame with the new row
print("\nDataFrame after adding a new row:")
print(df)
