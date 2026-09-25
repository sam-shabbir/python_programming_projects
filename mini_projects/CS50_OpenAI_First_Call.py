# pip install openai
# Set your API key as an environment variable first (never paste it into the code):
#   Windows PowerShell:  $env:OPENAI_API_KEY = "your-key-here"

from openai import OpenAI # FIX: the package name is lowercase `openai` (Python imports are case-sensitive); the class inside is `OpenAI`
# API = application programming interface

client = OpenAI () # reads OPENAI_API_KEY from the environment automatically

response = client.responses.create(
    input = "In one sentence, what is CS50?",
    model = "gpt-5"
)

print(response.output_text)
