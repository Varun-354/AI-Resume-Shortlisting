import pdfplumber

# Path of the resume PDF
resume_path = "Resumes/Sample_Resume_Data.pdf"

# Open and read the PDF
with pdfplumber.open(resume_path) as pdf:
    for page in pdf.pages:
        text = page.extract_text()
        if text:
            print(text)


import re

def preprocess_text(text):
    text = text.lower()
    text = re.sub(r'[^a-z\s]', ' ', text)
    text = re.sub(r'\s+', ' ', text)
    return text.strip()

with pdfplumber.open(resume_path) as pdf:
    for page in pdf.pages:
        raw_text = page.extract_text()
        if raw_text:
            clean_text = preprocess_text(raw_text)
            print(clean_text)

