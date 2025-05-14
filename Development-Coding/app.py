import streamlit as st
from utils import load_data
from model import train_model, detect_anomalies

st.title("Anomaly Detection in Financial Transactions")

uploaded_file = st.file_uploader("Upload a CSV file", type=["csv"])

if uploaded_file:
    try:
        df = load_data(uploaded_file)
        st.write("Sample Data:")
        st.write(df.head())

        numeric_df = df.select_dtypes(include=['float64', 'int64'])
        if numeric_df.empty:
            st.error("No numeric data found for training.")
        else:
            model = train_model(numeric_df)
            results = detect_anomalies(model, numeric_df)
            df['Anomaly'] = results['anomaly']
            st.subheader("Anomaly Detection Result")
            st.write(df)
    except Exception as e:
        st.error(f"Error: {e}")
