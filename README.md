# Startup Intel Agent

Startup Intel Agent is an AI-powered research assistant designed to gather, summarize, and analyze startup-related data from multiple sources including Google Search, ProductHunt, and Crunchbase. Built with LangChain and Google Gemini, it enables fast and intelligent market research for founders, analysts, and investors.

## Features

- Searches and extracts startup information in real-time
- Summarizes key insights using Google Gemini via LangChain
- Agent-based reasoning with multiple tools
- Modular, extensible codebase
- Lightweight Streamlit frontend

## Tech Stack

| Technology      | Description                          |
|-----------------|--------------------------------------|
| LangChain       | LLM orchestration and tool integration |
| Google Gemini   | Large Language Model for summaries    |
| Streamlit       | Frontend interface                   |
| SerpAPI         | Google Search result API             |
| ProductHunt API | Startup discovery                    |
| Crunchbase API  | Company information                  |

## Project Structure

startup_intel_agent/
├── app.py # Core agent logic
├── chains/
│ └── summarizer_chain.py # Summarization chain using Gemini
├── tools/
│ ├── producthunt.py # ProductHunt scraping
│ ├── crunchbase.py # Crunchbase integration
│ └── serp_search.py # Google Search via SerpAPI
├── frontend/
│ └── streamlit_app.py # Streamlit UI
├── .env # Environment variables
├── setup.py # Editable install configuration
└── README.md

bash
Copy
Edit

## Setup Instructions

### 1. Clone the repository

```bash
git clone https://github.com/yourusername/startup-intel-agent.git
cd startup-intel-agent
2. Set up a virtual environment
bash
Copy
Edit
conda create -n ai-assistant python=3.11
conda activate ai-assistant
3. Install dependencies
bash
Copy
Edit
pip install -r requirements.txt
4. Configure environment variables
Create a .env file in the project root with the following keys:

ini
Copy
Edit
GEMINI_API_KEY=your_gemini_api_key
SERPAPI_API_KEY=your_serpapi_api_key
(Optional) Add keys for Crunchbase and ProductHunt APIs if required.

Running the App
From the project root directory, launch the Streamlit UI:

bash
Copy
Edit
streamlit run startup_intel_agent/frontend/streamlit_app.py
This will start a local web app in your browser where you can input topics or startup names and receive structured summaries.

Customization
Add new tools under tools/ and register them in app.py

Modify the summarizer chain to fit different LLM workflows

Replace SerpAPI with other web search providers if needed

Extend the frontend interface with filters, graphs, or export buttons

Development Tips
To enable proper package imports, install the project in editable mode:

bash
Copy
Edit
pip install -e .
This allows you to use package-style imports like:

python
Copy
Edit
from startup_intel_agent.chains.summarizer_chain import summarize_report
License
This project is licensed under the MIT License.

Author
Osman Hassan Abdi
AI/ML Engineer

MIT License
