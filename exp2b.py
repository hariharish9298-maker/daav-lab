import pandas as pd
# Load dataset into a DataFrame
df = pd.read_csv('data.csv')
# Display first and last few rows
print("First 5 rows:\n", df.head())
print("Last 5 rows:\n", df.tail())
# Check data types and general info
df.info()
# Summary statistics
print("Summary statistics:\n", df.describe())
# Handle missing values
df.fillna(df.mean(), inplace=True)
# Create a new column
df['new_column'] = df['existing_column'] * 2
# Create a Series and perform operations
series = df['existing_column']
print("Series addition:", series + 10)
# Filter rows based on conditions
filtered_df = df[(df['existing_column'] > 50) & (df['another_column'] < 100)]
print("Filtered DataFrame:\n", filtered_df)
# Grouping and aggregation
grouped = df.groupby('category_column')['numeric_column'].mean()
print("Grouped mean:\n", grouped)
# Sorting
df_sorted = df.sort_values(by='numeric_column', ascending=False)
print("Sorted DataFrame:\n", df_sorted)
# Boolean masking
masked_df = df[df['numeric_column'] > df['numeric_column'].median()]
print("Masked DataFrame:\n", masked_df)
# Remove duplicates and drop missing values
df.drop_duplicates(inplace=True)
df.dropna(inplace=True)
# Create a new DataFrame with selected columns
subset_df = df[['column1', 'column2']]
# Save the new DataFrame to a CSV file
subset_df.to_csv('filtered_data.csv', index=False)
# Compute summary statistics
print("Total sum:", df['numeric_column'].sum())
print("Mean:", df['numeric_column'].mean())
print("Standard Deviation:", df['numeric_column'].std()
