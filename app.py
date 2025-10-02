import streamlit as st
from fpdf import FPDF

# -------------------------------
# Cancer Symptoms Database
# -------------------------------
male_cancers = {
    "Prostate Cancer": [
        "Frequent urination", "Difficulty urinating", "Blood in urine", "Painful ejaculation", "Pelvic pain"
    ],
    "Lung Cancer": [
        "Persistent cough", "Coughing up blood", "Shortness of breath", "Chest pain", "Hoarseness", "Unexplained weight loss"
    ],
    "Mouth Cancer": [
        "Mouth sore", "White/red patches in mouth", "Difficulty swallowing", "Voice changes"
    ],
    "Pancreatic Cancer": [
        "Jaundice", "Abdominal pain", "Back pain", "Unexplained weight loss", "Nausea", "New diabetes"
    ],
    "Blood Cancer": [
        "Fever", "Night sweats", "Frequent infections", "Easy bruising", "Swollen lymph nodes", "Bone pain"
    ],
    "Brain Cancer": [
        "Severe headaches", "Seizures", "Vision problems", "Balance issues", "Speech problems", "Personality changes"
    ]
}

female_cancers = {
    "Breast Cancer": [
        "Lump in breast", "Nipple discharge", "Breast pain", "Skin dimpling", "Change in breast size"
    ],
    "Cervical Cancer": [
        "Abnormal bleeding", "Pelvic pain", "Pain during intercourse", "Foul-smelling discharge"
    ]
}
female_cancers.update(male_cancers)  # Women can also have lung, brain, pancreatic, blood cancers etc.

# -------------------------------
# Streamlit UI
# -------------------------------
st.title("🧬 Cancer Symptom Checker")
st.write("This tool helps identify possible cancer risks based on symptoms. Not a medical diagnosis!")

# User Info
name = st.text_input("Enter Name")
age = st.number_input("Enter Age", 1, 120)
gender = st.radio("Select Gender", ["Male", "Female"])
location = st.text_input("Enter Location")
polluted_area = st.checkbox("Is your area highly polluted or near Ganga basin?")

family_history = st.radio("Any family history of cancer?", ["Yes", "No"])

# Show symptoms dynamically
if gender == "Male":
    symptom_db = male_cancers
else:
    symptom_db = female_cancers

st.subheader("Select Your Symptoms")
selected_symptoms = []
for cancer, symptoms in symptom_db.items():
    with st.expander(cancer):
        for s in symptoms:
            if st.checkbox(s):
                selected_symptoms.append(s)

# Prediction Logic
possible_cancers = [c for c, syms in symptom_db.items() if any(s in selected_symptoms for s in syms)]

if st.button("🔍 Predict"):
    if possible_cancers:
        st.success(f"### Based on your symptoms, possible cancer types: {', '.join(possible_cancers)}")
    else:
        st.info("No strong cancer indicators found. Please consult a doctor if symptoms persist.")

# -------------------------------
# PDF Report Generation
# -------------------------------
def generate_pdf():
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", "B", 16)
    pdf.cell(200, 10, "Cancer Symptom Report", ln=True, align="C")

    pdf.set_font("Arial", size=12)
    pdf.ln(10)
    pdf.cell(200, 10, f"Name: {name}", ln=True)
    pdf.cell(200, 10, f"Age: {age}", ln=True)
    pdf.cell(200, 10, f"Gender: {gender}", ln=True)
    pdf.cell(200, 10, f"Location: {location}", ln=True)
    pdf.cell(200, 10, f"Pollution Risk Area: {'Yes' if polluted_area else 'No'}", ln=True)
    pdf.cell(200, 10, f"Family History: {family_history}", ln=True)

    pdf.ln(5)
    pdf.set_font("Arial", "B", 14)
    pdf.cell(200, 10, "Selected Symptoms:", ln=True)
    pdf.set_font("Arial", size=12)
    for s in selected_symptoms:
        pdf.cell(200, 8, f"- {s}", ln=True)

    pdf.ln(5)
    pdf.set_font("Arial", "B", 14)
    pdf.cell(200, 10, "Possible Cancer Types:", ln=True)
    pdf.set_font("Arial", size=12)
    if possible_cancers:
        for c in possible_cancers:
            pdf.cell(200, 8, f"- {c}", ln=True)
    else:
        pdf.cell(200, 8, "No significant risk detected.", ln=True)

    pdf.ln(10)
    pdf.set_font("Arial", "I", 11)
    pdf.multi_cell(0, 10, "Disclaimer: This is not a medical diagnosis. Please consult a healthcare professional for further evaluation.")

    return pdf.output(dest="S").encode("latin-1")

if st.button("📄 Download PDF Report"):
    if name and age:
        pdf_data = generate_pdf()
        st.download_button("Download Report", data=pdf_data, file_name="cancer_report.pdf", mime="application/pdf")
    else:
        st.error("Please enter your Name and Age before downloading the report.")
