# ❤️ Heart Disease Prediction Web App

A full-stack **Machine Learning web application** that predicts the likelihood of heart disease using clinical patient data. The model is trained using scikit-learn and deployed with Flask, featuring a clean user interface and record management system.

---

## 🚀 Live Demo
👉 (Add your deployed link here after deploying)

---

## 📌 Features

- 🔍 Predicts heart disease based on medical inputs
- 🧠 Trained using Machine Learning (scikit-learn)
- 🌐 Web interface built with Flask
- 🎨 Clean and responsive UI (Bootstrap)
- 🗄️ Stores prediction records (SQLite database)
- 📊 View and manage past predictions
- ☁️ Cloud deployment ready

---

## 🧠 Machine Learning Details

- **Dataset**: Heart Disease Dataset (303 samples, 13 features)
- **Algorithms Used**:
  - Logistic Regression
  - Support Vector Machine (SVM)
  - Random Forest (selected for deployment)
- **Preprocessing**:
  - Train-test split (80:20)
  - Feature scaling using StandardScaler
- **Model Persistence**:
  - Saved using `joblib`

---

## 🧾 Input Features

- Age  
- Sex  
- Chest Pain Type (cp)  
- Resting Blood Pressure (trestbps)  
- Cholesterol (chol)  
- Fasting Blood Sugar (fbs)  
- Resting ECG (restecg)  
- Max Heart Rate (thalach)  
- Exercise Induced Angina (exang)  
- Oldpeak  
- Slope  
- CA  
- Thal  

---

## 🛠️ Tech Stack

- **Frontend**: HTML, CSS, Bootstrap  
- **Backend**: Flask  
- **Machine Learning**: scikit-learn  
- **Database**: SQLite  
- **Deployment**: Render  

---

## 📂 Project Structure

MiniProject/
│── app.py
│── model.pkl
│── scaler.pkl
│── requirements.txt
│── records.db
│
└── templates/
│── index.html
│── records.html


---

## ⚙️ Installation & Setup

### 1. Clone the repository

---

### 2. Create virtual environment

---

### 3. Install dependencies

---

### 4. Run the app

Open in browser:http://127.0.0.1:5000/

---

## ☁️ Deployment (Render)

1. Push code to GitHub  
2. Go to Render → New Web Service  
3. Connect repository  
4. Use:
   - **Build Command**: `pip install -r requirements.txt`
   - **Start Command**: `gunicorn app:app`  

---

## 📊 Future Enhancements

- 🔐 User authentication system  
- 📈 Data visualization dashboard  
- 📱 Mobile-friendly UI improvements  
- 🤖 Model improvement with larger dataset  

---

## 🎯 Conclusion

This project demonstrates how Machine Learning models can be integrated into a real-world web application for healthcare prediction. It combines data science, backend development, and deployment into a single end-to-end solution.

---

## 👨‍💻 Author

- Khushboo Kushwaha  
- (https://github.com/khushboo184)

---

## ⭐ If you like this project

Give it a star ⭐ on GitHub!
