import pandas as pd
df=pd.read_csv('orders.csv')
#cleaning data
df = df.drop_duplicates()#for duplicates
#setting mean for null values in price column
df["price"] = df["price"].fillna(df["price"].mean())
#setting 1 for null values in quantity column
df["quantity"] = df["quantity"].fillna(1)
#converting order_date to datetime format
df["order_date"] = pd.to_datetime(df["order_date"])


#creating new column total_amount by multiplying price and quantity
df["total_amount"] = df["price"] * df["quantity"]
#extracting year, month and day from order_date column
df["year"] = df["order_date"].dt.year   
df["month"] = df["order_date"].dt.month
df["day"] = df["order_date"].dt.day


#calculating total revenue
total_revenue = df["total_amount"].sum()
print("Total Revenue:", total_revenue)

#daily sales by grouping order_date and summing total_amount
daily_sales = df.groupby("order_date")["total_amount"].sum().reset_index()

#category-wise sales by grouping category and summing total_amount
category_sales = df.groupby("category")["total_amount"].sum().reset_index()

#city-wise sales by grouping city and summing total_amount
city_sales = df.groupby("city")["total_amount"].sum().reset_index()

#top customers by grouping customer_id and summing total_amount, then sorting in descending order
top_customers = df.groupby("customer_id")["total_amount"].sum().reset_index().sort_values(by="total_amount", ascending=False)


df.to_csv("clean_orders.csv", index=False)
daily_sales.to_csv("daily_sales.csv", index=False)
category_sales.to_csv("category_sales.csv", index=False)
city_sales.to_csv("city_sales.csv", index=False)
top_customers.to_csv("top_customers.csv", index=False)(    )
