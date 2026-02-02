from config.llm import get_gemini

client = get_gemini()

for m in client.models.list():
    print(m.name)
