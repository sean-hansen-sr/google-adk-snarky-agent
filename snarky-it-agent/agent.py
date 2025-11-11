from google.adk.agents import Agent
from google.adk.models.google_llm import Gemini
from google.genai import types
from google.adk.tools import VertexAiSearchTool

retry_config = types.HttpRetryOptions(
    attempts=5,  # Maximum retry attempts
    exp_base=7,  # Delay multiplier
    initial_delay=1,
    http_status_codes=[429, 500, 503, 504]  # Retry on these HTTP errors
)

base_agent = Agent(
    name="base_it_agent",
    model=Gemini(model="gemini-2.5-flash", retry_options=retry_config),
    description="Agent to answer IT questions.",
    instruction="""I am a snarky IT agent. I will answer your questions with a touch of sarcasm and wit, 
    but always provide the information you need.
    """,
    generate_content_config=types.GenerateContentConfig(
        max_output_tokens=10240,
        temperature=0.2,
        stop_sequences=["### End"],
        safety_settings=[
            types.SafetySetting(
                category=types.HarmCategory.HARM_CATEGORY_HATE_SPEECH,
                threshold=types.HarmBlockThreshold.BLOCK_LOW_AND_ABOVE
            )
        ]
    ),
    tools=[VertexAiSearchTool(data_store_id=os.environ.get(DATASTORE_ID))]
)
