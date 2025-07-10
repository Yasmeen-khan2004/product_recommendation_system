import streamlit as st
import pandas as pd
import joblib

st.set_page_config(page_title="🛍️ Product Recommendation Dashboard")

st.title("🛍️ Product Recommendation Dashboard")

# Load data
df = pd.read_csv('data/Products_dataset.csv')
df['product_name'] = df['product_name'].fillna('')

# Load model
model = joblib.load('models/recommender_model.pkl')
cosine_sim = model['cosine_sim']

# Map product indices
indices = pd.Series(df.index, index=df['product_name']).drop_duplicates()

# Recommend function
def recommend(product_name, topN=5):
    idx = indices.get(product_name)
    if idx is None:
        return []
    sim_scores = list(enumerate(cosine_sim[idx].tolist()[0]))
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)[1:topN+1]
    product_indices = [i[0] for i in sim_scores]
    return df['product_name'].iloc[product_indices].tolist()

# Sidebar
st.sidebar.header("Select a product to get recommendations")
product_list = df['product_name'].unique()
selected_product = st.sidebar.selectbox("Choose product:", product_list)

if st.sidebar.button("Recommend"):
    recs = recommend(selected_product)
    if recs:
        st.subheader(f"Top {len(recs)} recommendations for:")
        st.write(f"✅ **{selected_product}**")
        for i, prod in enumerate(recs, start=1):
            st.markdown(f"{i}. {prod}")
    else:
        st.warning("Product not found or no recommendations.")

st.markdown("---")
st.subheader("📦 Dataset Preview")
st.write(df.head())
