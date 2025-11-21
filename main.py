import os
import sys
from dotenv import load_dotenv
from google import genai
from google.genai import types

args = sys.argv
if len(args) < 2:
    print("prompt not provided")
    sys.exit(1)

user_prompt = args[1]
messages = [
    types.Content(role="user", parts=[types.Part(text=user_prompt)]),
]

load_dotenv()
api_key = os.environ.get("GEMINI_API_KEY")

client = genai.Client(api_key=api_key)

response = client.models.generate_content(
    model='gemini-2.0-flash-001', contents=messages
)
print(response.text)

print(f'Prompt tokens: {response.usage_metadata.prompt_token_count}')
print(f'Response tokens: {response.usage_metadata.candidates_tokens_details[0].token_count}')