import os 
import sys
from dotenv import load_dotenv
from google import genai
from google.genai import types



load_dotenv()
api_key = os.environ.get("GEMINI_API_KEY")

show_text = 0

if len(sys.argv) < 2:
    print("No text provided")
    exit(1)
elif len(sys.argv) > 2:
    if sys.argv[2] == "--verbose":
        show_text = 1
    user_prompt = sys.argv[1]
else:
    user_prompt = sys.argv[1]

messages = [
    types.Content(role="user", parts=[types.Part(text=user_prompt)],)
]

client = genai.Client(api_key=api_key)

def main(messages):

    model = "gemini-2.0-flash-001"
    contents = messages

    response = client.models.generate_content(
        model=model, contents=messages
    )
    if show_text == 1:
        print(f"User prompt: {user_prompt}")
        print(f"Prompt tokens: {response.usage_metadata.prompt_token_count}")
        print(f"Response tokens: {response.usage_metadata.candidates_token_count}")
    print(response.text)

main(messages)