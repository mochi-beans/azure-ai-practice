from app.memory_store import (
    get_or_create_session,
    add_message,
    get_messages
)
from app.knowledge_store import search_knowledge
from app.llm_client import ask_llm

MAX_HISTORY = 10  # 後で効いてくる

def chat(session_id: str, user_message: str):
    # セッション取得
    messages = get_or_create_session(session_id)

    # ユーザー発言追加
    add_message(session_id, "user", user_message)

    # 履歴制限
    trimmed_messages = trim_messages(messages)

    # ===== ここからRAG追加 =====

    # ナレッジ検索
    knowledge = search_knowledge(user_message)

    # 元のsystem取り出し
    base_system = trimmed_messages[0]

    if knowledge:
        context_text = "\n".join(knowledge)

        merged_system = {
            "role": "system",
            "content": f"""
    {base_system['content']}

    以下の情報を参考に回答してください:
    {context_text}
    """
        }
    else:
        merged_system = base_system

    # system以外の履歴
    rest_messages = trimmed_messages[1:]

    # 最終メッセージ
    rag_messages = [merged_system] + rest_messages

    # ===== ここまで =====

    # ログ
    print("=== BEFORE LLM ===")
    for m in rag_messages:
        print(m)
    print("==================")

    # LLM呼び出し
    assistant_reply = ask_llm(rag_messages)

    # 応答を履歴に追加
    add_message(session_id, "assistant", assistant_reply)

    return assistant_reply


def trim_messages(messages: list):
    """
    systemは残して、最新N件だけ使う
    """
    system = messages[0]
    rest = messages[1:]

    return [system] + rest[-MAX_HISTORY:]