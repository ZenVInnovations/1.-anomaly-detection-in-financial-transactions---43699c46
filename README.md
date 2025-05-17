# 💰 Anomaly Detection in Financial Transactions

## 📌 Objective
Implement AI-based models like Isolation Forest and Autoencoders to detect fraudulent transactions or anomalies in financial data. The project improves security and integrity of transactional systems.

---

## 🧭 Project Flow

1. ✅ **Phase 1: Research & Documentation**  
2. 📊 **Phase 2: Design** – Create system flowchart using draw.io  
3. 👨‍💻 **Phase 3: Development** – Code models and preprocessing  
4. 🧪 **Phase 4: Testing** – Evaluate models with various inputs  
5. 🚀 **Phase 5: Deployment** – Build UI in Streamlit and deploy to Streamlit Cloud  

---

## 📁 Folder Structure

```
anomaly-detection-financial-transactions/
├── __pycache__/
├── docs/
├── Financial Anomaly Detection Workflow.jpg
├── README.md
├── anomaly_detection.py
├── app.py
├── large_transactions.csv
├── output of large_transactions file.csv
├── output of transaction_anomalies file.csv
├── output of transactions file.csv
├── output of transactions_large file.csv
├── preprocess.py
├── requirements.txt
├── transaction_anomalies_dataset.csv
├── transactions.csv
├── transactions_large.csv
```

---

## 🧠 Models Used

- **Isolation Forest** – Tree-based anomaly detection  
- **Autoencoder** – Deep learning model for reconstruction error  

---

## 📊 Datasets

| Dataset | Link |
|--------|------|
| Credit Card Fraud Detection | [Kaggle Dataset](https://www.kaggle.com/mlg-ulb/creditcardfraud) |
| IEEE-CIS Fraud Detection | [Kaggle Competition](https://www.kaggle.com/c/ieee-fraud-detection) |

---

## 🛠️ Libraries

- `pandas`, `numpy`, `scikit-learn`  
- `tensorflow`, `keras`, `streamlit`  
- `matplotlib`, `seaborn`  

---

## 📦 Requirements

To install all the necessary dependencies, create a `requirements.txt` file with the following:

```
pandas==1.3.3
numpy==1.21.2
scikit-learn==0.24.2
tensorflow==2.6.0
keras==2.6.0
streamlit==0.88.0
matplotlib==3.4.3
seaborn==0.11.2
```

Alternatively, for Conda users:

```bash
conda create --name anomaly-detection python=3.8
conda activate anomaly-detection
conda install pandas numpy scikit-learn tensorflow keras streamlit matplotlib seaborn
```

---

## 🚀 Running the App

After setting up the environment, run the Streamlit app using:

```bash
streamlit run app.py
```

---

## 📜 Documentation

Detailed documentation can be found in the `docs/` folder:
- `overview.md`
- `anomaly_detection_methods.md`
- `dataset_description.md`
- `tools_and_libraries.md`
- `references.md`

---

## 📝 License

This project is licensed under the MIT License. See the `LICENSE.md` file for details.

---

## 🤝 Contributing

Feel free to fork this repository, create a feature branch, and submit a pull request.

---

## 🙋‍♂️ Acknowledgements

- Kaggle for open datasets  
- Developers of the open-source ML/AI libraries  
- Community and educational content that inspired the solution
