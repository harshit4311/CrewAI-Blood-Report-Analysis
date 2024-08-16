# src/my_project/main.py

import fitz  # PyMuPDF
import os
from my_project.crew import crew  # Use absolute import

def extract_text_from_pdf(pdf_path):
    text = ""
    doc = fitz.open(pdf_path)
    for page in doc:
        text += page.get_text()
    doc.close()
    return text

def main():
    # Path to the PDF report
    pdf_path = '/Users/harshit/Programming/Web Development/my_project/BloodTest-Report.pdf'

    # Extract text from the PDF report
    sample_report = extract_text_from_pdf(pdf_path)

    # Run the tasks in sequence
    summary = crew.run_task('analyze_blood_test', report=sample_report)
    articles = crew.run_task('search_health_articles', summary=summary)
    recommendations = crew.run_task('provide_health_recommendations', articles=articles)

    # Output the results
    print("Health Summary:", summary)
    print("Recommended Articles:", articles)
    print("Health Recommendations:", recommendations)

if __name__ == "__main__":
    main()
