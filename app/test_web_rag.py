from web_research.web_rag import (
    answer_with_online_research
)

question = "What is the purpose of NFPA 10?"

answer = answer_with_online_research(question)

print("\nONLINE JARVIS ANSWER:\n")
print(answer)