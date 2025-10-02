import streamlit as st

st.title("Cancer Symptom Checker")
st.write("Get possible cancer risks based on age, gender, history, location, and symptoms.")

# ---- Patient Info ----
name = st.text_input("Name")
age = st.number_input("Age", min_value=1, max_value=120)
gender = st.selectbox("Gender", ["Male", "Female", "Other"])
location = st.text_input("City / Location")
family_history = st.selectbox("Family history of cancer?", ["No", "Yes", "Don't know"])
bp = st.checkbox("High Blood Pressure")
diabetes = st.checkbox("Diabetes")
heart = st.checkbox("Heart Issues")

st.markdown("---")

# ---- Symptoms by Gender ----
st.header("Select Symptoms")

symptoms = []

# ----- Male-specific cancers -----
if gender == "Male":
    st.subheader("Male-specific cancers")

    with st.expander("Prostate Cancer"):
        if st.checkbox("Frequent urination, especially at night"): symptoms.append("prostate")
        if st.checkbox("Difficulty urinating / weak stream"): symptoms.append("prostate")
        if st.checkbox("Blood in urine or semen"): symptoms.append("prostate")
        if st.checkbox("Pelvic/back pain"): symptoms.append("prostate")

    with st.expander("Mouth Cancer"):
        if st.checkbox("Non-healing mouth sore"): symptoms.append("mouth")
        if st.checkbox("White/red patches in mouth"): symptoms.append("mouth")
        if st.checkbox("Difficulty swallowing"): symptoms.append("mouth")
        if st.checkbox("Voice changes / throat lump"): symptoms.append("mouth")

# ----- Female-specific cancers -----
if gender == "Female":
    st.subheader("Female-specific cancers")

    with st.expander("Breast Cancer"):
        if st.checkbox("Breast lump or thickening"): symptoms.append("breast")
        if st.checkbox("Change in breast size or shape"): symptoms.append("breast")
        if st.checkbox("Nipple discharge or bleeding"): symptoms.append("breast")
        if st.checkbox("Skin dimpling or redness on breast"): symptoms.append("breast")

    with st.expander("Cervical Cancer"):
        if st.checkbox("Abnormal vaginal bleeding or discharge"): symptoms.append("cervical")
        if st.checkbox("Pelvic pain"): symptoms.append("cervical")
        if st.checkbox("Pain during intercourse"): symptoms.append("cervical")

    with st.expander("Ovarian Cancer"):
        if st.checkbox("Abdominal bloating or swelling"): symptoms.append("ovarian")
        if st.checkbox("Feeling full quickly when eating"): symptoms.append("ovarian")
        if st.checkbox("Frequent urination"): symptoms.append("ovarian")
        if st.checkbox("Pelvic pain or pressure"): symptoms.append("ovarian")

# ----- Common to both genders -----
st.subheader("Cancers common to all genders")

with st.expander("Lung Cancer"):
    if st.checkbox("Persistent cough / worsening cough"): symptoms.append("lung")
    if st.checkbox("Coughing up blood"): symptoms.append("lung")
    if st.checkbox("Shortness of breath / wheezing"): symptoms.append("lung")
    if st.checkbox("Chest pain"): symptoms.append("lung")
    if st.checkbox("Hoarseness / voice change"): symptoms.append("lung")

with st.expander("Pancreatic Cancer"):
    if st.checkbox("Jaundice (yellow skin/eyes)"): symptoms.append("pancreatic")
    if st.checkbox("Abdominal/back pain"): symptoms.append("pancreatic")
    if st.checkbox("Unexplained weight loss"): symptoms.append("pancreatic")
    if st.checkbox("New diabetes onset"): symptoms.append("pancreatic")

with st.expander("Blood Cancer"):
    if st.checkbox("Night sweats / fever / chills"): symptoms.append("blood")
    if st.checkbox("Frequent infections"): symptoms.append("blood")
    if st.checkbox("Easy bruising/bleeding"): symptoms.append("blood")
    if st.checkbox("Swollen lymph nodes"): symptoms.append("blood")
    if st.checkbox("Bone pain"): symptoms.append("blood")

with st.expander("Brain Cancer"):
    if st.checkbox("Frequent/worsening headaches"): symptoms.append("brain")
    if st.checkbox("Seizures"): symptoms.append("brain")
    if st.checkbox("Vision problems"): symptoms.append("brain")
    if st.checkbox("Balance/coordination issues"): symptoms.append("brain")
    if st.checkbox("Personality or memory changes"): symptoms.append("brain")

# ---- Risk Calculation ----
def predict_cancer(symptoms, age, gender, family_history, location):
    cancer_count = {}
    for s in symptoms:
        cancer_count[s] = cancer_count.get(s, 0) + 1

    # Add modifiers
    risk_score = 0
    if age > 50: risk_score += 1
    if family_history == "Yes": risk_score += 2
    if "delhi" in location.lower() or "kanpur" in location.lower():
        risk_score += 1  # polluted cities
    if any(x in location.lower() for x in ["varanasi","patna","kolkata","lucknow"]):
        risk_score += 1  # ganga belt risk

    return cancer_count, risk_score

if st.button("Predict Possible Cancer Type"):
    cancers, score = predict_cancer(symptoms, age, gender, family_history, location)
    
    if not cancers:
        st.warning("No significant cancer-related symptoms selected.")
    else:
        st.subheader(f"Prediction for {name}")
        st.write("### Possible Cancer Types (based on symptoms):")
        for c, count in sorted(cancers.items(), key=lambda x: x[1], reverse=True):
            st.write(f"- {c.capitalize()} (symptom matches: {count})")
        
        if score <= 2: risk = "Low Risk"
        elif score <= 4: risk = "Medium Risk"
        else: risk = "High Risk"
        
        st.success(f"Overall Risk Level: {risk}")
