
import pandas as pd
import numpy as np
from sklearn.ensemble import IsolationForest
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report
import tensorflow as tf
from tensorflow.keras.models import Model
from tensorflow.keras.layers import Input, Dense
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset
df = pd.read_csv("/content/creditcard.csv")

# Display first few rows
print(df.head())

# Preprocessing
df = df.dropna()
y_true = df['Class']
X = df.drop(columns=['Class'])

scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# ---- Isolation Forest ----
iso_forest = IsolationForest(contamination=0.0017, random_state=42)
iso_preds = iso_forest.fit_predict(X_scaled)
iso_preds = np.where(iso_preds == -1, 1, 0)

# ---- Autoencoder ----
X_train, X_test = train_test_split(X_scaled, test_size=0.2, random_state=42)

input_dim = X_train.shape[1]
encoding_dim = input_dim // 2

input_layer = Input(shape=(input_dim,))
encoded = Dense(encoding_dim, activation="relu")(input_layer)
decoded = Dense(input_dim, activation="linear")(encoded)

autoencoder = Model(input_layer, decoded)
autoencoder.compile(optimizer='adam', loss='mse')

autoencoder.fit(X_train, X_train,
                epochs=10,
                batch_size=32,
                shuffle=True,
                validation_data=(X_test, X_test),
                verbose=1)

# Compute reconstruction error
X_pred = autoencoder.predict(X_scaled)
mse = np.mean(np.power(X_scaled - X_pred, 2), axis=1)
threshold = np.percentile(mse, 99.83)  # ~0.17% fraud
ae_preds = (mse > threshold).astype(int)

# ---- Evaluation ----
print("Isolation Forest Report:")
print(classification_report(y_true, iso_preds))

print("\nAutoencoder Report:")
print(classification_report(y_true, ae_preds))

# ---- Visualization ----
plt.figure(figsize=(10, 5))
sns.histplot(mse, bins=100, kde=True)
plt.axvline(threshold, color='r', linestyle='--', label='Threshold')
plt.title('Autoencoder Reconstruction Error')
plt.legend()
plt.show()
=======
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

