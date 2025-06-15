# 🩺 Disease Prediction through Symptoms

This is an AI-powered web application built with **Streamlit** that predicts possible diseases based on selected symptoms and provides precautionary advice and descriptions.

<br>

---

## 🔍 Features

- ✅ Predict disease from selected symptoms using a trained ML model.
- 💊 Suggests precautions for the predicted disease.
- 📖 Displays a short description of each selected symptom.
- ⚠️ Calculates severity score based on symptom weights.
- 🎨 Clean, modern, and interactive UI powered by Streamlit.

---

## 🧠 How It Works

- **Input**: User selects multiple symptoms.
- **Model**: A `RandomForestClassifier` trained on a synthetic dataset predicts the most probable disease.
- **Output**:
  - Predicted disease
  - Symptom descriptions
  - Precautionary steps
  - Severity score

---

## 📁 Project Structure

├── app.py # Streamlit app code
├── model.pkl # Trained ML model
├── label_encoder.pkl # Label encoder for diseases
├── symptom_list.pkl # List of symptoms used in training
├── symptom-severity.csv # Severity scores for symptoms
├── symptom_precaution.csv # Precautions for each disease
├── symptom_Description.csv # Descriptions for each disease
└── README.md # Project documentation

