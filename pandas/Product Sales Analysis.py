import pandas as pd

data = {
    "Product Name": ["Laptop", "Phone", "Tablet", "Headphones", "Keyboard"],
    "Category": ["Electronics", "Electronics", "Electronics", "Accessories", "Accessories"],
    "Price": [50000, 30000, 20000, 2000, 1500],
    "Quantity Sold": [20, 60, 40, 80, 55]
}

df = pd.DataFrame(data)

# Calculate total sales
df["Total Sales"] = df["Price"] * df["Quantity Sold"]

print("Product Data:")
print(df)

# Product with highest sales
highest = df.loc[df["Total Sales"].idxmax()]

print("\nProduct with highest sales:")
print(highest)

# Average product price
print("\nAverage Product Price:")
print(df["Price"].mean())

# Products with quantity sold greater than 50
print("\nProducts with quantity sold greater than 50:")
print(df[df["Quantity Sold"] > 50])

# Sort based on total sales
print("\nProducts sorted by total sales:")
print(df.sort_values("Total Sales"))
