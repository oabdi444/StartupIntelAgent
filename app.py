from dotenv import load_dotenv
load_dotenv()
from langchain.agents import initialize_agent, Tool
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.agents.agent_types import AgentType

from tools.producthunt import get_top_producthunt_startups
from tools.crunchbase import get_crunchbase_data
from tools.serp_search import search_google
from chains.summarizer_chain import summarize_report

llm = ChatGoogleGenerativeAI(model="models/gemini-1.5-pro-latest")

tools = [
    Tool(
        name="ProductHunt Tool",
        func=get_top_producthunt_startups,
        description="Fetch top startups from Product Hunt for a given topic."
    ),
    Tool(
        name="Crunchbase Tool",
        func=get_crunchbase_data,
        description="Fetch Crunchbase data for a given startup name."
    ),
    Tool(
        name="Search Tool",
        func=search_google,
        description="Perform a Google search and return summaries of results."
    )
]

agent = initialize_agent(
    tools,
    llm,
    agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
    verbose=True
)

if __name__ == "__main__":
    query = input("Enter your startup research topic: ")
    response = agent.run(query)
    final_summary = summarize_report(response)
    print("\n\n====== Startup Intelligence Report ======\n")
    print(final_summary)