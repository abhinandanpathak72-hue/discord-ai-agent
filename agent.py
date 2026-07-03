from dotenv import load_dotenv
load_dotenv()
import os

from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.agents import create_agent
from langchain.tools import tool
from langchain.messages import HumanMessage
from tavily import TavilyClient


tavily_client = TavilyClient(api_key= os.getenv("TAVILY_API_KEY"))


@tool

def SurfInternet(query:str):
    """USE THIS TOOL TO GET LATEST INFORMATION FROM INTERNET"""
    
    result = tavily_client.search(query=query)
    
    return str(result)
    

model = ChatGoogleGenerativeAI(model = "gemini-2.5-flash")
agent = create_agent(model= model, tools = [SurfInternet], system_prompt= "provide clean out to the user")
