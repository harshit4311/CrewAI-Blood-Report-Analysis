import yaml
import os
import requests
from dotenv import load_dotenv
from tabulate import tabulate

load_dotenv()

config_path = os.path.join(os.path.dirname(__file__), 'config')

def load_yaml(filename):
    with open(os.path.join(config_path, filename), 'r') as file:
        return yaml.safe_load(file)

agents = load_yaml('agents.yaml')
tasks = load_yaml('tasks.yaml')

API_KEY = os.getenv('SERPER_API_KEY')
SEARCH_URL = 'https://google.serper.dev/search'  # Search the internet using Google Seper Search API

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
            # Ensure 'report' is included in kwargs
            return self.provide_health_recommendations(
                articles=kwargs.get('articles', []),
                report=kwargs.get('report', '')
            )
        else:
            raise ValueError(f"Unknown task '{task_name}'")

    def analyze_blood_test(self, report):
        print("Analyzing report:")
        formatted_report = self.format_report(report)
        print(formatted_report)
        
        # Example of results analysis
        recommendations = []
        
        # Blood test data (could be dynamically extracted from the report)
        test_data = {
            "Hemoglobin": {"result": 15.00, "interval": (13.00, 17.00)},
            "Packed Cell Volume (PCV)": {"result": 45.00, "interval": (40.00, 50.00)},
            "RBC Count": {"result": 4.50, "interval": (4.50, 5.50)},
            "MCV": {"result": 90.00, "interval": (83.00, 101.00)},
            "MCH": {"result": 32.00, "interval": (27.00, 32.00)},
            "MCHC": {"result": 33.00, "interval": (31.50, 34.50)},
            "Red Cell Distribution Width (RDW)": {"result": 14.00, "interval": (11.60, 14.00)},
        }
        
        for test, data in test_data.items():
            result = data["result"]
            low, high = data["interval"]
            if result < low:
                recommendations.append(f"{test} is below the normal range. Consider increasing intake of foods rich in this nutrient or consult a healthcare provider.")
            elif result > high:
                recommendations.append(f"{test} is above the normal range. This could indicate a potential health issue. Please consult a healthcare provider for further investigation.")
            else:
                recommendations.append(f"{test} is within the normal range.")

        return "\n".join(recommendations)

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
        print(f"Searching articles based on: {summary[:100]}...") 
        headers = {
            'X-API-KEY': API_KEY,  
            'Content-Type': 'application/json'
        }
        json_data = {
            'q': summary,  
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

    def provide_health_recommendations(self, articles, report):
        print(f"Providing recommendations based on: {articles}")

        # Generate recommendations based on articles
        recommendations = []
        if articles:
            recommendations.append(
                "Check out these articles for more information on blood test results:"
                "\n" + "\n".join([f"- {article}" for article in articles])
            )
        
        # Analyze the blood test report for specific recommendations
        report_recommendations = self.analyze_blood_test(report)
        recommendations.append(report_recommendations)
        
        # Always include general recommendations
        recommendations.append(
            "\nAdditionally, here are some general health recommendations:"
            "\n- Drink plenty of water."
            "\n- Avoid alcohol and smoking."
            "\n- Ensure adequate vitamin D exposure."
            "\n- Maintain a balanced diet and exercise regularly."
        )
            
        return "\n".join(recommendations)

# Execution logic
if __name__ == "__main__":
    crew = Crew()
    
    report_summary = "Summary of blood test report"  # This should be your actual report summary
    articles = crew.search_health_articles(report_summary)  # Example call to get articles

    recommendations = crew.run_task('provide_health_recommendations', articles=articles, report=report_summary)
    print(recommendations)
