import yaml
import os
import requests
from dotenv import load_dotenv
from tabulate import tabulate

# Load environment variables from .env file
load_dotenv()

# Define the path to your config files
config_path = os.path.join(os.path.dirname(__file__), 'config')

def load_yaml(filename):
    with open(os.path.join(config_path, filename), 'r') as file:
        return yaml.safe_load(file)

# Load agents and tasks configuration
agents = load_yaml('agents.yaml')
tasks = load_yaml('tasks.yaml')

API_KEY = os.getenv('SERPER_API_KEY')
SEARCH_URL = 'https://google.serper.dev/search'  # Search the internet 

class Crew:
    def run_task(self, task_name, **kwargs):
        task = tasks.get(task_name)
        if not task:
            raise ValueError(f"Task '{task_name}' not found.")
        if task_name == 'analyze_blood_test':
            return self.analyze_blood_test(**kwargs)
        elif task_name == 'search_health_articles':
            return self.search_health_articles(**kwargs)
        elif task_name == 'provide_health_recommendations':
            return self.provide_health_recommendations(**kwargs)
        else:
            raise ValueError(f"Unknown task '{task_name}'")

    def analyze_blood_test(self, report):
        print("Analyzing report:")
        print(self.format_report(report))
        return "Summary of blood test report"

    def format_report(self, report):
        data = [
            ["Test Name", "Results", "Units", "Bio. Ref. Interval"],
            ["Hemoglobin", "15.00", "g/dL", "13.00 - 17.00"],
            ["Packed Cell Volume (PCV)", "45.00", "%", "40.00 - 50.00"],
            ["RBC Count", "4.50", "mill/mm3", "4.50 - 5.50"],
            ["MCV", "90.00", "fL", "83.00 - 101.00"],
            ["MCH", "32.00", "pg", "27.00 - 32.00"],
            ["MCHC", "33.00", "g/dL", "31.50 - 34.50"],
            ["Red Cell Distribution Width (RDW)", "14.00", "%", "11.60 - 14.00"]
        ]
        return tabulate(data, headers="firstrow", tablefmt="grid")

    def search_health_articles(self, summary):
        print(f"Searching articles based on: {summary[:100]}...")  # Print first 100 characters for brevity
        headers = {
            'X-API-KEY': API_KEY,  # Corrected header key
            'Content-Type': 'application/json'
        }
        json_data = {
            'q': summary,  # Query parameter
            'num': 10  # No.of results
        }
        response = requests.post(SEARCH_URL, headers=headers, json=json_data)
        if response.status_code == 200:
            data = response.json()
            articles = [item.get('link') for item in data.get('organic', [])] 
            return articles
        else:
            print("Error fetching articles:", response.status_code, response.text)
            return []

    def provide_health_recommendations(self, articles):
        print(f"Providing recommendations based on: {articles}")
        
        if articles:
            recommendations = [
                f"Check out these articles for more information on blood test results:\n"
                + "\n".join([f"- {article}" for article in articles])
            ]
        else:
            # General health advice if no specific articles are found
            recommendations = [
                "Here are some general health recommendations:",
                "- Drink plenty of water.",
                "- Avoid alcohol and smoking.",
                "- Ensure adequate vitamin D exposure.",
                "- Maintain a balanced diet and exercise regularly."
            ]
        
        # Join recommendations into a single string for output
        return "\n".join(recommendations)

crew = Crew()
