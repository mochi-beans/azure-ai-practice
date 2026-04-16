import os
from openai import AzureOpenAI
from dotenv import load_dotenv

load_dotenv()

client = AzureOpenAI(
    api_key=os.getenv("AZURE_OPENAI_API_KEY"),
    api_version="2024-02-01",
    azure_endpoint=os.getenv("AZURE_OPENAI_ENDPOINT")
)

def ask_llm(message: str) -> str:
    response = client.chat.completions.create(
        model=os.getenv("AZURE_OPENAI_MODEL"),
        messages=[
            {"role": "user", "content": message}
        ]
    )
    return response.choices[0].message.content

print("ENDPOINT:", os.getenv("AZURE_OPENAI_ENDPOINT"))
if __name__ == "__main__":
    print(ask_llm("こんにちは、自己紹介して"))