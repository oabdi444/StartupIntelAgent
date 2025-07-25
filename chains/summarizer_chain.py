from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from langchain_google_genai import ChatGoogleGenerativeAI

llm = ChatGoogleGenerativeAI(model="models/gemini-1.5-pro-latest")

prompt = PromptTemplate(
    input_variables=["raw_info"],
    template="""
    You are an AI assistant creating structured startup intelligence reports.
    Based on the raw information below, generate a detailed report with sections:
    - Executive Summary
    - Key Startups
    - Market Trends
    - Notable Fundings

    Raw Info:
    {raw_info}
    """
)

summarize_chain = LLMChain(llm=llm, prompt=prompt)

def summarize_report(raw_info: str) -> str:
    return summarize_chain.run(raw_info)