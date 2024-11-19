# Import it into your project
from langtrace_python_sdk import langtrace # Must precede any llm module imports
import os 
from dotenv import load_dotenv
load_dotenv()

langtrace.init(api_key = os.getenv('LANGTRACE_API_KEY'))
print(langtrace)

