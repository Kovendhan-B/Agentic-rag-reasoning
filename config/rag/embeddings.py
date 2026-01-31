from openai import OpenAI

client = OpenAI()

def embed(texts):
    return client.embeddings.create(
        model="text-embedding-3-small",
        input=texts
    ).data
