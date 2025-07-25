# Startup Intel Agent

**Startup Intel Agent** is an AI-powered research assistant designed to gather, analyze, and summarize startup-related data from multiple sources such as Google Search, ProductHunt, and Crunchbase. Powered by **LangChain** and **Google Gemini**, it provides fast, intelligent market insights for founders, analysts, and investors.

---

## Features

- Real-time startup data extraction via SerpAPI, ProductHunt, and Crunchbase
- Summary generation powered by Google Gemini and LangChain
- Agent-based decision making with modular tools
- Simple, extensible codebase
- Lightweight Streamlit interface

---

## Tech Stack

| Technology        | Purpose                                  |
|-------------------|-------------------------------------------|
| **LangChain**      | LLM orchestration and tool management     |
| **Google Gemini**  | LLM for summarization and reasoning       |
| **Streamlit**      | Interactive frontend interface            |
| **SerpAPI**        | Web search API (Google Search wrapper)    |
| **ProductHunt API**| Startup discovery data                    |
| **Crunchbase API** | Company information lookup                |

---

## Project Structure

startup_intel_agent/
├── app.py # Core agent setup
├── chains/
│ └── summarizer_chain.py # Gemini-based summarization
├── tools/
│ ├── producthunt.py # ProductHunt API wrapper
│ ├── crunchbase.py # Crunchbase API wrapper
│ └── serp_search.py # Google search via SerpAPI
├── frontend/
│ └── streamlit_app.py # UI logic
├── .env # API keys and env vars
├── setup.py # Editable package installation
└── README.md



---
Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/yourusername/startup-intel-agent.git
cd startup-intel-agent


conda create -n ai-assistant python=3.11
conda activate ai-assistant

### 3. Install dependencies
pip install -r requirements.txt

### 4. Configure environment variables
Create a .env file in the root directory with the following:

GEMINI_API_KEY=your_gemini_api_key
SERPAPI_API_KEY=your_serpapi_api_key

Optionally, add your Crunchbase and ProductHunt API keys if you're using those tools

### Running the App
From the project root directory:

streamlit run frontend/streamlit_app.py
This will launch a browser window with the Streamlit UI.


### Customization
.Add custom tools to the tools/ directory and register them in app.py
.Replace SerpAPI with another web search tool if preferred
.Extend the summarization logic in chains/summarizer_chain.py
.Enhance the frontend with filters, tags, or export options

### Development Tips
Install the project in editable mode for easier import management:

pip install -e .
Then you can use clean imports like:

python
from startup_intel_agent.chains.summarizer_chain import summarize_report

### License
This project is licensed under the MIT License.

Author
Osman Hassan Abdi
AI/ML Engineer







