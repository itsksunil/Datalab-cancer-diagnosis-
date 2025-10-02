import streamlit as st

st.title("Cancer Risk Prediction App")
st.subheader("Symptom & Health Data Diagnosis Lab")

# ---- User Info ----
st.header("Patient Information")
name = st.text_input("Name")
age = st.number_input("Age", min_value=1, max_value=120, step=1)
gender = st.selectbox("Gender", ["Male", "Female", "Other"])
bp = st.checkbox("High Blood Pressure")
diabetes = st.checkbox("Diabetes")
heart = st.checkbox("Heart Issues")

# ---- Family History ----
family_history = st.selectbox(
    "Has anyone in your family (parents, grandparents, siblings) had cancer?",
    ["No", "Yes", "Don't know"]
)

# ---- Symptoms ----
st.header("Select Symptoms")
symptoms = {
    "Fatigue": st.checkbox("Fatigue / extreme tiredness"),
    "WeightChange": st.checkbox("Unexplained weight loss/gain"),
    "EatingProblems": st.checkbox("Eating problems (loss of appetite, nausea, belly pain)"),
    "Swelling": st.checkbox("Swelling or lumps anywhere"),
    "BreastLump": st.checkbox("Thickening or lump in breast/other body part"),
    "Pain": st.checkbox("Unexplained pain"),
    "SkinChanges": st.checkbox("Skin changes / mole changes / jaundice"),
    "Cough": st.checkbox("Cough or hoarseness that doesn’t go away"),
    "Bleeding": st.checkbox("Unusual bleeding or bruising"),
    "BowelChange": st.checkbox("Change in bowel habits"),
    "BloodStool": st.checkbox("Blood in stool"),
    "Bladder": st.checkbox("Bladder changes / pain while urinating"),
    "Fever": st.checkbox("Fever or night sweats"),
    "Headache": st.checkbox("Frequent headaches"),
    "VisionHearing": st.checkbox("Vision or hearing problems"),
    "MouthChanges": st.checkbox("Mouth sores, bleeding, pain or numbness")
}

# ---- Prediction Logic ----
def calculate_risk(symptoms, age, bp, diabetes, heart, family_history):
    score = 0
    for s, val in symptoms.items():
        if val:
            score += 1
    
    # medical history
    if bp: score += 1
    if diabetes: score += 1
    if heart: score += 1
    
    # age factor
    if age > 50:
        score += 1
    
    # family history factor
    if family_history == "Yes":
        score += 2
    elif family_history == "Don't know":
        score += 1

    # classify risk
    if score <= 3:
        return "Low Risk"
    elif score <= 6:
        return "Medium Risk"
    else:
        return "High Risk"

# ---- Button ----
if st.button("Predict Cancer Risk"):
    risk = calculate_risk(symptoms, age, bp, diabetes, heart, family_history)
    st.success(f"Prediction for {name}: {risk}")
