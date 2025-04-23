
import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity

# Load customer sales data
df = pd.read_csv("data/customer_sales.csv")

# Create pivot table
customer_product_matrix = df.pivot_table(
    index='CustomerName',
    columns='ProductName',
    values='SalesAmount',
    fill_value=0
)

cosine_sim = cosine_similarity(customer_product_matrix)
similarity_df = pd.DataFrame(cosine_sim, index=customer_product_matrix.index, columns=customer_product_matrix.index)

def get_similar_customers(customer_name, top_n=5):
    if customer_name not in similarity_df:
        return []
    similar_scores = similarity_df[customer_name].sort_values(ascending=False)[1:top_n+1]
    return similar_scores.index

def recommend_products(customer_name, top_n=5):
    similar_customers = get_similar_customers(customer_name, top_n)
    if not similar_customers:
        return []

    similar_data = customer_product_matrix.loc[similar_customers]
    mean_scores = similar_data.mean().sort_values(ascending=False)

    customer_products = customer_product_matrix.loc[customer_name]
    already_bought = customer_products[customer_products > 0].index

    recommendations = mean_scores.drop(already_bought).head(top_n)
    return recommendations
