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
    "Changes in personality, behavior, or concentration"
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
    "Changes in personality, behavior, or concentration": "Brain Cancer"
}

# -------------------------------
# Streamlit UI
# -------------------------------
st.title("🧬 Cancer Symptom Checker")
st.write("Select the symptoms you are experiencing. After selecting, click 'Show Possible Cancer Types'.")

selected_symptoms = st.multiselect("Select your symptoms", all_symptoms)

# Prediction Logic
if st.button("🔍 Show Possible Cancer Types"):
    if not selected_symptoms:
        st.warning("Please select at least one symptom.")
    else:
        # Map selected symptoms to cancer types
        cancer_count = {}
        for s in selected_symptoms:
            c_type = symptom_to_cancer.get(s)
            if c_type:
                cancer_count[c_type] = cancer_count.get(c_type, 0) + 1
        
        if cancer_count:
            st.success("### Possible Cancer Types Based on Your Symptoms:")
            for cancer, count in sorted(cancer_count.items(), key=lambda x: x[1], reverse=True):
                st.write(f"- **{cancer}** (matching symptoms: {count})")
        else:
            st.info("No strong cancer indicators detected. Please consult a doctor if symptoms persist.")
