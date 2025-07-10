# 🛍️ Product Recommendation System

![Streamlit](https://img.shields.io/badge/Streamlit-Dashboard-orange?logo=streamlit)
![Python](https://img.shields.io/badge/Python-3.8+-blue?logo=python)
![License](https://img.shields.io/badge/license-MIT-green)

A simple content-based product recommendation system built with Python, scikit-learn, and Streamlit.  
This dashboard shows similar products based on product names, and lets users interactively explore recommendations.

---

## ✨ **Features**
- Upload / explore product dataset
- Build a content-based recommender (TF-IDF + cosine similarity)
- Streamlit dashboard to:
  - Browse dataset
  - Select a product
  - See top 5 recommended similar products

---

## 📂 **Project Structure**
├── app.py # Streamlit dashboard
├── Project2_Main_Local.ipynb # Local notebook (builds model & EDA)
├── requirements.txt # Dependencies
├── data/
│ └── Products_dataset.csv # Product dataset
├── models/
│ └── recommender_model.pkl # Saved model
└── plots/ # EDA plots (optional)
