import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Task 1: Load and Explore the Dataset
try:
    # Load the dataset
    df = pd.read_csv("your_dataset.csv")  # Replace with the actual dataset file
    
    # Display first few rows
    print("First five rows of the dataset:")
    print(df.head())
    
    # Check for missing values
    print("\nMissing values:")
    print(df.isnull().sum())
    
    # Fill or drop missing values
    df = df.dropna()  # Alternatively, df.fillna(method='ffill', inplace=True)
    
    # Check dataset info
    print("\nDataset Info:")
    print(df.info())
except FileNotFoundError:
    print("Error: File not found. Please check the file path.")

# Task 2: Basic Data Analysis
print("\nStatistical summary:")
print(df.describe())

# Grouping data by a categorical column and computing mean
if 'CategoryColumn' in df.columns:
    print("\nAverage values by category:")
    print(df.groupby('CategoryColumn').mean())

# Task 3: Data Visualization
sns.set(style="whitegrid")

# Line Chart
plt.figure(figsize=(10,5))
if 'DateColumn' in df.columns and 'NumericColumn' in df.columns:
    df.plot(x='DateColumn', y='NumericColumn', kind='line', title='Trend Over Time')
    plt.xlabel('Date')
    plt.ylabel('Value')
    plt.show()

# Bar Chart
plt.figure(figsize=(10,5))
if 'CategoryColumn' in df.columns and 'NumericColumn' in df.columns:
    df.groupby('CategoryColumn')['NumericColumn'].mean().plot(kind='bar', title='Comparison Across Categories')
    plt.xlabel('Category')
    plt.ylabel('Average Value')
    plt.show()

# Histogram
plt.figure(figsize=(10,5))
if 'NumericColumn' in df.columns:
    df['NumericColumn'].plot(kind='hist', bins=20, title='Distribution of Values')
    plt.xlabel('Value')
    plt.show()

# Scatter Plot
plt.figure(figsize=(10,5))
if 'NumericColumn1' in df.columns and 'NumericColumn2' in df.columns:
    sns.scatterplot(x=df['NumericColumn1'], y=df['NumericColumn2'])
    plt.title('Relationship Between Two Numerical Variables')
    plt.xlabel('NumericColumn1')
    plt.ylabel('NumericColumn2')
    plt.show()
