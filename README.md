# 🧠 Disease Prediction Chatbot

A dynamic chatbot built with **Django**, **jQuery**, and **Machine Learning** that interacts with users to collect symptom data and predicts the likely disease using a trained ML model.

---

## 🚀 Features

- ✅ WhatsApp-style chatbot UI
- ✅ Dynamic symptom-based questioning
- ✅ Disease prediction using trained ML model
- ✅ Built with Django, SQLite, and Scikit-learn
- ✅ Frontend using HTML, CSS, JavaScript, Bootstrap, and jQuery

---

## 🛠️ Tech Stack

- **Frontend:** HTML, CSS, JavaScript, Bootstrap, jQuery  
- **Backend:** Python, Django  
- **Database:** SQLite  
- **ML:** Scikit-learn (Naive Bayes), Joblib  
- **Dataset:** Provided CSV (`symbipredict_cleaned.csv`)

---

## 📁 Project Structure

disease_chatbot_project/
├── disease_chatbot/               # Django Project
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── chatbot/                       # Django App
│   ├── __init__.py
│   ├── views.py
│   ├── urls.py
│   ├── questions.py
│   └── templates/
│       └── chatbot/
│           └── chat.html
├── model_assets/
│   ├── symbipredict_cleaned.csv
│   ├── model.pkl        ← generated after running train_model.py
│   └── encoder.pkl      ← generated after running train_model.py
├── train_model.py
├── manage.py
└── db.sqlite3             ← (will be created after migrations)




---

## ⚙️ Setup Instructions

### 1. 🔧 Clone & Install Dependencies

git clone https://github.com/akhilsm97/DISEASE-PREDICTION-CHATBOT.git
cd disease_chatbot
pip install -r requirements.txt

### 2. 🔧 Train Model (Optional)

python train_model.py

### 3.⚙️ Apply Migrations

python manage.py migrate

### 4. 🧪 Run Development Server

python manage.py runserver



### 🧠 Model Details

Algorithm: Multinomial Naive Bayes

Training Accuracy: ~96.7%

Input Features: Binary symptom flags

Output: Encoded disease prediction





