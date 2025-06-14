import streamlit as st
import pandas as pd
import pickle

# --- Load model and encoders ---
with open("model.pkl", "rb") as f:
    model = pickle.load(f)

with open("label_encoder.pkl", "rb") as f:
    le = pickle.load(f)

with open("symptom_list.pkl", "rb") as f:
    symptoms = pickle.load(f)

# --- Load disease-based description and precaution data ---
desc_df = pd.read_csv("symptom_Description.csv")  # contains disease descriptions
precaution_df = pd.read_csv("symptom_precaution.csv")  # contains disease precautions
severity_df = pd.read_csv("symptom-severity.csv")  # still symptom-based severity

# --- Utility functions ---
def predict_disease(selected_symptoms):
    input_vec = [1 if s in [x.lower().strip() for x in selected_symptoms] else 0 for s in symptoms]
    prediction = model.predict([input_vec])[0]
    return le.inverse_transform([prediction])[0]

def get_disease_description(disease):
    row = desc_df[desc_df["Disease"].str.lower() == disease.lower()]
    return row["Description"].values[0] if not row.empty else "No description available."

def get_precautions(disease):
    row = precaution_df[precaution_df["Disease"].str.lower() == disease.lower()]
    return row.iloc[0, 1:].dropna().tolist() if not row.empty else []

def get_severity_score(selected_symptoms):
    total = 0
    for s in selected_symptoms:
        row = severity_df[severity_df["Symptom"].str.lower() == s.lower()]
        if not row.empty:
            total += row["weight"].values[0]
    return total

# --- Streamlit App ---
st.set_page_config(page_title="Medical Symptom Checker", layout="centered")

# --- Styling ---
st.markdown("""
    <style>
        body {
            background: linear-gradient(to right, #f8f9fa, #e3f2fd);
            color: #212529;
        }
        .main-header {
            font-size: 2.8em;
            font-weight: bold;
            text-align: center;
            color: #0d6efd;
            margin-bottom: 10px;
        }
        .footer {
            position: fixed;
            bottom: 0;
            width: 100%;
            color: #adb5bd;
            text-align: center;
            font-size: 0.75em;
            padding: 8px;
        }
        .stButton>button {
            background-color: #0d6efd;
            color: white;
            font-weight: 600;
            border-radius: 10px;
            padding: 0.5em 1.5em;
            font-size: 1.05em;
            transition: 0.3s;
        }
        .stButton>button:hover {
            background-color: #0b5ed7;
        }
    </style>
    <div class="main-header">🩺 Medical Symptom Checker</div>
""", unsafe_allow_html=True)

# --- Input ---
st.markdown("### 🤒 Select your symptoms:")
selected = st.multiselect("Symptoms", symptoms)

# --- Prediction ---
if st.button("🔍 Predict Disease"):
    if not selected:
        st.warning("⚠️ Please select at least one symptom.")
    else:
        disease = predict_disease(selected)
        st.success(f"🧾 **Predicted Disease:** {disease}")

        # Disease Description
        st.markdown("### 🧬 Disease Description")
        st.info(get_disease_description(disease))

        # Precautions
        st.markdown("### 💊 Suggested Precautions")
        precautions = get_precautions(disease)
        if precautions:
            for p in precautions:
                st.markdown(f"🔹 {p}")
        else:
            st.write("No precautions found.")

        # Severity
        severity_score = get_severity_score(selected)
        st.markdown("### ⚠️ Severity Score")
        st.code(f"{severity_score} — Higher means more serious condition.")

# --- Footer ---
st.markdown('<div class="footer">Made with ❤️ by Hrishi</div>', unsafe_allow_html=True)
