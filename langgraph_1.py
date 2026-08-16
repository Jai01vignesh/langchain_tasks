from dotenv import load_dotenv
from langchain.agents import create_agent
from tavily import TavilyClient
from langchain.tools import tool
load_dotenv()
tavily_api = TavilyClient()

system_prompt = """You are mosquito bhat, a multistar michelin and a famous chef in India and also a weatherman. You know A to Z in cooking, poems and weatherman. Even with a mosquito egg you will cook biriyani. Your job is to give cooking reciepe suggestions based on the ingredients user says. Your tone should be polite and witty. 
                    Make your answers grounded and don't hallucinate.Keep your response within 500 tokens"""


@tool
def get_weather(prompt):
    """ Use this to fetch weather data from web"""
    return tavily_api.search(prompt)


@tool
def write_poems(prompt):
    """ Use this to write poems for food, weather based on the poem samples from the web"""
    return tavily_api.search(prompt)



model_tool = create_agent(model="groq:openai/gpt-oss-20b", 
                     system_prompt=system_prompt,
                     tools = [get_weather,
                              write_poems],
                     #checkpointer= InMemorySaver()
                     )