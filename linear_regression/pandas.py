#pip install pandas


import pandas as pd

# Creating a DataFrame from a dictionary
data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eve'],
    'Age': [25, 30, 35, 28, 22],
    'City': ['Port Moresby', 'Lae', 'Mt Hagen', 'Kokopo', 'Kimbe']
}

df = pd.DataFrame(data)

# Display the DataFrame
print("DataFrame:")
print(df)

# Accessing specific columns
print("\nName Column:")
print(df['Name'])

# Filtering data based on a condition
print("\nPeople over 30:")
print(df[df['Age'] > 30])

# Basic statistics
print("\nSummary statistics:")
print(df.describe())




