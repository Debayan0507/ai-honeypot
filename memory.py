memory_store = {}

def store_message(convo_id: str, role: str, content: str):
    if convo_id not in memory_store:
        memory_store[convo_id] = []
    memory_store[convo_id].append({
        "role": role,
        "content": content
    })

def get_history(convo_id: str):
    return memory_store.get(convo_id, [])
