import os
from dotenv import load_dotenv

# Load the .env file
load_dotenv()

OPENAI_API_KEY = os.environ.get("OPENAI_API_KEY")

if not OPENAI_API_KEY:
    raise Exception("No OpenAI API key found. Please add it to the .env file.")