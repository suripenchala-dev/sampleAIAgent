import json
import os

from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client = OpenAI(
    api_key=os.getenv("GEMINI_API_KEY"),
    base_url="https://generativelanguage.googleapis.com/v1beta/",
)

response = client.chat.completions.create(
    model="gemini-3-flash-preview",
    messages=[
        {
            "role": "system",
            "content": "You are a senior software engineer. Give concise, practical answers.",
        },
        {
            "role": "user",
            "content": "What are the three most important things to know about database indexing?",
        },
    ],
)

answer = response.choices[0].message.content

raw_response = {
    "id": response.id,
    "model": response.model,
    "object": response.object,
    "created": response.created,
    "choices": [
        {
            "index": choice.index,
            "finish_reason": choice.finish_reason,
            "message": {
                "role": choice.message.role,
                "content": choice.message.content,
            },
        }
        for choice in response.choices
    ],
    "usage": {
        "prompt_tokens": response.usage.prompt_tokens if response.usage else None,
        "completion_tokens": response.usage.completion_tokens if response.usage else None,
        "total_tokens": response.usage.total_tokens if response.usage else None,
    },
}

print(json.dumps(raw_response, indent=2))