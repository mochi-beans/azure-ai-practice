# knowledge_store.py

KNOWLEDGE = [
    "有給は入社半年後に付与される",
    "残業は月45時間まで",
    "出勤率が一定以上である必要がある",
    "交通費は月3万円まで支給される",
    "リモートワークは週3日まで可能"
]


def search_knowledge(query: str):
    results = []

    for doc in KNOWLEDGE:
        if any(word in doc for word in query):
            results.append(doc)

    return results[:3]  # とりあえず上位3件