import os

# Read API key from file and set it for this notebook session
with open("DALLE_Key") as f:
    os.environ["OPENAI_API_KEY"] = f.read().strip()