from sklearn.ensemble import IsolationForest
import pandas as pd

def train_model(data, contamination=0.05):
    model = IsolationForest(contamination=contamination, random_state=42)
    model.fit(data)
    return model

def detect_anomalies(model, data):
    data['anomaly'] = model.predict(data)
    data['anomaly'] = data['anomaly'].map({1: 'Normal', -1: 'Anomaly'})
    return data
