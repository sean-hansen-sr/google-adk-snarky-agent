from google.adk.agents import Agent
from google.adk.tools import VertexAiSearchTool
from.external_variables import *
    
base_agent = Agent(
    name="base_nurse_call_agent",
    model="gemini-2.0-flash",
    description="Agent to answer IT questions.",
    instruction="""I am a snarky IT agent. I will answer your questions with a touch of sarcasm and wit, 
    but always provide the information you need.
    """,
    tools=[VertexAiSearchTool(data_store_id=os.environ.get(DATASTORE_ID))]
)
