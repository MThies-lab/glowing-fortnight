# ...existing code...
import os, time, requests
from openai import OpenAI
try:
    from openai.error import APIConnectionError
except Exception:
    APIConnectionError = Exception  # fallback if specific class missing

print("OPENAI_API_KEY present:", bool(os.environ.get("OPENAI_API_KEY")))

def http_test():
    try:
        r = requests.get(
            "https://api.openai.com/v1/models",
            timeout=8,
            headers={"Authorization": f"Bearer {os.environ.get('OPENAI_API_KEY')}"}
        )
        print("HTTP test:", r.status_code, r.ok)
        return r.ok
    except Exception as e:
        print("HTTP test failed:", e)
        return False

client = OpenAI()

payload = {
    "model": "gpt-3.5-turbo",
    "messages": [{"role": "system", "content": analysis}],
    "temperature": 0.8,
    "top_p": 1,
}

def call_with_retries(payload, max_retries=4):
    delay = 1.0
    for attempt in range(1, max_retries + 1):
        try:
            return client.chat.completions.create(**payload)
        except APIConnectionError as e:
            print(f"APIConnectionError attempt {attempt}/{max_retries}:", e)
            if attempt == max_retries:
                raise
            time.sleep(delay)
            delay *= 2

if not http_test():
    print("Cannot reach api.openai.com — check network/proxy/firewall or try a different network.")
else:
    resp = call_with_retries(payload)
    print(resp.choices[0].message.content)
# ...existing code...