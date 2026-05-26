from web_research.online_reader import read_webpage
from web_research.trusted_sources import (
    TRUSTED_FIRE_CODE_SOURCES
)

from ai.openai_service import client


def answer_with_online_research(query: str):

    collected_context = ""

    for source in TRUSTED_FIRE_CODE_SOURCES[:3]:

        try:
            print(f"Reading: {source['name']}")

            text = read_webpage(source["url"])

            collected_context += f"""

SOURCE:
{source['name']}

CONTENT:
{text[:4000]}

"""

        except Exception as e:
            print(f"Failed source: {source['name']}")
            print(e)

    prompt = f"""
You are Jarvis, an advanced fire inspection
and fire code assistant.

Use the retrieved online fire-code references below
to help answer the user's question.

USER QUESTION:
{query}

ONLINE RESEARCH:
{collected_context}

Provide a professional fire-code-focused answer.
"""

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {
                "role": "system",
                "content": "You are a fire-code research assistant."
            },
            {
                "role": "user",
                "content": prompt
            }
        ],
        temperature=0.2
    )

    return response.choices[0].message.content