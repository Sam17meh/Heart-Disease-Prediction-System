❤️ Heart Disease Prediction System

A complete **Flask-based Machine Learning web application** that predicts the risk of heart disease based on medical parameters. The project includes **user authentication**, **dashboard**, **prediction history-ready structure**, and a **modern UI with Light/Dark mode**.

---

🚀 Features

* 🔐 User Authentication (Signup / Login / Logout)
* 🫀 Heart Disease Prediction using ML model
* 📊 Risk Probability Calculation
* 🌗 Light & Dark Mode Toggle
* 📱 Responsive & Clean UI
* 🧠 Trained ML model using real medical dataset
* 🧩 Modular Flask Blueprint Structure

---

🗂️ Project Structure

```
heart-disease-prediction/
│
├── app/
│   ├── __init__.py          # App factory & model loading
│   ├── routes.py            # Main routes (dashboard, prediction)
│   ├── auth.py              # Authentication logic
│   ├── models.py            # Database helpers
│   ├── templates/           # HTML templates
│   │   ├── base.html
│   │   ├── login.html
│   │   ├── signup.html
│   │   ├── dashboard.html
│   │   ├── predict.html
│   │   └── result.html
│   └── static/
│       ├── css/style.css    # App styling
│       └── js/theme.js      # Light/Dark mode
│
├── data/
│   └── Medicaldataset.csv   # Dataset used for training
│
├── heart_model.pkl          # Trained ML model
├── train_model.py           # Model training script
├── app.py                   # App entry point
├── users.db                 # SQLite database
├── requirements.txt         # Dependencies
└── README.md
```

---

🧠 Machine Learning Model

* **Algorithm:** Logistic Regression / RandomForest (depending on training)

* **Input Features:**

  * Age
  * Gender
  * Heart Rate
  * Systolic BP
  * Diastolic BP
  * Blood Sugar
  * CK-MB
  * Troponin

* **Output:**

  * Risk Level (High / Low)
  * Probability Percentage

---

📦 Installation & Setup

1️⃣ Clone Repository

```bash
git clone https://github.com/misha22-code/heart-disease-prediction.git
cd heart-disease-prediction
```

2️⃣ Create Virtual Environment

```bash
python -m venv venv
```

3️⃣ Activate Virtual Environment

**Windows:**

```bash
venv\Scripts\activate
```

**Mac/Linux:**

```bash
source venv/bin/activate
```

4️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

🧪 Train the Model (Optional)

If you want to retrain the model:

```bash
python train_model.py
```

This will generate `heart_model.pkl`.

---

▶️ Run the Application

```bash
python app.py
```

Open browser:

```
http://127.0.0.1:5000
```

---

🎨 UI Highlights

* Modern card-based layout
* Dark mode toggle 🌙
* Clean navbar and dashboard
* Responsive on mobile

---

🛠️ Tech Stack

* **Frontend:** HTML, CSS, JavaScript
* **Backend:** Flask (Python)
* **ML:** Scikit-learn, NumPy, Pandas
* **Database:** SQLite

---

🔮 Future Improvements

* 📈 Prediction History Page
* 📊 Graphs & Analytics
* 👩‍⚕️ Doctor/Admin Panel
* ☁️ Deployment (Render / Railway)

---

👩‍💻 Author

**Misha Noor**
Flutter & Android Developer → AI & Machine Learning
Python | Flask | ML

🔗 GitHub: [https://github.com/misha22-code](https://github.com/misha22-code)

---

⭐ If you like this project, don’t forget to **star** the repository!
