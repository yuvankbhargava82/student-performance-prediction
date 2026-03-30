# 🎓 Student Performance Prediction using AI/ML

Ever wondered how factors like study time, attendance, sleep, and past performance affect your exam results?

This project is a simple yet powerful **Machine Learning application** that predicts a student's score based on these real-life factors. It’s designed to demonstrate how AI can be used in education to better understand and improve student outcomes.

---

## 🌟 Why this Project?

As students, we often ask:

* *“Am I studying enough?”*
* *“Does sleep really affect my performance?”*
* *“How much does attendance matter?”*

This project tries to answer those questions using **data and machine learning**.

---

## 📌 What This Project Does

It builds a prediction model using:

* 📖 Study Hours
* 🏫 Attendance
* 😴 Sleep Hours
* 📊 Previous Scores

👉 Based on these inputs, it predicts your expected exam score.

---

## 🚀 Key Features

✔ Generates realistic student data using NumPy
✔ Trains a Machine Learning model (Linear Regression)
✔ Evaluates performance using MAE and R²
✔ Interactive command-line interface
✔ Input validation to avoid errors
✔ Continuous prediction loop for multiple users

---

## 🧠 How the Model Works

We use **Linear Regression**, one of the simplest and most interpretable ML algorithms.

The model learns relationships like:

* More study hours → better score 📈
* Better attendance → higher performance 🎯
* Proper sleep → improved focus 😴

### Conceptual Formula:

```
score = (1.8 × study_hours) + (0.7 × attendance) + 
        (1.0 × sleep_hours) + (0.5 × previous_score) + noise
```

👉 This is not just random — it simulates realistic academic behavior.

---

## 📂 Project Structure

```
student-performance-prediction/
│
├── main.py          # Main program
├── README.md        # Documentation
```

---

## ⚙️ Setup Instructions

### 1️⃣ Clone the Repository

```
git clone https://github.com/your-username/student-performance-prediction.git
cd student-performance-prediction
```

---

### 2️⃣ Install Required Libraries

Make sure Python (3.7 or above) is installed, then run:

```
pip install pandas numpy scikit-learn
```

---

## ▶️ How to Run

Simply run:

```
python main.py
```

---

## 💻 Example Interaction

```
Enter study hours per day: 5
Enter attendance percentage: 85
Enter sleep hours per day: 7
Enter previous exam score: 70

Predicted Score: 82.45
```

You can keep predicting for multiple inputs — super interactive!

---

## 📊 Model Performance

The model gives you:

* **Mean Absolute Error (MAE):**
  → Average prediction error

* **R² Score:**
  → How well the model explains the data

Example:

```
Mean Absolute Error: 2.45
R² Score: 0.95
```

👉 That means the model is quite accurate!

---

## ✅ Input Guidelines

| Input          | Range   |
| -------------- | ------- |
| Study Hours    | 0 – 24  |
| Attendance (%) | 0 – 100 |
| Sleep Hours    | 0 – 24  |
| Previous Score | 0 – 100 |

---

## 🔍 Behind the Scenes

Here’s what happens step-by-step:

1. Synthetic data is generated
2. Data is split into training & testing sets
3. Model is trained on training data
4. Performance is evaluated
5. Model is retrained on full data
6. User inputs are used for prediction

---

## 🔮 Future Improvements

This project can be taken much further:

* 🌐 Build a web app using Streamlit or Flask
* 📊 Add graphs & visualizations
* 📁 Use real-world datasets
* 🤖 Try advanced models (Random Forest, XGBoost)
* 💾 Save & reuse trained models

---

## 🤝 Contributing

Want to improve this project? Awesome!

You can:

* Fork the repository
* Make improvements
* Submit a pull request

## 🙌 Acknowledgements

Big thanks to:

* The open-source community
* Libraries like Pandas, NumPy, and Scikit-learn
* Everyone exploring AI in education

---

## ⭐ Show Your Support

If you found this project helpful or interesting:

👉 Give it a ⭐ on GitHub — it really helps!

---

## 👨‍💻 Author

**Yuvank Bhargava**
🔗 GitHub: https://github.com/yuvankbhargava82

---

> 💡 *Small habits create big results — and now, you can predict them too!*
