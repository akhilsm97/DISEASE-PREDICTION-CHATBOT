# train_model.py
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import accuracy_score
import joblib
import os

# Load dataset
csv_path = os.path.join('model_assets', 'symbipredict_cleaned.csv')
df = pd.read_csv(csv_path)

# Features and labels
X = df.drop('prognosis', axis=1)
y = df['prognosis']

# Encode target labels
le = LabelEncoder()
y_encoded = le.fit_transform(y)

# Train/test split
X_train, X_test, y_train, y_test = train_test_split(X, y_encoded, test_size=0.2, random_state=42)

# Train model
model = MultinomialNB()
model.fit(X_train, y_train)

# Evaluate
y_pred = model.predict(X_test)
print("Accuracy:", accuracy_score(y_test, y_pred))

# Save model and encoder
joblib.dump(model, os.path.join('model_assets', 'model.pkl'))
joblib.dump(le, os.path.join('model_assets', 'encoder.pkl'))
joblib.dump(list(X.columns), os.path.join('model_assets', 'symptoms.pkl'))
