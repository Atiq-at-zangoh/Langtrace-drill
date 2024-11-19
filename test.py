import google.generativeai as genai
import os
from langtrace_python_sdk import langtrace, with_langtrace_root_span  # Must precede any llm module imports
from dotenv import load_dotenv
load_dotenv()

langtrace.init(api_key=os.getenv("LANGTRACE_API_KEY"))


@with_langtrace_root_span("chat_complete")
def chat_complete():
    model = genai.GenerativeModel("gemini-1.5-flash")
    genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

    chat_response = genai.ChatSession(
        model=model,
        response=model.generate_content("Write a story about a magic backpack.")

    )
    print(chat_response.text)
    print(chat_response.choices[0].response.content)

chat_complete()

