
import streamlit as st
from recommender import recommend_products
import pandas as pd

st.title("AdventureWorks Customer Recommender")

# Load mock customer data
df = pd.read_csv("data/customer_sales.csv")
customer_names = df['CustomerName'].unique()

selected_customer = st.selectbox("Select a customer:", customer_names)

if st.button("Recommend Products"):
    recommendations = recommend_products(selected_customer)
    st.write("Recommended Products:")
    st.write(recommendations)
