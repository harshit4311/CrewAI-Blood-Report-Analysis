# src/my_project/main.py

import fitz  # PyMuPDF
import os
from my_project.crew import Crew  # Import the Crew class

def extract_text_from_pdf(pdf_path):
    text = ""
    doc = fitz.open(pdf_path)
    for page in doc:
        text += page.get_text()
    doc.close()
    return text

def main():
    pdf_path = '/Users/harshit/Programming/Web Development/my_project/BloodTest-Report.pdf'

    # Extract text from PDF
    sample_report = extract_text_from_pdf(pdf_path)

    # Create an instance of Crew
    crew = Crew()

    # Run all tasks that would be performed by agents
    summary = crew.run_task('analyze_blood_test', report=sample_report)
    articles = crew.run_task('search_health_articles', summary=summary)
    recommendations = crew.run_task('provide_health_recommendations', articles=articles, report=sample_report)

    print("Health Summary:", summary)
    print("Recommended Articles:", articles)
    print("Health Recommendations:", recommendations)

if __name__ == "__main__":
    main()
