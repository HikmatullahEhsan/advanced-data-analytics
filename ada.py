# Import necessary libraries
import pandas as pd  # Pandas is a powerful data manipulation and analysis library for Python.
import numpy as np  # NumPy is a library for numerical operations in Python, often used with Pandas.
import matplotlib.pyplot as plt  # Matplotlib is a plotting library for creating static, animated, and interactive visualizations.
import seaborn as sns  # Seaborn is a statistical data visualization library based on Matplotlib.

# Load the dataset
dikw = pd.read_csv(
    "data/DIKW_dataset.csv"
)  # Reads a CSV file into a Pandas DataFrame named 'dikw'.

# Display the shape of the DataFrame
print(dikw.shape)  # Prints the number of rows and columns in the DataFrame.

# Display the structure and data types of the DataFrame
print(
    dikw.info()
)  # Prints a concise summary of the DataFrame, including column names, data types, and non-null counts.

# Generate descriptive statistics
print(
    dikw.describe()
)  # Prints summary statistics of numerical columns in the DataFrame, such as count, mean, std, min, and max.

# Display unique countries in the dataset
print(
    dikw["Country"].unique()
)  # Prints an array of unique values in the 'Country' column.

# Select specific columns related to product sales
Product_Sales = dikw[
    ["ProductName", "TotalAmount"]
]  # Creates a new DataFrame with only 'ProductName' and 'TotalAmount' columns.

# Display the Product Sales DataFrame
print(Product_Sales)  # Prints the newly created DataFrame for product sales.

# Filter transactions for the United States
us_transactions = dikw[
    dikw["Country"] == "United States"
]  # Filters the original DataFrame for entries where 'Country' is 'United States'.

# Display US transactions
print(us_transactions)  # Prints the filtered DataFrame containing only US transactions.

# Calculate total amounts for each transaction
dikw["CalculatedTotal"] = (
    dikw["PricePerUnit"] * dikw["Quantity"]
)  # Creates a new column 'CalculatedTotal' by multiplying 'PricePerUnit' by 'Quantity'.

# Sort the DataFrame by Total Amount
sorted_dikw = dikw.sort_values(
    by="TotalAmount", ascending=False
)  # Sorts the DataFrame in descending order based on 'TotalAmount'.

# Display the sorted DataFrame
print(
    sorted_dikw
)  # Prints the sorted DataFrame to show transactions from highest to lowest total amount.

# Create a count plot of transactions by country
sns.countplot(
    data=dikw, x="Country"
)  # Creates a bar plot showing the count of transactions for each country.
plt.show()  # Displays the plot.

# Create a scatter plot of Quantity vs. Total Amount
sns.scatterplot(
    data=dikw, x="Quantity", y="TotalAmount", hue="Country"
)  # Creates a scatter plot with 'Quantity' on the x-axis and 'TotalAmount' on the y-axis, colored by 'Country'.
plt.show()  # Displays the scatter plot.

# Group by country and calculate total sales
country_sales = dikw.groupby("Country")[
    "TotalAmount"
].sum()  # Groups the DataFrame by 'Country' and sums the 'TotalAmount' for each country.
print(country_sales)  # Prints the total sales amount for each country.
