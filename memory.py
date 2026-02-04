memory = {}

def store_message(conversation_id, role, content):
    if conversation_id not in memory:
        memory[conversation_id] = []
    memory[conversation_id].append({
        "role": role,
        "content": content
    })

def get_history(conversation_id):
    return memory.get(conversation_id, [])
