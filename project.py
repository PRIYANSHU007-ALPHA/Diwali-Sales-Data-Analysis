import pandas as pd #pandas is use for data manipulation and analysis
import numpy as np #numpy is used for numerical operations
import matplotlib.pyplot as plt #matplotlib is used for plotting graphs
import seaborn as sns #seaborn is used for statistical data visualization

df = pd.read_csv(r"C:\Users\priya\OneDrive\Documents\data analysis project\Diwali_Sales_Analysis\Diwali Sales Data.csv", encoding='unicode_escape') # Load the dataset
print(df.shape) # Display the shape of the DataFrame
print(df.head(10)) # Display the first ten rows of the DataFrame
print(df.info()) # Display information about the DataFrame
df.drop(["Status", "unnamed1"], axis=1, inplace=True) # Drop unnecessary columns
print(df.head()) # Display the first five rows after dropping columns
print(pd.isnull(df).sum())# Check for null values in the DataFrame and sum is used to get the total count of null values in each column
df.dropna(inplace=True) # Drop rows with null values
print(df.shape) # Display the shape of the DataFrame after dropping null values
print(pd.isnull(df).sum()) # Check for null values again to confirm they have been dropped
df["Amount"] = df["Amount"].astype("int") # Convert the "Amount" column to integer type
print(df["Amount"].dtype) # Display the data type of the "Amount" column
print(df.columns) # Display the column names of the DataFrame
print(df.describe()) # Display descriptive statistics of the DataFrame
print(df[["Age","Amount","Orders"]].describe()) # Display descriptive statistics for specific columns

#start exploratory data analysis
#GENDER
ax = sns.countplot(x = "Gender", data=df) # Countplot used to visualize the distribution

for bars in ax.containers:
    ax.bar_label(bars) # Add labels to the bars in the count

plt.show() # Display the plot window

sales_gender =df.groupby(["Gender"], as_index=False)["Amount"].sum().sort_values(by="Amount", ascending=False) # this is used to group the DataFrame 
sns.barplot(x = "Gender", y = "Amount", data=sales_gender) # Bar plot
plt.show()
#from the above the graph we can see that the most of the buyers are female and the purchasing power of females are more than 

# AGE DISTRIBUTION ANALYSIS

# Age distribution by Gender (countplot)
# Create age groups
age_bins = [0, 18, 25, 35, 45, 55, 65, 100] # Define the bins for age groups
age_labels = ['0-18', '19-25', '26-35', '36-45', '46-55', '56-65', '65+'] # Define labels for each age group
df['AgeGroup'] = pd.cut(df['Age'], bins=age_bins, labels=age_labels) # Create a new column 'AgeGroup' by categorizing 'Age' into bins

# Age group distribution by Gender (countplot)
ax = sns.countplot(x="AgeGroup", hue="Gender", data=df) # Plot count of each age group split by gender
for bars in ax.containers:
    ax.bar_label(bars) # Add labels to each bar in the plot
plt.show() # Display the 
#from the above graph we can see that the most of the buyers are in the age group of 26-35 and most of the buyers is female

# STATE ANALYSIS
# TOTAL NUMBER OF ORDERS BY STATE TOP 10 STATES
top_state = df.groupby(["State"], as_index=False)["Orders"].sum().sort_values(by="Orders", ascending=False).head(10) # Group by state and sum orders, then sort and take top 10
sns.barplot(x="Orders", y="State", data=top_state) # Bar plot for top 10 states by number of orders
plt.title("Top 10 States by Number of Orders") # Set title for the plot
plt.show() # Display the plot

# TOTAL AMOUNT BY STATE TOP 10 STATES
top_state_amount = df.groupby(["State"], as_index=False)["Amount"].sum().sort_values(by="Amount", ascending=False).head(10) # Group by state and sum amount, then sort and take top 10
sns.barplot(x="Amount", y="State", data=top_state_amount) # Bar plot for top 10 states by amount
plt.title("Top 10 States by Amount") # Set title for the plot
plt.show() # Display the plot
# from the above two graphs we can see that the most of the orders are from uttar pradesh and maharashtra and the most of the amount is from uttar pradesh and maharashtra

#Marital_Status analysis
sns.countplot(x="Marital_Status", data=df) # countplot is used to visualize the distribution of marital status
for bars in ax.containers:
    ax.bar_label(bars) # Add labels to the bars in the count plot
plt.title("Marital Status Distribution") # Set title for the plot
plt.show() # Display the plot

# Marital Status based on amount
sales_state= df.groupby(["Marital_Status", "Gender"], as_index=False)["Amount"].sum().sort_values(by="Amount", ascending=False) # Group by marital status and gender, then sum amount
sns.barplot(x="Marital_Status", y="Amount", hue="Gender", data=sales_state) # Bar plot for marital status based on amount
#plt.title("Marital Status vs Amount") # Set title for the plot
plt.show() # Display the plot
#from above graph we can see that the most of the buyers are married(women) and they have more purchasing power than unmarried

#OCCUPATION ANALYSIS
# Set figure size for the plots
ax = sns.countplot(x="Occupation", data=df) # Countplot for occupation distribution
for bars in ax.containers:
    ax.bar_label(bars) # Add labels to the bars in the count plot

plt.title("Occupation Distribution") # Set title for the plot
plt.show() # Display the plot

# Occupation based on amount
sales_occupation = df.groupby(["Occupation"], as_index=False)["Amount"].sum().sort_values(by="Amount", ascending=False) # Group by occupation and sum amount
sns.barplot(x="Occupation", y="Amount", data=sales_occupation) # Bar plot for occupation based on amount
plt.title("Occupation vs Amount") # Set title for the plot
plt.show() # Display the plot
# from the above two graphs we can see that the most of the buyers are working in it sector and healthcare and they have more purchasing power than others

# PRODUCT ANALYSIS
# Product category distribution
sns.set(rc={"figure.figsize":(10,6)}) # Set figure size for the plots
ax = sns.countplot(x="Product_Category", data=df) # Countplot for product category distribution
for bars in ax.containers:
    ax.bar_label(bars)  # Add labels to the bars in the count plot
plt.title("Product Category Distribution") # Set title for the plot
plt.show() # Display the plot

# Product category based on amount
sales_product = df.groupby(["Product_Category"], as_index=False)["Amount"].sum().sort_values(by="Amount", ascending=False).head(10) # Group by product category and sum amount
sns.barplot(x="Product_Category", y="Amount", data=sales_product) # Bar plot for product category based on amount
plt.title("Product Category based on amount") # Set title for the plot
plt.show() # Display the plot
#from the above two graphs we can see that the most of the buyers are buying products from  Food,electronics and clothing 

#find the top selling product in each category
top_selling_product = df.groupby(["Product_ID"], as_index=False)["Orders"].sum().sort_values(by="Orders", ascending=False).head(10) # Group by product ID and sum orders, then sort and take top 10
sns.barplot(x="Orders", y="Product_ID", data=top_selling_product) # Bar plot for top selling products in each category
plt.title("Top Selling Products in Each Category") # Set title for the plot
plt.show() # Display the plot

