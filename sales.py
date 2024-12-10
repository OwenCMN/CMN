import streamlit as st
import pandas as pd
import plotly.express as px

# Load data
@st.cache_data
def load_data():
    return pd.read_csv('sales_data.csv', parse_dates=['Date'])

df = load_data()

# Dashboard Title
st.title("Sales Dashboard")

# KPIs
total_sales = df['Sales'].sum()
total_quantity = df['Quantity'].sum()
average_sales = df['Sales'].mean()

col1, col2, col3 = st.columns(3)
col1.metric("💰 Total Sales", f"${total_sales:,.2f}")
col2.metric("📦 Total Quaantity Sold", f"{total_quantity}")
col3.metric("📊 Avg. Sales Per Transaction", f"${average_sales:,.2f}")

# Time Series Chart: Total Sales Over Time
st.header("📈 Sales Over Time")
sales_over_time = df.groupby('Date', as_index=False)[['Sales']].sum()
fig1 = px.line(sales_over_time, x='Date', y='Sales', title="Total Sales Over Time")
st.plotly_chart(fig1, use_container_width=True)

# Bar Chart: Sales by Region
st.header("🌍 Sales by Region")
sales_by_region = df.groupby('Region', as_index=False)[['Sales', 'Quantity']].sum()
fig2 = px.bar(sales_by_region, x='Region', y='Sales', color='Region',
              title="Sales by Region")
st.plotly_chart(fig2, use_container_width=True)

# Pie Chart: Sales by Product Category
st.header("🛍 Sales by Product Category")
sales_by_product = df.groupby('Product', as_index=False)[['Sales']].sum()
fig3 = px.pie(sales_by_product, names='Product', values='Sales',
              title="Sales by Product Category")
st.plotly_chart(fig3, use_container_width=True)

# Bar Chart: Quantity Sold by Region
st.header("📦 Quantity Sold by Region")
quantity_by_region = df.groupby('Region', as_index=False)[['Quantity']].sum()
fig4 = px.bar(quantity_by_region, x='Region', y='Quantity', color='Region', 
              title="Quantity Sold by Region")
st.plotly_chart(fig4, use_container_width=True)

# Footer
st.markdown("""
---
* Supermarket Sales Dashboard built with ❤ by Owen.*
""")