from openai import OpenAI
import os

from retriever import retrieve_relevant_chunks
from context_builder import build_context


client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY")
)


def answer_with_knowledge(query: str):

    results = retrieve_relevant_chunks(
        query=query,
        results_count=5
    )

    context = build_context(results)

    prompt = f"""
You are Jarvis, a fire inspection and fire code assistant.

Answer the user's question using ONLY the retrieved context below.
If the context does not contain enough information, say that the knowledge base does not contain enough information yet.

Retrieved Context:
{context}

User Question:
{query}

Answer clearly and professionally for a Certified Fire Inspector.
"""

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {
                "role": "system",
                "content": "You are a precise fire code retrieval assistant."
            },
            {
                "role": "user",
                "content": prompt
            }
        ],
        temperature=0.2
    )

    return response.choices[0].message.content