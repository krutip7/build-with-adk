from google.adk.agents import Agent
from google.adk.tools import google_search


# def get_current_time(date_format: str) -> dict:
#     """Get the current time in the specified format."""
#     from datetime import datetime
#     return {'current_time': datetime.now().strftime(date_format)}


root_agent = Agent(
    model='gemini-2.0-flash-lite',
    name='google_search_agent',
    description='A helpful assistant for user questions.',
    instruction="""You are a helpful web search assistant. 
    When a user asks a question, you will search the web for relevant information and provide a concise answer. 
    You must always use the google_search tool to search the web and find information.""",
    tools=[google_search],
)
