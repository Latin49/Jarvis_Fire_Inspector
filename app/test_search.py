from knowledge.retriever import retrieve_relevant_chunks
from knowledge.context_builder import build_context


query = "What are the requirements for blocked exits or means of egress?"


results = retrieve_relevant_chunks(
    query=query,
    results_count=5
)


context = build_context(results)


print("\nRETRIEVED CONTEXT:\n")
print(context)