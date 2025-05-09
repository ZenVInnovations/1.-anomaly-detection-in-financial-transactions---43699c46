# 🧠 Anomaly Detection Methods

## 1. Isolation Forest
- An unsupervised algorithm that isolates anomalies.
- Based on randomly selecting features and splitting values.
- Anomalies are more susceptible to isolation and appear in shorter paths.

**Pros:**
- Efficient with high-dimensional data.
- Works well without labeled data.

---

## 2. Autoencoders
- A neural network that learns to compress and reconstruct input data.
- High reconstruction error indicates anomalies.
- Useful for detecting subtle and non-linear anomalies.

**Architecture:**
- Encoder → Bottleneck → Decoder
- Loss = Mean Squared Error (Input vs Reconstructed Output)
