# src/my_project/crew.py

import yaml
import os
import requests

# Define the path to your config files
config_path = os.path.join(os.path.dirname(__file__), 'config')

def load_yaml(filename):
    with open(os.path.join(config_path, filename), 'r') as file:
        return yaml.safe_load(file)

# Load agents and tasks configuration
agents = load_yaml('agents.yaml')
tasks = load_yaml('tasks.yaml')

# Define your API key and endpoint
API_KEY = 'cd649edae1b327a6eef39dbddc97f00d5b71e9f2debe21f475645a1018b20869'  # Replace with your actual API key
SEARCH_URL = 'https://api.serper.dev/search'

class Crew:
    def run_task(self, task_name, **kwargs):
        task = tasks.get(task_name)
        if not task:
            raise ValueError(f"Task '{task_name}' not found.")
        # Task handling logic
        if task_name == 'analyze_blood_test':
            return self.analyze_blood_test(**kwargs)
        elif task_name == 'search_health_articles':
            return self.search_health_articles(**kwargs)
        elif task_name == 'provide_health_recommendations':
            return self.provide_health_recommendations(**kwargs)
        else:
            raise ValueError(f"Unknown task '{task_name}'")

    def analyze_blood_test(self, report):
        print(f"Analyzing report: {report[:1000]}...")  # Print first 1000 characters for brevity
        # Dummy implementation - replace with actual analysis logic
        return "Summary of blood test report"

    def search_health_articles(self, summary):
        print(f"Searching articles based on: {summary[:100]}...")  # Print first 100 characters for brevity
        params = {
            'q': summary,
            'api_key': API_KEY
        }
        response = requests.get(SEARCH_URL, params=params)
        if response.status_code == 200:
            data = response.json()
            articles = [item['link'] for item in data.get('results', [])]
            return articles
        else:
            print("Error fetching articles:", response.status_code)
            return []

    def provide_health_recommendations(self, articles):
        print(f"Providing recommendations based on: {articles}")
        # Dummy implementation - replace with actual recommendation logic
        return "Recommendations based on articles"

crew = Crew()
