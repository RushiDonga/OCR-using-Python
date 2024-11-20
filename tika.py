from tika import parser
import re
import json

def extract_text_with_tika(pdf_path):
    try:
        parsed = parser.from_file(pdf_path)
        return parsed.get("content", "").strip()
    except Exception as e:
        print(f"Error extracting text with Tika: {e}")
        return ""

def extract_patient_info(text):
    info = {}

    # Extract patient name
    name_match = re.search(r"(?i)\bName\s*:\s*([A-Za-z\s]+)", text)
    if name_match:
        info['Name'] = name_match.group(1).strip()

    # Extract age
    age_match = re.search(r"(?i)\bAge\s*:\s*(\d+)", text)
    if age_match:
        info['Age'] = age_match.group(1).strip()

    # Extract gender
    gender_match = re.search(r"(?i)\bGender\s*:\s*(Male|Female|Other)", text)
    if gender_match:
        info['Gender'] = gender_match.group(1).strip()

    # Extract medicines
    medicines_match = re.search(r"(?i)\bMedicines\s*:\s*([\w\s,]+)", text)
    if medicines_match:
        info['Medicines'] = [med.strip() for med in medicines_match.group(1).split(",")]

    # Extract other important information
    other_info_match = re.search(r"(?i)\bOther Information\s*:\s*(.+)", text)
    if other_info_match:
        info['Other Information'] = other_info_match.group(1).strip()

    return info

def process_pdf_with_tika(pdf_path, output_json_path):

    text = extract_text_with_tika(pdf_path)
    if not text:
        print("No text extracted from the PDF.")
        return

    patient_info = extract_patient_info(text)

    with open(output_json_path, "w", encoding="utf-8") as json_file:
        json.dump(patient_info, json_file, indent=4)
    
    print(f"Patient information extracted and saved to: {output_json_path}")

if __name__ == "__main__":
    pdf_path = "patient_report.pdf" 
    output_json_path = "patient_info.json" 
    process_pdf_with_tika(pdf_path, output_json_path)
