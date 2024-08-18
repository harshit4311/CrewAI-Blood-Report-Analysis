# Blood Report Analysis using CrewAI

This project is powered by CrewAI and is designed to automate the analysis of blood test reports to provide personalized health recommendations. 

Leveraging the powerful CrewAI framework, this multi-agent system performs the following tasks:

- **Input:** The system accepts a sample blood test report for analysis.

- **Analysis:** Using the **Blood Test Analyst** agent, the system analyzes the blood test report and summarizes the key health indicators in an easy-to-understand manner.

- **Find Articles:** The **Health Article Researcher** agent then searches the web for relevant health articles tailored to the individual’s health needs based on the blood test results.

- **Recommendations:** Finally, the **Health Advisor** agent provides personalized health recommendations and includes links to the relevant articles for further reading.

This template is designed to help you set up a multi-agent AI system, leveraging CrewAI’s framework to enable effective collaboration among agents. The aim is to maximize the collective intelligence and capabilities of the agents, ensuring comprehensive and actionable health insights.

## What is CrewAI?

CrewAI is a flexible and powerful framework designed to create, manage, and deploy multi-agent AI systems for real-world use cases. It allows you to define and configure AI agents that can work together on complex tasks, streamlining processes and providing intelligent solutions.

### Framework Overview

CrewAI uses a structured approach where agents are defined with specific roles and tasks. The framework allows you to customize agents, configure their tasks, and integrate various tools to achieve your objectives. Agents can be configured through `agents.yaml`, and their tasks are defined in `tasks.yaml`.

### AI Agents and Tasks

In this project, we used AI agents to analyze blood test reports, search for health-related articles, and provide health recommendations. The key agents and their tasks are:

- **Health Report Analyzer:** This agent reads and analyzes the blood test report, summarizing the findings in an easy-to-understand manner.
- **Article Researcher:** This agent searches the web for articles tailored to the person's health needs based on the blood test results. We used the Google Serper Search API for this, but Gemini API or OpenAI API could have been used as alternatives.
- **Health Advisor:** Based on the analysis and articles found, this agent provides health recommendations and links to relevant resources.

### End-to-End Process in Detail: What Runs Behind the Code

1. **Input:** The system takes a sample blood test report.
2. **Analysis:** The Health Report Analyzer agent examines the report, highlighting key results and any deviations from the normal range.
3. **Research:** The Article Researcher agent searches the web for relevant health articles using the Google Serper Search API.
4. **Recommendations:** The Health Advisor agent provides personalized health recommendations based on the blood test analysis and the articles found.

## Installation

Ensure you have Python >=3.10 <=3.13 installed on your system. This project uses [Poetry](https://python-poetry.org/) for dependency management.

### Installing CrewAI

To install CrewAI, you can use the following commands:

```
# Install the main CrewAI package
pip install crewai

# Install the main CrewAI package and the tools package
# that includes a series of helpful tools for your agents
pip install 'crewai[tools]'

# Alternatively, you can also use:
pip install crewai crewai-tools
```

## Starting a New CrewAI Project

To create a new CrewAI project, use the following command:

```
crewai create crew <project_name>
```

This will create a new project folder with the following structure:

```
my_project/
├── .gitignore
├── pyproject.toml
├── README.md
└── src/
    └── my_project/
        ├── __init__.py
        ├── main.py
        ├── crew.py
        ├── tools/
        │   ├── custom_tool.py
        │   └── __init__.py
        └── config/
            ├── agents.yaml
            └── tasks.yaml
```

## Customizing Your Project

To customize your project, you can:

- Modify src/my_project/config/agents.yaml to define your agents.
- Modify src/my_project/config/tasks.yaml to define your tasks.
- Modify src/my_project/crew.py to add your own logic, tools, and specific arguments.
- Modify src/my_project/main.py to add custom inputs for your agents and tasks.
- Add your environment variables into the .env file.

## Example: Defining Agents and Tasks

Here’s an example of how you might define ```agents``` and their ```tasks```:

- ### agents.yaml:

1. blood_test_analyst
```
# src/my_project/config/agents.yaml

blood_test_analyst:
  role: >
    Blood Test Analyst
  goal: >
    Analyze the given blood test report and summarize the key health indicators.
  backstory: >
    You are a skilled medical analyst specializing in interpreting blood test results. Your focus is on identifying critical health metrics and abnormalities to provide a clear summary of the individual's health status.
  tasks:
    - analyze_blood_test
```

2. health_article_researcher

```
health_article_researcher:
  role: >
    Health Article Researcher
  goal: >
    Search the internet for health articles that are relevant to the individual's needs based on the blood test analysis.
  backstory: >
    You are an expert in finding reliable health information online. Your ability to sift through vast amounts of data ensures that you can find the most relevant and accurate articles to guide health decisions.
  tasks:
    - search_health_articles
```

3. health_advisor

```
health_advisor:
  role: >
    Health Advisor
  goal: >
    Provide personalized health recommendations based on the blood test analysis and the articles found.
  backstory: >
    You are a health advisor with a deep understanding of nutrition, lifestyle changes, and medical advice. Your recommendations are based on a combination of data analysis and expert knowledge to help individuals improve their health.
  tasks:
    - provide_health_recommendations
```

- ### tasks.yaml:

1. analyze_blood_test

```
analyze_blood_test:
  description: >
    Analyze the blood test report to extract relevant health information.
  expected_output: >
    Summary of the blood test report.
  agent: researcher
  context:
    - researcher
```

2. search_health_articles

```
search_health_articles:
  description: >
    Search for health-related articles based on the provided summary.
  expected_output: >
    List of relevant articles.
  agent: researcher
  context:
    - researcher
```

3. provide_health_recommendations

```
provide_health_recommendations:
  description: >
    Provide health recommendations based on the retrieved articles.
  expected_output: >
    Health recommendations.
  agent: researcher
  context:
    - researcher
```

## Referencing Variables:

Use the annotations to properly reference the agent and task in the crew.py file.

Annotations include:
```
@agent
@task
@crew
@llm
@tool
@callback
@output_json
@output_pydantic
@cache_handler
```

## Installing Dependencies
To install the dependencies for your project, navigate to your project directory:

```
cd my_project

crewai install

poetry lock
poetry install
```
This will install the dependencies specified in the ```pyproject.toml``` file.




## Running the Project

To kickstart your crew of AI agents and begin task execution, run this from the root folder of your project:

```
cd my_project
PYTHONPATH=./src python -m my_project.main
```
This command initializes the MyProject Crew, assembling the agents and assigning them tasks as defined in your configuration.

## Reset Crew Memory
If you need to reset the memory of your crew before running it again, you can do so by calling the reset memory feature:

```crewai reset-memory```

This will clear the crew's memory, allowing for a fresh start.

## Deploying Your Project (Still in BETA)

The easiest way to deploy your crew is through [CrewAI+](https://www.crewai.com/crewaiplus) (still in Beta but you can apply for early access), where you can deploy your crew in a few clicks.


## Support

For support, questions, or feedback regarding the MyProject Crew or CrewAI:

- Visit CrewAI's [website](https://www.crewai.com/)
- Check out their [documentation](https://docs.crewai.com/)
- [Chat with CrewAI's docs](https://chatg.pt/DWjSBZn)
- Join thier [Discord community](https://discord.com/invite/X4JWnZnxPb)
- Read thier [blog](https://www.crewai.com/blog)

