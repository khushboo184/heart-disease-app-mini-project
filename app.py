from flask import Flask, request, render_template, redirect
import numpy as np
import joblib
import sqlite3
from datetime import datetime

app = Flask(__name__)

model = joblib.load("model.pkl")
scaler = joblib.load("scaler.pkl")

# Create DB
def init_db():
    conn = sqlite3.connect("records.db")
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS records
                 (id INTEGER PRIMARY KEY AUTOINCREMENT,
                  date TEXT,
                  name TEXT,
                  features TEXT,
                  result TEXT)''')
    conn.commit()
    conn.close()

init_db()

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():
    form_data = request.form.to_dict()
    name = form_data.pop("name")

    features = [float(x) for x in form_data.values()]
    final = np.array(features).reshape(1, -1)
    scaled = scaler.transform(final)

    prediction = model.predict(scaled)[0]
    result = "Heart Disease ❌" if prediction == 1 else "No Disease ✅"

    # Save to DB
    conn = sqlite3.connect("records.db")
    c = conn.cursor()
    c.execute("INSERT INTO records (date, name, features, result) VALUES (?, ?, ?, ?)",
              (datetime.now(), name, str(features), result))
    conn.commit()
    conn.close()

    return render_template("index.html", prediction_text=f"{name}: {result}")

@app.route("/records")
def records():
    conn = sqlite3.connect("records.db")
    c = conn.cursor()
    c.execute("SELECT * FROM records")
    data = c.fetchall()
    conn.close()

    return render_template("records.html", records=data)

@app.route("/delete/<int:id>")
def delete(id):
    conn = sqlite3.connect("records.db")
    c = conn.cursor()
    c.execute("DELETE FROM records WHERE id=?", (id,))
    conn.commit()
    conn.close()
    return redirect("/records")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)