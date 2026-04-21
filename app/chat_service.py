from app.memory_store import (
    get_or_create_session,
    add_message,
    get_messages
)
from app.llm_client import ask_llm

MAX_HISTORY = 10  # 後で効いてくる

def chat(session_id: str, user_message: str):
    # セッション取得
    messages = get_or_create_session(session_id)

    # ユーザー発言追加
    add_message(session_id, "user", user_message)

    # 履歴制限（system + 最新N件）
    trimmed_messages = trim_messages(messages)

    # 暫く、履歴確認用ログを残す
    print("=== BEFORE LLM ===")
    for m in trimmed_messages:
        print(m)
    print("==================")

    # LLM呼び出し
    assistant_reply = ask_llm(trimmed_messages)

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