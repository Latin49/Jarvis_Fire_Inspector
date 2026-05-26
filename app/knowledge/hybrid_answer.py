import sys

sys.path.append("app")
sys.path.append("app/knowledge")
sys.path.append("app/web_research")

from rag_answer import answer_with_knowledge
from web_rag import answer_with_online_research


def answer_with_hybrid_research(query: str):

    local_answer = answer_with_knowledge(query)

    if "does not contain enough information" not in local_answer.lower():
        return local_answer

    online_answer = answer_with_online_research(query)

    return online_answer