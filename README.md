# Azure OpenAI Chat Practice

## 概要

Azure OpenAIとPythonを用いて、ユーザー入力に対するAI応答を取得するシンプルな処理を実装したプロジェクトです。

## 使用技術

* Python 3.12
* Azure OpenAI
* OpenAI Python SDK

## 実装内容

* Azure OpenAIへの接続
* ユーザー入力に対するAI応答取得

## 起動方法

```bash
pip install fastapi uvicorn openai python-dotenv
python app/llm.py
```

## 環境変数

`.env`ファイルを作成し、以下を設定してください。

```
AZURE_OPENAI_API_KEY=your_api_key
AZURE_OPENAI_ENDPOINT=https://your-resource.openai.azure.com/
AZURE_OPENAI_MODEL=your_deployment_name
```

## 工夫・学び

Azure OpenAIでは、エンドポイントやAPIの種類（Chat Completions / Responses）、
デプロイ名とモデル名の違いに注意が必要であることを理解した。

## 今後の予定

* FastAPIによるAPI化
* チャット履歴管理
* ストリーミング対応
* RAG（Azure AI Search）
