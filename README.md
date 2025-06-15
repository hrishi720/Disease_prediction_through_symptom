# 📊 AI-Based Disease Prediction App

An intelligent and interactive web app that predicts diseases based on user-selected symptoms and provides relevant medical information like precautions and severity. Powered by **Machine Learning**, styled with a smooth **UI**, and deployed with ease.

> ✅ Built with **Python**, **Scikit-learn**, and **Streamlit**

---

### 🚀 Features

* 🔍 Predict disease from multiple symptoms
* 💬 Auto-display descriptions for selected symptoms
* 💊 Shows precautions for detected disease
* ⚠️ Severity score calculated using symptom weights
* 🎨 Responsive, clean UI (Streamlit powered)

---

### 📂 Files & Structure

```
├── app.py                    # Streamlit app logic
├── model.pkl                # Trained RandomForest model
├── label_encoder.pkl        # Encoded disease labels
├── symptom_list.pkl         # List of trained symptoms
├── symptom-severity.csv     # Weight data for symptoms
├── symptom_precaution.csv   # Precautions for diseases
├── symptom_Description.csv  # Description for diseases
└── README.md                # This file
```

---

### 🛠️ How to Run Locally

1. **Clone the Repo**

```bash
git clone https://github.com/hrishi720/Disease_prediction_through_symptom.git
cd Disease_prediction_through_symptom
```

2. **Install Requirements**

```bash
pip install -r requirements.txt
```

3. **Run the App**

```bash
streamlit run app.py
```

---

### 🌐 Live Deployment (Free)

Deployed using **Streamlit Cloud**:
🔗 [Check Live App](https://diseasepredictionthroughsymptom-bft8cappl2epu9vwy3tyt5x.streamlit.app/)

---

### 🧠 Tech Stack

* Python
* Pandas
* Scikit-learn
* Streamlit
* Pickle

---

### 🤛‍♂️ Author

Made with ❤️ by **Hrishi**

* 🌐 GitHub: [@hrishi720](https://github.com/hrishi720)

---

### 📄 License

This project is open source under the [MIT License](LICENSE).
