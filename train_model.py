import pandas as pd
from sklearn.svm import SVC
import pickle
import os

# Load dataset
data = pd.read_csv("data.csv")

# Remove first column (Date column)
data = data.iloc[:, 1:]

# Check column count
print("Columns:", data.columns)
print("Feature count:", data.shape[1])

# Create Risk column
risk = data.sum(axis=1)
risk = risk.apply(lambda x: 1 if x > 500 else 0)

# Features
X = data

# Target
y = risk

# Train model
model = SVC(kernel='linear')
model.fit(X, y)

# Save model
os.makedirs("model", exist_ok=True)
pickle.dump(model, open("model/disease_model.pkl", "wb"))

print("Model Saved Successfully")