from fastapi import FastAPI
from pydantic import BaseModel
from app.chat_service import chat
from app.memory_store import get_messages, clear_session

app = FastAPI()

class ChatRequest(BaseModel):
    session_id: str
    message: str

@app.post("/chat")
def chat_api(req: ChatRequest):
    reply = chat(req.session_id, req.message)
    return {"reply": reply}

@app.get("/history/{session_id}")
def get_history(session_id: str):
    return {"messages": get_messages(session_id)}

@app.delete("/history/{session_id}")
def delete_history(session_id: str):
    clear_session(session_id)
    return {"status": "deleted"}