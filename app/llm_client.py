from dotenv import load_dotenv
from pathlib import Path
import os
from openai import AzureOpenAI

# プロジェクトルートを取得
BASE_DIR = Path(__file__).resolve().parent.parent

# .envを明示的に読み込む
load_dotenv(dotenv_path=BASE_DIR / ".env")

client = AzureOpenAI(
    api_key=os.getenv("AZURE_OPENAI_API_KEY"),
    api_version="2024-02-15-preview",
    azure_endpoint=os.getenv("AZURE_OPENAI_ENDPOINT")
)

DEPLOYMENT_NAME = os.getenv("AZURE_OPENAI_DEPLOYMENT")

def ask_llm(messages: list):
    response = client.chat.completions.create(
        model=DEPLOYMENT_NAME,
        messages=messages
    )
    return response.choices[0].message.content