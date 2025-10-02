import streamlit as st

# -------------------------------
# Unified Symptom List
# -------------------------------
all_symptoms = [
    # Prostate
    "Frequent need to urinate, especially at night",
    "Difficulty urinating (hesitancy or interrupted flow)",
    "Weak or slow urine stream",
    "Pain or burning during urination",
    "Blood in urine or semen",
    "Painful ejaculation",
    "Pain in the back, hips, or pelvis that doesn't go away",

    # Lung
    "Persistent cough that gets worse or won't go away",
    "Coughing up blood or rust-colored sputum",
    "Shortness of breath or wheezing",
    "Chest pain worse with deep breathing, coughing, or laughing",
    "Hoarseness or a change in voice",
    "Unexplained weight loss",
    "Loss of appetite",
    "Constant fatigue",

    # Mouth
    "Sore, irritation, lump, or thick patch in mouth, lip, or throat that does not heal",
    "White or reddish patches in mouth",
    "Pain, tenderness, or numbness in mouth or lips",
    "Difficulty chewing or swallowing",
    "Feeling that something is caught in the throat",
    "Voice changes",

    # Pancreatic
    "Jaundice (yellowing of skin/eyes)",
    "Dark urine or light/greasy stools",
    "Abdominal or back pain",
    "Fatigue",
    "Nausea or vomiting",
    "New-onset diabetes",

    # Blood
    "Fever, chills, or night sweats",
    "Persistent fatigue or weakness",
    "Frequent or severe infections",
    "Easy bruising or bleeding",
    "Swollen lymph nodes",
    "Bone or joint pain",
    "Feeling full after eating very little",

    # Brain
    "New or changing headaches",
    "Seizures",
    "Nausea or vomiting",
    "Vision problems",
    "Gradual loss of sensation or movement in limb",
    "Difficulty with balance or walking",
    "Speech difficulties",
    "Changes in personality, behavior, or concentration",

    # Female-specific
    "Lump in breast",
    "Nipple discharge",
    "Breast pain",
    "Skin dimpling",
    "Change in breast size",
    "Abnormal bleeding",
    "Pelvic pain",
    "Pain during intercourse",
    "Foul-smelling discharge"
]

# -------------------------------
# Mapping Symptoms to Cancer Types
# -------------------------------
symptom_to_cancer = {
    # Prostate
    "Frequent need to urinate, especially at night": "Prostate Cancer",
    "Difficulty urinating (hesitancy or interrupted flow)": "Prostate Cancer",
    "Weak or slow urine stream": "Prostate Cancer",
    "Pain or burning during urination": "Prostate Cancer",
    "Blood in urine or semen": "Prostate Cancer",
    "Painful ejaculation": "Prostate Cancer",
    "Pain in the back, hips, or pelvis that doesn't go away": "Prostate Cancer",

    # Lung
    "Persistent cough that gets worse or won't go away": "Lung Cancer",
    "Coughing up blood or rust-colored sputum": "Lung Cancer",
    "Shortness of breath or wheezing": "Lung Cancer",
    "Chest pain worse with deep breathing, coughing, or laughing": "Lung Cancer",
    "Hoarseness or a change in voice": "Lung Cancer",
    "Unexplained weight loss": "Lung Cancer",
    "Loss of appetite": "Lung Cancer",
    "Constant fatigue": "Lung Cancer",

    # Mouth
    "Sore, irritation, lump, or thick patch in mouth, lip, or throat that does not heal": "Mouth Cancer",
    "White or reddish patches in mouth": "Mouth Cancer",
    "Pain, tenderness, or numbness in mouth or lips": "Mouth Cancer",
    "Difficulty chewing or swallowing": "Mouth Cancer",
    "Feeling that something is caught in the throat": "Mouth Cancer",
    "Voice changes": "Mouth Cancer",

    # Pancreatic
    "Jaundice (yellowing of skin/eyes)": "Pancreatic Cancer",
    "Dark urine or light/greasy stools": "Pancreatic Cancer",
    "Abdominal or back pain": "Pancreatic Cancer",
    "Fatigue": "Pancreatic Cancer",
    "Nausea or vomiting": "Pancreatic Cancer",
    "New-onset diabetes": "Pancreatic Cancer",

    # Blood
    "Fever, chills, or night sweats": "Blood Cancer",
    "Persistent fatigue or weakness": "Blood Cancer",
    "Frequent or severe infections": "Blood Cancer",
    "Easy bruising or bleeding": "Blood Cancer",
    "Swollen lymph nodes": "Blood Cancer",
    "Bone or joint pain": "Blood Cancer",
    "Feeling full after eating very little": "Blood Cancer",

    # Brain
    "New or changing headaches": "Brain Cancer",
    "Seizures": "Brain Cancer",
    "Nausea or vomiting": "Brain Cancer",
    "Vision problems": "Brain Cancer",
    "Gradual loss of sensation or movement in limb": "Brain Cancer",
    "Difficulty with balance or walking": "Brain Cancer",
    "Speech difficulties": "Brain Cancer",
    "Changes in personality, behavior, or concentration": "Brain Cancer",

    # Female-specific
    "Lump in breast": "Breast Cancer",
    "Nipple discharge": "Breast Cancer",
    "Breast pain": "Breast Cancer",
    "Skin dimpling": "Breast Cancer",
    "Change in breast size": "Breast Cancer",
    "Abnormal bleeding": "Cervical Cancer",
    "Pelvic pain": "Cervical Cancer",
    "Pain during intercourse": "Cervical Cancer",
    "Foul-smelling discharge": "Cervical Cancer"
}

# -------------------------------
# Streamlit UI
# -------------------------------
st.title("🧬 Cancer Symptom Checker")
st.write("Select your medical details and symptoms. The app will suggest possible cancer types.")

# User Info
age = st.number_input("Age", 1, 120)
gender = st.radio("Gender", ["Male", "Female"])
blood_pressure = st.radio("Do you have high blood pressure?", ["Yes", "No"])
diabetes = st.radio("Do you have diabetes?", ["Yes", "No"])
heart_issues = st.radio("Do you have any heart issues?", ["Yes", "No"])
family_history = st.radio("Any family history of cancer?", ["Yes", "No"])

# Show only relevant symptoms based on gender
if gender == "Male":
    filtered_symptoms = [s for s in all_symptoms if "breast" not in s.lower() and "cervical" not in s.lower() and "pelvic" not in s.lower()]
else:
    filtered_symptoms = all_symptoms

selected_symptoms = st.multiselect("Select your symptoms", filtered_symptoms)

# Prediction Logic
if st.button("🔍 Show Possible Cancer Types"):
    if not selected_symptoms:
        st.warning("Please select at least one symptom.")
    else:
        # Map symptoms to cancer types
        cancer_count = {}
        for s in selected_symptoms:
            c_type = symptom_to_cancer.get(s)
            if c_type:
                # Filter by gender-specific cancers
                if gender == "Male" and c_type in ["Breast Cancer", "Cervical Cancer"]:
                    continue
                cancer_count[c_type] = cancer_count.get(c_type, 0) + 1

        # Factor family history as increasing relevance
        if family_history == "Yes":
            for c in cancer_count:
                cancer_count[c] += 1  # simple weight

        if cancer_count:
            st.success("### Possible Cancer Types Based on Your Symptoms:")
            for cancer, count in sorted(cancer_count.items(), key=lambda x: x[1], reverse=True):
                st.write(f"- **{cancer}** (matching symptoms: {count})")
        else:
            st.info("No strong cancer indicators detected. Please consult a doctor if symptoms persist.")
