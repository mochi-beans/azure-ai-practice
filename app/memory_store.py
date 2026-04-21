from typing import Dict, List

chat_store: Dict[str, List[dict]] = {}

SYSTEM_PROMPT = """
あなたは会話型のAIアシスタントです。
ユーザーとの会話履歴を必ず参照し、文脈を踏まえて自然に会話を続けてください。
単発の質問として扱わず、前後の流れを理解して回答してください。
"""

def get_or_create_session(session_id: str):
    if session_id not in chat_store:
        chat_store[session_id] = [
            {"role": "system", "content": SYSTEM_PROMPT}
        ]
    return chat_store[session_id]

def add_message(session_id: str, role: str, content: str):
    chat_store[session_id].append({
        "role": role,
        "content": content
    })

def get_messages(session_id: str):
    return chat_store.get(session_id, [])

def clear_session(session_id: str):
    if session_id in chat_store:
        del chat_store[session_id]