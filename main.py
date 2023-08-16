import os
import re
import shutil
import fitz  # PyMuPDF library

# Define paths to input and output folders
input_folder = "input_resumes"
output_folder = "output_resumes"
requirement_file = "requirement.txt"

# Load content from the requirement file
with open(requirement_file, 'r') as req_file:
    requirements = req_file.read()

# Ensure the output folder exists
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# Process each PDF file in the input folder
for pdf_file in os.listdir(input_folder):
    if pdf_file.endswith(".pdf"):
        pdf_path = os.path.join(input_folder, pdf_file)
        
        # Extract text from the PDF file
        pdf_document = fitz.open(pdf_path)
        text = ""
        for page_num in range(pdf_document.page_count):
            page = pdf_document[page_num]
            text += page.get_text()

        # Check if the extracted text contains content from the requirement file
        if re.search(requirements, text, re.IGNORECASE):
            # Move the PDF file to the output folder
            output_path = os.path.join(output_folder, pdf_file)
            shutil.copy(pdf_path, output_path)
            print(f"Match found in '{pdf_file}' - Copied to '{output_folder}'")

        pdf_document.close()

print("Processing completed.")
