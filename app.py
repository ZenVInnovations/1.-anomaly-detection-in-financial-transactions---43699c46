import streamlit as st
import pandas as pd
from preprocess import preprocess_data
from sklearn.ensemble import IsolationForest

st.title("Anomaly Detection in Financial Transactions")

uploaded_file = st.file_uploader("Upload transaction CSV", type=["csv"])

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    st.subheader("Uploaded Data")
    st.write(df.head())

    data = preprocess_data(df)

    model = IsolationForest(contamination=0.05)
    model.fit(data)
    df["anomaly"] = model.predict(data)

    df["anomaly"] = df["anomaly"].map({1: "Normal", -1: "Anomaly"})

    st.subheader("Anomaly Detection Results")
    st.write(df)

    st.download_button("Download Results", df.to_csv(index=False), "labeled_transactions.csv")